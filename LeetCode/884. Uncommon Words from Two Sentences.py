#熟练使用字典
'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words.
You may return the list in any order.

Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]
'''
class Solution(object):
    #解法一：最简单，把A,B放进一个字典，分别添加两次而已
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = {}
        for word in A.split():
            count[word] = count.get(word,0) + 1 #亮点：一行搞定给字典添加元素
        for word in B.split():
            count[word] = count.get(word,0) + 1
        return [word for word in count if count[word] == 1]

    #同解法一，只是用了字典的加法，和整数一样迭代，用‘+=’
    def uncommonFromSentences1(self, A, B):
        import collections
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())
        return [word for word in count if count[word] == 1]

    #解法三：
    #先形成A,B各自的字典，这里是collection类型的，但是使用的类型和字典是一样的
    #collection.Count中的keys（）是集合型的，可以做集合间运算
    #用到filter的地方，不如试试列表生成式
    #字典用lambda，应该对item()操作
    def uncommonFromSentences2(self, A, B):
        import collections
        countA = collections.Counter(A.split())  # type: <class 'collections.Counter'>
        countB = collections.Counter(B.split())
        res = (countA.keys() | countB.keys()) - (countA.keys() & countB.keys()) # type:<class 'dict_keys'>
        ans = [word for word in res if countA[word] == 1 or countB[word] == 1]
        return ans
