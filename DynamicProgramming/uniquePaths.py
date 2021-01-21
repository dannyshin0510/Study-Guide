# Unique Paths

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# dynamic programming solution without any memoization:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def recurse(m, n):
            if m==1 and n==1:
                return 1
            if m < 1:
                return 0
            if n  < 1:
                return 0
            
            return recurse(m-1,n)+recurse(m,n-1)
        return recurse(m,n)


# Not dynamic, but realizing all you need to do is to add the square above and left to current.
#O(m*n) speed. Much faster

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.stage = [[1] * n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                self.stage[i][j]=self.stage[i-1][j]+self.stage[i][j-1]

        return self.stage[m-1][n-1]