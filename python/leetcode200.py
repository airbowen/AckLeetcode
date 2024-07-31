class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])) or (grid[i][j] == '0'):
                return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
        #只要发现一个1，就调用dfs 把所有相邻的1 全部清理
                    dfs(grid, i, j)
                    count += 1
        return count
