""" Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You
may assume that the majority element always exists in the array. """

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
###
        # Boyer-Moore
        candidate = nums[0]
        count = 1
        for n in nums:
            if n == candidate:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                candidate = n
                count = 1

###
