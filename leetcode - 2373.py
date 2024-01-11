def largestLocal(grid):
    size = len(grid)
    mtrx = []
    
    for i in range(1, size - 1):
        temp = []
        for j in range(1, size - 1):
            window = [
                grid[i-1][j-1:j+2],
                grid[i][j-1:j+2],
                grid[i+1][j-1:j+2],
            ]
            
            val = max(max(row) for row in window)
            
            temp.append(val)
            
        mtrx.append(temp)
        
    return mtrx

grid = [[8,1,9,9],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

print(largestLocal(grid))