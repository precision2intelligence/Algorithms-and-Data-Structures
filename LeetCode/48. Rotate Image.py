#注意list的reverse用法
#理解题意，是先沿主对角线镜像，在竖直镜像

# Time:  O(n^2)
# Space: O(1)
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?
#
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                if i != j :
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()