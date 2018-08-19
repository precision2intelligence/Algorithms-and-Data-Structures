# Time:  O(n)
# Space: O(1)
# Method: 对撞指针，使用自定义函数维持程序框架

# Note:
# 边界条件，while下再额外记住i < j.
# 测试用例包括全奇数，全偶数，已排序，为空，为1，奇数偶数相间。
class Solution(object):
    def JustifyOdd(self,lists):
        if not list or len(lists) <= 1:
            return lists
        g = lambda x : x % 2
        i, j = 0, len(lists) - 1
        while i < j:
            flagi = g(lists[i])
            flagj = g(lists[j])
            while flagi and i < j:
                i += 1
                flagi = g(lists[i])
            while not flagj and i < j:
                j -= 1
                flagj = g(lists[j])
            lists[i], lists[j] = lists[j], lists[i]
            i += 1
            j -= 1
        return lists

if __name__ == "__main__":
    s = Solution()
    nums = [3,6,2,6,3,7,8,1]
    res1 = s.JustifyOdd(nums)
    print(res1)