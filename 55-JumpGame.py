"""
You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length
at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
    ###
        max_jump_distance = 0 

        for idx in range(len(nums)):
            if idx > max_jump_distance:
                return False
            max_jump_distance = max(max_jump_distance, idx+nums[idx])
        
        return True
    ###