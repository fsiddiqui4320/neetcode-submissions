class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        # array[m-1][n-1] = 0
        
        for row in range(m-1,-1,-1):
            currRow = [0] * n
            for col in range(n-1,-1,-1):
                if row == m-1 or col == n-1:
                    currRow[col] = 1
                else:
                    currRow[col] = prevRow[col] + currRow[col + 1]
            prevRow = currRow
                    
        return currRow[0]