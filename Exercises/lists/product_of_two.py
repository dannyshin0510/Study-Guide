# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).


# Thought: simple; need two largest vals in the list

# Two solutions:

#First: requiring traversal TWICE, due to 'max()' method used twice
def maxProduct(self, nums: List[int]) -> int:
    first = max(nums)
    nums.remove(first)
    second = max(nums)
    return (first - 1) * (second - 1)

#Second: requires traversing once, since we are using '.sort()'
def maxProduct(self, nums: List[int]) -> int:
    nums.sort()
    
    return (nums[len(nums) - 1] - 1) * (nums[len(nums) - 2] - 1)
