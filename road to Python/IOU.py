import torch

def cxcy2xy(cxcy): # (n, 4)
    '''
    torch.clamp 夹紧区间
    torch.clamp(input, min, max, out=None) → Tensor
    将输入input张量每个元素的夹紧到区间 [min,max]，并返回结果到一个新张量。
          | min, if x_i < min
    y_i = | x_i, if min <= x_i <= max
          | max, if x_i > max
    '''
    '''
    torch.cat 拼接可迭代张量
    torch.cat((A,B)) 和 torch.cat([A,B])都是合法的
    '''

    # 易错：用冒号表示行全选，用逗号分隔维度
    return torch.cat([torch.clamp(cxcy[:,:2]-cxcy[:,2:]/2, min=0), # x_min, y_min
                      cxcy[:,:2]+cxcy[:,2:]/2], 1) # x_max, y_max

def find_intersection(set1, set2):
    lower_bounds = torch.max(set1[:,:2].unsqueeze(1), set2[:,:2].unsequeeze(0)) # (n1, n2, 2)
    upper_bounds = torch.min(set1[:,2:].unsqueeze(1), set2[:,2:].unsequeeze(0)) # (n1, n2, 2)
    intersection_dims = torch.clamp(upper_bounds - lower_bounds, min=0)
    return intersection_dims[:,:,0] * intersection_dims[:,:,1] # (n1, n2)

def find_jaccard_overlap(set1, set2):
    set1Area = (set1[:,2] - set1[:,0]) * (set1[:,3] - set1[:,1]) # (n1,1) (n1)
    set2Area = (set2[:,2] - set2[:,0]) * (set2[:,3] - set2[:,1]) # (n2,1)
    intersection = find_intersection(set1, set2)
    union = set1Area.unsequeeze(1) + set2Area.unsequeeze(0) - intersection
    return intersection / union

if __name__ == "__main__":
   set1 = torch.rand(5,4) # 0-100怎么办
   set2 = torch.rand(9,4)
   set1xy = cxcy2xy(set1)
   set2xy = cxcy2xy(set2)
   res = find_jaccard_overlap(set1xy, set2xy)
   print(res)