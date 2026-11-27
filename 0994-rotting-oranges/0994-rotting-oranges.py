class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque 
        q=deque()
        r=len(grid)
        c=len(grid[0])
        fresh=0
        sol=[[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append([i,j])
                    sol[i][j]=1
                if grid[i][j]==1:
                    fresh+=1
        mini=0
        while q and fresh>0:
            for _ in range(len(q)):
                ro,co=q.popleft()
                di=[(0,1),(1,0),(-1,0),(0,-1)]
                for i , j in di:
                    nr,nc=ro+i,co+j
                    if 0<=nr<r and 0<=nc<c and sol[nr][nc]==0 and grid[nr][nc]==1:
                        fresh-=1
                        q.append([nr,nc])
                        sol[nr][nc]=1
            mini+=1
        return mini if fresh==0 else -1
        
        