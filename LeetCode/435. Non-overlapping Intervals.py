#Time O(nlogn) 来源于排序
#Space O(1)

# 贪心，是动规的特殊情况
# 这里采用从末尾开始比较，参考leetcode题解画图（已点赞）
# 这里计算最大保留区间数，总数减去保留即为正确结果
# 易错一：如果区间数是0，要返回0

'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals,key=lambda x:x[1])

        reserve = 0
        # 易错二：初始边界错误
        # 第一个指针一定是放在负无穷（注意负无穷表示方法），不是第一个数组的末尾
        # 因为都是下一个数组的start和上一个数组的end比较，curr指向end
        # 在第一个数组的时候，自身的start一定是不大于end，造成无法保留
        curr = -float('inf')
        for interval in intervals:
            if interval[0] >= curr:
                reserve += 1
                curr = intervals[1]
        return len(intervals)- reserve

if __name__=="__main__":
    s = Solution()
    res = s.eraseOverlapIntervals([[1,2]])
    print(res)