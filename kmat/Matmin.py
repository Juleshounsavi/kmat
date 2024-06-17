
def Matmin(Mat, row, col):
    min = Mat[0][0]
    for i in range(row):
        for j in range(col):
            if Mat[i][j] <= min:
                min  = Mat[i][j]
    return min
