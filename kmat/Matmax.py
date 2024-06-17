
def Matmax(Mat, row, col):
    max = Mat[0][0]
    for i in range(row):
        for j in range(col):
            if Mat[i][j] >= max:
                max  = Mat[i][j]
    return max