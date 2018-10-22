#Time: O(n)
#BD考过

#方法一：
#观察，保存最大，类似买卖股票
#易错点1：if 和 else在一行时，等于号后面的会被完全替换。写成pre += array[i] if pre >= 0 else array[i] 则pre会一直加array[i]
#易错点2：是否更新最大值取决于当前的pre是否比maximum大了，不是array[i]的正负，很直接的想法
class Solution:
    def FindGreatestSumOfSubArray1(self, array):
        #write code here
        if not array:
            return
        maximum, pre = array[0], array[0]
        l = len(array)
        for i in range(1,l):
            pre = pre + array[i] if pre >= 0 else array[i]
            maximum = pre if pre > maximum else maximum
        return maximum
#方法二：
#动规：dp[i]是以i结尾的最大和
#注意，max函数本身也是O(n)的，因为可以一趟遍历得结果
    def FindGreatestSumOfSubArray2(self, array):
        dp = [0 for _ in range(len(array))]
        dp[0] = array[0]
        for i in range(1, len(array)):
            dp[i] = dp[i - 1] + array[i] if dp[i - 1] >= 0 else array[i]
        return max(dp)
