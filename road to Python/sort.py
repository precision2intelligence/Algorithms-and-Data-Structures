'''
快排
O(Time) : 最好和平均nlogn，最差类比冒泡，n^2
O(Space): logn
'''
## 快排极简写法
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(greater)

## 常规写法
def qsort_rec(array, left, right):
    ## 注意退出条件
    if left >= right:
        return
    i, j = left, right
    mark = array[i]
    while i < j:
        while i < j and array[j] >= mark:
            j -= 1
        array[i] = array[j]
        while i < j and array[i] < mark:
            i += 1
        array[j] = array[i]

    array[i] = mark
    qsort_rec(array, left, i - 1)
    qsort_rec(array, i + 1, right)
    return array

'''
归并
O(Time): 全部nlogn
O(Space): n
'''
def mergeSort(arr):
    if not arr or len(arr) == 1:
        return arr
    mid = len(arr) >> 1
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
def merge(arr1, arr2):
    i,j = 0,0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res



alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
b = qsort_rec(alist,0,len(alist)-1)
c = mergeSort(alist)
print(b,c)