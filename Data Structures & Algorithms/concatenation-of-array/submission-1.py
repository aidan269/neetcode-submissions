class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
    # Initialize an empty result list or an array ans of size 2n, where n is the length of the input array.
        ans = []
    # Use a loop that runs twice.
        for i in range(2):
    # Inside that loop, iterate through every element num in the input array nums.
            for num in nums:
    # Append num to the result list or assign it to the next available index in the result array.
                ans.append(num)
        return ans 