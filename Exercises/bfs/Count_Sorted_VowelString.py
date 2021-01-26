# Count Sorted Vowel Strings

# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.



# Sol1: very inefficient

# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         if not n: return 0
        
#         v = ['a', 'e', 'i', 'o', 'u']
#         res = []
        
#         def bfs(arr, path, ret):
#             if path == n: ret.append(0)
#             if path > n: return
#             for i in range(len(arr)):
#                 bfs(arr[i:], path + 1, ret)
                
#         bfs(v, 0, res)
#         return len(res)


# With Dynamic Programming isntead of BFS: much faster

# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         dp = [[i for i in range(5,0,-1)] for _ in range(n)]   # intialize dp matrix
        
#         for i in range(1,n):
#             for j in range(3,-1,-1):
#                 dp[i][j] = dp[i - 1][j] + dp[i][j + 1]   # dp expression
                
#         return dp[n-1][0]