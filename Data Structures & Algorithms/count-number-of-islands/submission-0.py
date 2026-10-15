class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        initialize a dict that takes a node as key and returns which island it's in as value
        perform dfs starting at 0,0
        if current node is 1:
            check if it's in dict yet
                if so, check if prev was 1:
                    if so, set curr node island to prev node island
                    decrement island_counter
            elif prevnode was 1:
                if so, set curr node island to prev node island
            else:
                increment island_counter
                dict.add(currnode, island_counter)

    
        '''
        def dfs(grid, r, c):
            ROW, COL = len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] != "1":
                return
            grid[r][c] = "2"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        island_counter = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    island_counter += 1
                    grid[r][c] = "2"
                    dfs(grid, r + 1, c)
                    dfs(grid, r - 1, c)
                    dfs(grid, r, c + 1)
                    dfs(grid, r, c - 1)                    

        
            
        print(grid)
        return island_counter
        '''
        ["0","2","1","1","0"],
        ["0","2","0","1","0"],
        ["2","2","0","0","0"],
        ["0","0","0","0","0"]
        '''