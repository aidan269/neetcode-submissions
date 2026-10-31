class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            cur = 0 
            if num in seen:
                return True 
            seen.add(num)
        return False