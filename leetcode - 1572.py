def diagonalSum(mtrx):
    pri = [mtrx[i][j] for i in range(len(mtrx)) for j in range(i, len(mtrx)) if i == j]
    sec = [mtrx[i][j] for i in range(len(mtrx)) for j in range(len(mtrx)) if j == len(mtrx) - i - 1]
    
    center = mtrx[int(len(mtrx) / 2)][int(len(mtrx) / 2)] if len(mtrx) % 2 != 0 else 0
    
    diag_sum = sum(pri) + sum(sec) - center
    
    return diag_sum
    
matrix = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

print(diagonalSum(matrix))