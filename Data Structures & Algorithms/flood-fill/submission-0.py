class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, row, col, original_color, color, seen):
            ROW, COL = len(image), len(image[0])
            if min(row, col) < 0 or row == ROW or col == COL or (row,col) in seen:
                return
            seen.add((row,col))
            if image[row][col] == original_color:
                image[row][col] = color
                dfs(image, row + 1, col, original_color, color, seen)
                dfs(image, row - 1, col, original_color, color, seen)
                dfs(image, row, col + 1, original_color, color, seen)
                dfs(image, row, col - 1, original_color, color, seen)
        
        dfs(image, sr, sc, image[sr][sc], color, set())
        return image
        '''
        ROW: 3
        COL: 3
        original_color = 1
        Seen: (1,1)
        1 1 1
        1 1 0
        1 0 1
        '''