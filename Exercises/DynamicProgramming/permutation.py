# Permutations
# Given an array nums of distinct integers,
# return all the possible permutations. You can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        answer = []

        def recur(temp, numbers):

            if len(numbers) == 0:
                answer.append(temp)
                return

            for i in range(len(numbers)):
                recur(temp + [numbers[i]], numbers[:i] + numbers[i + 1:])

        recur([], nums)
        return answer