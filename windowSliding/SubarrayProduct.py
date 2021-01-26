# Subarray Product Less Than K

# Your are given an array of positive integers nums.
#
# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.
#
# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        answer = 0
        l = 0
        temp = 1
        if k <= 1:
            return 0
        for r in range(len(nums)):
            temp *= nums[r]
            if temp >= k:
                temp /= nums[l]
                l += 1
            while temp >= k:
                temp /= nums[l]
                l += 1
            if temp < k:
                answer += (r - l + 1) #Tricky part: we are NOT counting number of elements
                                      # thisis the number of Subarray combinations

        return answer