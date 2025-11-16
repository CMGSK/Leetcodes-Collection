""" 
Given an integer array nums, rotate the array to the right by k steps, where
k is non-negative.  
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
###
        def invert(start, end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        invert(0, len(nums)-1)
        invert(0, k-1)
        invert(k, len(nums)-1)
###