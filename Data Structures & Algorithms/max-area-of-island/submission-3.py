class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        loop through grid
            if curr node is 1:
                area = run dfs to find all other nodes in its island
                    for each node visited in dfs that's 1, mark it as seen
                    return 1 + dfs from all adjacent nodes
                maxArea= max(area,maxArea)
        '''
        def dfs(grid, r, c):
            ROW, COL = len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] != 1:
                return 0
            grid[r][c] = 2  
            return 1 + (
                        dfs(grid, r + 1, c) +
                        dfs(grid, r - 1, c) +
                        dfs(grid, r, c + 1) +
                        dfs(grid, r, c - 1)
                    )
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    area = 1 + (
                        dfs(grid, r + 1, c) +
                        dfs(grid, r - 1, c) +
                        dfs(grid, r, c + 1) +
                        dfs(grid, r, c - 1)
                    )
                    maxArea = max(area, maxArea)

        return maxArea
'''
[0,1,1,0,1]
[1,0,1,0,1]
[0,1,1,0,1]
[0,1,0,0,1]
'''
        