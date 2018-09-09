# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# 先排序，这样控制住了左边的索引大于右边。

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)<=1:
            return intervals
        res = []
        intervals = sorted(intervals, key=lambda intervals:intervals.start)
        m = len(intervals)
        i = 0
        while i < m:
            start_id = intervals[i].start
            end_id = intervals[i].end
            while i < m and intervals[i].start <= end_id:
                end_id = max(end_id,intervals[i].end)
                i += 1
            res.append([start_id,end_id])
        return res
