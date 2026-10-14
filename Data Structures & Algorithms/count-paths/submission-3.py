class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array = [[0] * n] * m
        # array[m-1][n-1] = 0
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row == m-1 or col == n-1:
                    array[row][col] = 1
                else:
                    array[row][col] = array[row + 1][col] + array[row][col + 1]
                    
        print(array)
        return array[0][0]