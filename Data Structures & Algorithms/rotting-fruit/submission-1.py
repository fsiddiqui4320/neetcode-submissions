class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        solve using bfs:
            return time to rot all fruit

        loop through all cells in the grid:
            if cell is rotten:
                run bfs from that fruit
            if cell is fresh:
                check if it's adjacent to any fruit
                    if not return -1
        '''
        ROW, COL = len(grid), len(grid[0])
        dimensions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        queue = deque()
        time = 0
        fresh = 0
        

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                fruit = grid[r][c]
                if fruit == 2:
                    queue.append((r,c))
                if fruit == 1:
                    fresh += 1
        
        while fresh > 0 and queue:
            level_size = len(queue)
            for i in range(level_size):
                r,c = queue.popleft()
                for dr,dc in dimensions:
                    nr, nc = r + dr, c + dc
                    if (min(nr,nc) >= 0 and not nr == ROW and not nc == COL 
                        and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1
                
        