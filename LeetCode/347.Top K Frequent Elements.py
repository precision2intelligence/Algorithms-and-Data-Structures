# 解法一：优先队列（最小堆）
# Time:  O(nlogk)
'''
其中 n 表示数组的长度。
首先，遍历一遍数组统计元素的频率，这一系列操作的时间复杂度是 O(n) 的；
接着，遍历用于存储元素频率的 map，如果元素的频率大于最小堆中顶部的元素，则将顶部的元素删除并将该元素加入堆中，这一系列操作的时间复杂度是 O(nlogk) 的；
最后，弹出堆中的元素所需的时间复杂度是 O(klogk) 的。备注：堆上浮下沉是logk复杂度
因此，总的时间复杂度是 O(nlogk) 的。
'''
# Space: O(n)
'''
最坏情况下（每个元素都不同），map 需要存储 n 个键值对，优先队列需要存储 k 个元素.
因此，空间复杂度是 O(n) 的
'''

'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''

import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 统计元素出现的频率
        freq_dic = dict()
        for num in nums:
            freq_dic[num] = freq_dic.get(num,0) + 1

        # 维护一个大小为k的最小堆
        # 堆是完全二叉树，也是优先队列。入队和出队（上浮和下沉）时间复杂度是logn
        priorityQueue = list()
        for key,value in freq_dic.items():
            if len(priorityQueue) < k:
                heapq.heappush(priorityQueue,(value,key))
                # 优先队列就是数组
                # print(priorityQueue)
                # [(2, 2), (3, 1)]
            # 题目中说，频率是unique的，不存在两个数字频率相同，否则这样处理不了频率相同的，会返回先出现的同频率数字
            elif value > priorityQueue[0][0]:
                heapq.heapreplace(priorityQueue, (value,key))

        # 获得最后的结果
        res = list()
        # 如果直接打印，会是频率先小后大
        # for (value,key) in priorityQueue:
        #     res.append(key)

        # 直接pop也是逆序，堆顶先出队，同上一种情况
        while priorityQueue:
            res.append(heapq.heappop(priorityQueue)[1])
        # 如果强迫从大到小排序，res[::-1]
        return res

# 解法二：桶排序
# Time:  O(n)
'''
首先，遍历一遍数组统计元素的频率，这一系列操作的时间复杂度是 O(n)；
桶的数量为 n + 1，所以桶排序的时间复杂度为 O(n)；
因此，总的时间复杂度是 O(n)。
'''
# Space: O(n)
'''
n+1个桶，存n个数，2n，舍弃系数
'''
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 统计元素出现的频率
        freq_dic = dict()
        for num in nums:
            freq_dic[num] = freq_dic.get(num, 0) + 1

        # 桶排序
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in freq_dic.items():
            bucket[value].append(key)

        # 逆序取出前k个元素
        # 这里没有对桶中的键进行排序，因为最快的时间复杂度是O(nlogn)，所以遍历最快，是O(n)
        # 经验：能遍历，不排序
        res = list()
        # 很精妙，因为一个数字最多出现的次数等于数组长度
        for i in range(len(nums), -1, -1):
            if len(res) < k:
                if bucket[i]:
                    res.extend(bucket[i])
            else:
                return res