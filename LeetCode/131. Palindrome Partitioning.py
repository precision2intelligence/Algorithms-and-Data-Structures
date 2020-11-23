class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = list()
        dpCenter = [[False for _ in range(len(s))] for _ in range(len(s))]
        length = len(s)
        for i in range(length):
            self.centerSpread(s, dpCenter, length, i, i)
            self.centerSpread(s, dpCenter, length, i, i+1)
        self.backtrack(res, "", 0, s, dpCenter)
        return res
    def centerSpread(self, s, dpCenter, length, l, r):
        while l >= 0 and r < length and s[l] == s[r]:
            dpCenter[l][r] = True
            l -= 1
            r += 1
    def backtrack(self, res, path, begin, s, residue, dpCenter):
        if len(residue) == 0:
            res.append(path)
        for i in range(begin, len(residue)):
            if not dpCenter[begin][i]:
                return

            self.backtrack(res, path + s[i], i+1, s[i+1:], dpCenter)
            res.append(tmpPath)
