class Solution:
    def arrangeCoins(self, n: int) -> int:
        # initialize row = 0 
        row = 0 
        # while enough coins for the next row (n > 0)
        while n - row > 0:
            row += 1
        # increment row 
        # subtract row coins from n 
            n -= row
        return row #as number of complete rows 