from kmat.Matmin import Matmin
from kmat.Matmax import Matmax
from kmat.Matdet import Matdet
from kmat.Matsize import Matsize
from kmat.Matranspo import Matranspo

matrice = [[1,2,3],
           [4,5,6],
           [7,8,9]]

print(Matmin(matrice,3,3))
print("---------------------------------------------------------------------")

print(Matmax(matrice,3,3))
print("---------------------------------------------------------------------")

print(Matdet(matrice))
print("---------------------------------------------------------------------")

print(Matsize(matrice))
print("---------------------------------------------------------------------")

print(Matranspo(matrice,3,3))
