import os, re, sys

class Matrix:

    def __init__(self, mat):
        #aici presupunem ca cine ne da matricea e intr-o forma ok;
        # mai tarziu vom face o verificare ca are cate elemente trebuie
        self.mat = mat


    def mprint(self):
        print "-----"
        for i in range(0, 2):
            print self.mat[i]
        print "-----"

    def multiply(self, other):
        rez =Matrix([[],[]])
        mat[0][0] = a1
        mat[0][1] = a2
        mat[1][0] = b1
        mat[1][1] = b2
        print self.a1 * other.a1 + self.a2 + other.a2
        
        return rez

mat1 = Matrix([[1,2],[3,4]])
mat2 = Matrix([[2,2],[3,3]])
mat3 = mat1.multiply(mat2)
mat1.mprint()
mat2.mprint()
mat3.mprint()

'''
# incearca in pycharm 
x=[[1,2],[3,4]]
apoi x[0]
x[1]
x[0][1]
joaca-te
'''