class Solution:
    def numIslands(self , grid:List[List[str]] ) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        islands = 0
        # Land fill Algorithm to find the no of Islands 
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] == "0" # we update all the visited nodes to 0
            directions = [[1,0] , [0,1] , [-1,0] , [0,-1]] # These are the only possible directions that we can go
            while q:
                row , col = q.popleft()
                for directionRow , directionCol in directions:
                    r , c = row + directionRow , col + directionCol
                    if r in range(nrows) and c in range(ncols) and grid[r][c] == "1":
                        q.append((r,c)) # append the current cell to the queue 
                        grid[r][c] = 0 # update the current cell to 0 as marked
                        
                
            
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    islands += 1 
                    bfs(r,c)

        return islands

# Time Complexity - O(M * N)
# Space Complexity - O(1) or O(M * N) considering the input and output space 
