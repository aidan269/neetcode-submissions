class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # initialize res with the first element 
        n = len(nums)
        res = nums[0]
        # for each starting index i from 0 to n - 1
        for i in range(n):
            cur_sum = 0 
            for j in range(i, i + n):
                cur_sum += nums[j % n]
                res = max(res, cur_sum)
        return res