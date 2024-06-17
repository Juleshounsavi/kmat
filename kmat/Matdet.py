
def Matdet(Mat):
    if len(Mat) != len(Mat[0]):
        raise ValueError("The matrix must be square.")
    
    elif len(Mat) == 1:
        return Mat[0][0]
    
    elif len(Mat) == 2:
        return Mat[0][0] * Mat[1][1] - Mat[0][1] * Mat[1][0]
    
    else:
        det = 0
        for col in range(len(Mat)):
            sub_Mat = [row[:col] + row[col+1:] for row in Mat[1:]]
            det += ((-1) ** col) * Mat[0][col] * Matdet(sub_Mat)
        return det