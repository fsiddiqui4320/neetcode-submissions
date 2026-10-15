class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] ==  1 or grid[ROWS-1][COLS-1] ==  1:
            return -1
        seen = set()
        queue = deque()
        queue.append((0,0))
        seen.add((0,0))
        length = 1
        # if ROWS == 1 and COLS == 1 and grid[0][0] ==  0:
        #     return 1
        directions = [[0,1], [1,0], [0,-1], [-1,0], 
                        [1,1], [1,-1], [-1,1], [-1,-1]]
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1 and grid[r][c] ==  0:
                    return length
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in seen or grid[nr][nc] == 1:
                        continue
                    queue.append((nr, nc))
                    seen.add((nr, nc))
            length += 1

        return -1
