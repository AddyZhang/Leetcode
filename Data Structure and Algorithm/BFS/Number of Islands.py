from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        numIslands = 0
        que = deque()
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # print('AA') 
                    numIslands += 1
                    grid[i][j] = '*'
                    que.append([i,j])
                    self.bfs(grid, que)
        return numIslands
    
    def bfs(self,grid,que):
        dircs = [[0,1],[0,-1],[1,0],[-1,0]]
        while que:
            cur = que.popleft()
            for dirc in dircs:
                x = cur[0] + dirc[0]
                y = cur[1] + dirc[1]
                if (x<0 or x >=len(grid) or y < 0 or y>= len(grid[0]) or grid[x][y] != '1' ):
                    continue
                grid[x][y] = '*'
                que.append([x,y])
            
