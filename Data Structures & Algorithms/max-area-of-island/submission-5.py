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
        visit = set()
        ROW, COL = len(grid), len(grid[0])
        def dfs(r, c):
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))  
            return 1 + (
                        dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1)
                    )
        maxArea = 0
        for r in range(ROW):
            for c in range(COL):
                area = dfs(r, c)
                maxArea = max(area, maxArea)

        return maxArea
'''
[0,1,1,0,1]
[1,0,1,0,1]
[0,1,1,0,1]
[0,1,0,0,1]
'''
        