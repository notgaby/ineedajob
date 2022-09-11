#https://leetcode.com/problems/number-of-islands/

class Solution:
    def dfs(self, grid, x, y):

        if(x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])):
            return
        if(grid[x][y] == "0"):
            return
        
        grid[x][y] = "0"
        
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x, y - 1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num = 0
        
        for i in range (rows):
            for j in range (cols):
                if(grid[i][j] == "1"):
                    num += 1
                    self.dfs(grid, i, j)
        return num
        

        
                    
