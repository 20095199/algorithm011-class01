class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid)==0:
            return 0

        b=len(grid[0])
        for i in grid:
            i.append('0')
            i=i.insert(0,'0')
        grid.append(['0']*(b+2))
        grid.insert(0,['0']*(b+2))

        num1=0

        def sousuo(i,j,b):
            if grid[i][j]=='1':
                grid[i][j]=b
                if grid[i-1][j]=='1':sousuo(i-1,j,b)
                if grid[i+1][j]=='1':sousuo(i+1,j,b)
                if grid[i][j-1]=='1':sousuo(i,j-1,b)
                if grid[i][j+1]=='1':sousuo(i,j+1,b)
        
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j]=='1':
                    num1+=1
                    sousuo(i,j,num1)
        
        return num1
