class Solution(object):
    def uniquePathsIII(self, grid):
        def find(x,y,c):
            # total_path,co
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==-1 or sol[x][y]==1:
                return 
            if grid[x][y]==2:
                if c ==total_path[0]:
                    co[0]+=1
                return 
            sol[x][y]=1
            find(x+1,y,c+1)
            find(x,y+1,c+1)
            find(x-1,y,c+1)
            find(x,y-1,c+1)
            sol[x][y]=0
            return 
        sol=[[0]*(len(grid[0])) for i in range(len(grid))]
        total_path=[0]
        co=[0]
        xx=yy=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):   
                if grid[i][j]==1:
                    xx=i
                    yy=j
                if grid[i][j]!=-1:
                    total_path[0]+=1
        #return sol
        find(xx,yy,1)
        return co[0]
        

                    