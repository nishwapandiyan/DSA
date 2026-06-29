class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        total = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] != -1:
                    total += 1

                if grid[i][j] == 1:
                    sr,sc = i,j
        ans = 0            
        def dfs(r,c,count):
            nonlocal ans
            
            if r<0 or c<0 or r>=row or c >= col or grid[r][c] == -1:
                return

            if grid[r][c] == 2:
                if count == total:
                    ans += 1
                return
            temp = grid[r][c]
            grid[r][c] = -1

            dfs(r+1,c,count+1)            
            dfs(r-1,c,count+1)            
            dfs(r,c+1,count+1)            
            dfs(r,c-1,count+1)  

            grid[r][c] = temp          

        dfs(sr,sc,1)    
        return ans
