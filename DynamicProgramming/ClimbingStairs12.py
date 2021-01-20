# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


#Utilizing Dynamic Programming and Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        self.bank = {}
        def recur(n):
            if n in self.bank:
                return self.bank[n]
            if n < 4:
                return n
            self.bank[n] = recur(n-1) + recur(n-2)
            return self.bank[n]
        return recur(n)