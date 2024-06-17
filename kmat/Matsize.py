
def Matsize(Mat):
    row = 0
    col = 0
    for i in Mat:
        row += 1
    if row > 0:
        for i in Mat[0]:
            col += 1   
    return (row, col)