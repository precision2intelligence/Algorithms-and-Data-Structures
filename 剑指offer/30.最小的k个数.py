import heapq

def GetLeastNumbers_QuickSort_partion(lists, left, right):
    # 划分函数处理部分
    key = lists[left]
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[left] = key
    return left


class Solution(object):
    def GetLeastNumbers_Heap(self, tinput, k):
        # Time:  O(n * logk)
        # Space: O(k)
        # Method: 维护一个大小为k的最大堆

        # Note:
        # 默认是最小堆，这里用了trick，取相反数。

        if len(tinput) < k:
            return []
        res = []
        for i in tinput:
            heapq.heappush(res, -i) if len(res) < k else heapq.heappushpop(res, -i)
        return sorted(list(map(lambda x: -x, res)))

    def GetLeastNumbers_SimpleHeap(self,nums,k):
        # Time:  O(n * logk)
        # Space: O(k)
        # Method: 直接利用堆的函数求最小

        # Note:
        # heap.nlargest(k,iter)是求最大的几个数。
        res = heapq.nsmallest(k,nums)
        return res

    def GetLeastNumbers_QuickSort(self,lists, k):
        # Time:  O(n)
        # Space: O(1)
        # Method: 分区快排，比较索引

        # Note:
        # 最快的方法了，只要内存允许。
        # 比较索引，控制边界。
        # 划分部分在类的外面。
        # 主要函数部分
        length = len(lists)
        left = 0
        right = length - 1
        index = GetLeastNumbers_QuickSort_partion(lists, left, right)
        while k != index:
            if index > k - 1:
                right = index - 1
            else:
                left = index + 1
            index = GetLeastNumbers_QuickSort_partion(lists, left, right)
        return lists[0:k]

    def GetLeastNumbers_Bubble(self,lists,k):
        # Time:  O(n * k)
        # Space: O(1)
        # Method: 冒泡，只冒4次

        # Note:
        # 时间、空间复杂度
        length = len(lists)
        for i in range(k):
            for j in range(i + 1, length):
                if lists[i] > lists[j]:
                    lists[j], lists[i] = lists[i], lists[j]
        return lists[0:k]


if __name__ == "__main__":
    s = Solution()
    nums = [11,1,6,4,11,9,2,10,3]
    res1 = s.GetLeastNumbers_Heap(nums,7)
    res2 = s.GetLeastNumbers_SimpleHeap(nums,4)
    res3 = s.GetLeastNumbers_QuickSort(nums,7)
    res4 = s.GetLeastNumbers_Bubble(nums, 7)
    print(res1,res2,res3,res4)