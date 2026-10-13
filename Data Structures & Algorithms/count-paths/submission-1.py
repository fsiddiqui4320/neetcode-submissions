class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(x, y, cache):
            if x >= m or y >= n:
                return 0
            if x == m-1 and y == n-1:
                return 1
            if (x,y) in cache:
                return cache[(x,y)]
            cache[(x,y)] = dfs(x+1,y,cache) + dfs(x,y+1,cache)
            return cache[(x,y)]
        
        return dfs(0,0,{})