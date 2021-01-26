# Minimum Swaps to Group All 1's Together

# Input: data = [1,0,1,0,1]
# Output: 1
# Explanation:
# There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.

class Solution:
    def minSwaps(self, data: List[int]) -> int:

        length = data.count(1) #length of 1s are already set
        count = data[:length].count(0) #first window
        answer = count
        if length <= 1:
            return 0
        for r in range(length, len(data)):

            if data[r] == 0:
                count += 1

            if data[r - length] == 0:
                count -= 1

            answer = min(count, answer)

        return answer