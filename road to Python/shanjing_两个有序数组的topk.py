def fun(nums1,nums2,k):
    # if (len(nums2) + len(nums1)) < k:  #防患于未然
    #     return 'error,k大于两个list总个数'

    #必须优先检查list是否为空,不然会越界...
    #如果nums2为空,那么第k个元素,肯定是nums[k - 1]了啊(k - 1为序列第k个元素,是因为list从0开始...)
    # if len(nums2) == 0:
    #     return nums1[k - 1]

    #为了防止越界,保证nums1长度大于nums2
    if len(nums2) > len(nums1):
        return fun(nums2,nums1,k)

    #取第一个元素,肯定是要比两个list的首个元素中比较小的那个
    if k == 1:
        return min(nums1[0],nums2[0])

    #防不胜防啊...因为nums2比nums1短,取k/2有可能越界...,检查了n久没查出来...
    #如果nums2个数不足k/2，所以只能取比k/2小,又不越界的最大值了,即len(nums2),只要保证p + q = k就好啦...
    q = min(k // 2, len(nums2))
    p = k - q
    if nums1[p - 1] < nums2[q - 1]:
        return fun(nums1[p:],nums2,k - p)
    elif nums1[p - 1] > nums2[q - 1]:
        return fun(nums1,nums2[q:],k - q)
    else:
        return nums1[p - 1]


nums1 = [1,5,8,9]
nums2 = [2,3,6,7,10,12,14]
print(fun(nums1, nums2,8))