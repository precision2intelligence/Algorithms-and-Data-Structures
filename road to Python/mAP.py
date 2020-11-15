'''
277-145=132L
首先，有两组三类6个变量：Bbox(det/true),Label(det/true),Score(difficulty)
其次，汇总所有的Bbox、Label、Score分别存储进张量，由于检测模板和真值目标数量不同，所以分开存变量
3，按照类别筛选image，bbox，label，score，筛选利用索引一一对应的关系，过滤出需要的索引，在tensor中寻找
为什么类别是range(1, n_classes)有背景算一类0吧
L194 n_easy_class_objects L198 true_class_boxes_detected
4，把一个类别下检测出来的目标按照Score降序排序，得到调整后的Score，image，bbox。为每个类别下的所有
目标初始化tp和tf张量，维度等于所有的检测目标（0）
5，对于一个类别下的每个目标，找到它的来源图片，按照图片找到gt坐标和难度。这里gt会找到多个，因为找到的是
来源图片中所有的该类别的gt。如原图中没有该类别，fp+1
6，找到det目标和所有gt的IOU，选择最大的作为待匹配框。然后按照得到的索引，返回该类别所有框下的索引org
7，判断IOU是否大于0.5，如否，fp置1；如是，判断是否是忽略项，如否，判断true_class_boxes_detected是否被检测过，
如没有检测过，tp为1，且在tensor中标记已经检测过；如已经被检测过了，fp置1
-------------------------------------------------------------------
8，L254，（按照置信度排序BBox后），××累计××该类别下的tp和fp。
p = tp / tp + fp, r = tp / all_gt
由于是累加的，所以这里得到一组p、r值，将每点（r，p）画出，就得到p-r曲线
11点差值法：就是在[0,0.1,1]的每个recall下，向后搜索比该recall大的precision中最大的一个，作为该点的一个precision
计算p-r曲线下面积：宽为0.1，高为刚刚选出的插值的precision，面积即为AP

9，后面按照每个
注意，true_positives用的维度是detection的类别L215
recall的计算很特别
'''

import torch

def calculate_mAP(det_boxes, det_labels, det_scores, true_boxes, true_labels, true_difficulties):
    """
    Calculate the Mean Average Precision (mAP) of detected objects.
    See https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173 for an explanation
    :param det_boxes: list of tensors, one tensor for each image containing detected objects' bounding boxes
    :param det_labels: list of tensors, one tensor for each image containing detected objects' labels
    :param det_scores: list of tensors, one tensor for each image containing detected objects' labels' scores
    :param true_boxes: list of tensors, one tensor for each image containing actual objects' bounding boxes
    :param true_labels: list of tensors, one tensor for each image containing actual objects' labels
    :param true_difficulties: list of tensors, one tensor for each image containing actual objects' difficulty (0 or 1)
    :return: list of average precisions for all classes, mean average precision (mAP)
    """
    # 第一个易错点：所有list长度相同，因为其等于图片的数量
    assert len(det_boxes) == len(det_labels) == len(det_scores) == len(true_boxes) == len(true_labels) == len(true_difficulties)
    n_classes = 20

    true_images = list()
    for i in range(len(true_boxes)):
        true_images.extend([i] * len(true_boxes[i].size(0))) # 易错：读入具体一个Bbox，里面是（n，4）的张量，要加上size(0)
    true_boxes = torch.cat(true_boxes, dim=0)
    true_labels = torch.cat(true_labels, dim=0)
    true_difficulties = torch.cat(true_difficulties, dim=0)
    assert true_images.size(0) == true_boxes.size(0) == true_labels.size(0) == true_difficulties.size(0) # n_objects

    det_images = list()
    for i in range(len(det_boxes)):
        det_images.extend([i] * len(det_boxes[i]).size(0))
    det_boxes = torch.cat(det_boxes, dim=0)
    det_labels = torch.cat(det_labels, dim=0)
    det_scores = torch.cat(det_scores, dim=0)
    assert det_images.size(0) == det_boxes.size(0) == det_labels.size(0) == det_scores.size(0) # 不是len，是size，张量

    # calculate AP for each class 除去背景
    average_precisions = torch.zeros((n_classes-1), dtype=torch.float)
    for c in range(1, n_classes):
        true_class_images = true_images[true_labels == c]
        true_class_boxes = true_boxes[true_labels == c]
        true_class_difficulties = true_difficulties[true_labels == c]
        # 如何理解这里的容易程度加和
        n_easy_class_objects = (1 - true_class_difficulties).sum().item()

        # 标记已经被检测出来的目标个数
        true_class_boxes_detected = torch.zeros((true_class_boxes.size(0)),dtype=uint8).to(device)


        det_class_images = det_images[det_labels == c]
        det_class_boxes = det_boxes[det_labels == c]
        det_class_scores = det_scores[det_labels == c]
        n_class_detections = det_class_images.size(0)
        if n_class_detections == 0:
            continue

        # sort detection object in decreasing order by score
        det_class_scores, sort_ind = torch.sort(det_class_scores, dim=0, descending=True)
        det_class_boxes = det_class_boxes[sort_ind]
        det_class_images = det_class_images[sort_ind]

        # culmulate tp & fp
        true_positives = torch.zeros((n_class_detections), dtype=torch.float).to(device)
        false_positives = torch.zeros((n_class_detections), dtype=torch.float).to(device)
        for d in range(n_class_detections):
            this_detection_box = det_class_boxes[d].unsqueeze(0)
            this_image = det_class_images[d]

            true_objects = true_class_boxes[true_class_images == this_image]
            object_difficulties = true_class_difficulties[true_class_images == this_image]

            if true_objects.size(0) == 0:
                false_positives = 1

            overlaps = find_jaccard_overlap(this_detection_box,true_objects)
            max_overlap, inx = torch.max(overlaps.squeeze(0),dim=0)

            # 这里不懂，为啥？
            org_index = torch.LongTensor(range(n_class_detections.size(0)))[true_class_images == this_image][ind]

            if max_overlap.item() > 0.5:
                if object_difficulties[inx] == 0:
                    if true_class_boxes_detected[org_index] == 0:
                        true_positives[d] = 1
                        true_class_boxes_detected[org_index] = 1
                    else:
                        false_positives[d] = 1
            else:
                false_positives[d] = 1

            # Compute cumulative precision and recall at each detection in the order of decreasing scores
            cumul_true_positives = torch.comsum(true_positives, dim=0)
            cumul_false_positives = torch.comsum(false_positives, dim=0)
            cumul_precision = cumul_true_positives / (cumul_true_positives + cumul_false_positives + 1e-10)
            cumul_recall = cumul_true_positives / n_easy_class_objects

            # Find the mean of the maximum of the precisions corresponding to recalls above the threshold 't'
            recall_threshholds = torch.arange(start=0, end=1.1, step=0.1).tolist()
            precisions = torch.zeros((len(recall_threshholds)), dtype=torch.float).to(device)
            for i,t in enumerate(recall_threshholds):
                recalls_above_t = cumul_recall >= t
                if recalls_above_t.any():
                    precisions[i] = cumul_precision[recalls_above_t].max()
                else:
                    precisions[i] = 0
            # 为什么减1
            average_precisions[c-1] = precisions.mean().item()

        mean_average_precision = average_precisions.mean().item()

        # 放进字典
        average_precisions = {rev_label_map[c+1]: v for c,v in enumerate(average_precisions.tolist())}

        return average_precisions, mean_average_precision


















