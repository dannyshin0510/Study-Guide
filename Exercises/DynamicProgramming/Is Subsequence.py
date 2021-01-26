# Is Subsequence

# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Dynamic programming made!
# on each recursion, check in the letters after last confirmed
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def recur(index, letterindex):
            print (letterindex)
            if letterindex == len(s):
                print('true immediated')
                return True
            for i in range(index, len(t)):
                if t[i] == s[letterindex]:
                    return recur(i+1, letterindex+1)
            return False
        return recur(0,0)