# Find K-Length Substrings With No Repeated Characters

# Input: S = "havefunonleetcode", K = 5
# Output: 6
# Explanation:
# There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if K>len(S):
            return 0
        answer = 0
        l = 0
        for r in range(K, len(S)+1):
            if len(S[l:r])==len(set(S[l:r])):      #THE KEY POINT: check if string has repeated letters
                answer +=1
            l+=1
            
        return answer