class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        unique_nums = set(nums)
        if len(unique_nums) != len(nums):
            return False 
        
        return max(nums) - min(nums) == len(nums) - 1



