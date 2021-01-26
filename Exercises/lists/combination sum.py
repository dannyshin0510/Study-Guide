# Combination Sum.
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    dp = [[] for _ in range(target + 1)]
    for c in candidates:  # O(N): for each candidate
        for i in range(c, target + 1):  # O(M): for each possible value <= target
            if i == c: dp[i].append([c])
            for comb in dp[i - c]: dp[i].append(comb + [c])  # O(M) worst: for each combination
    return dp[-1]

# Time Complexity: O(M*M*N), N = len(candidates), M = target
# Space Complexity: O(M*M)