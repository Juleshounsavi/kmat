
def Matranspo(Mat, row, col):
    B = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            B[j][i] = Mat[i][j]
    return B
