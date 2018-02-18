import os, re, sys

class Matrix:

    def __init__(self, mat):
        #aici presupunem ca cine ne da matricea e intr-o forma ok;
        # mai tarziu vom face o verificare ca are cate elemente trebuie
        self.mat = mat


    def mprint(self):
        #print "-----"
        for i in range(0, len(self.mat)):
            print '[',
            for j in range(0, len(self.mat[0])):
                print "%.2f" % self.mat[i][j],
            print ']'  
            #print
        print "-----"


    def __eq__(self, other):

        if self.mat == other.mat:
            return True
        else:
            return False


    def __add__(self, other):

        rows_self = len(self.mat)
        cols_self = len(self.mat[0])
        rows_other = len(other.mat)
        cols_other = len(other.mat[0])

        if cols_self != cols_other or rows_self != rows_other:
         print "Cannot add the two matrices. Incorrect dimensions."
         return

        C = [[self.mat[row][col]+other.mat[row][col] for row in range(cols_other)] for col in range(rows_self)]

        '''
        for i in range(rows_self):
            for j in range(cols_self):
                C[i][j] = self.mat[i][j] + other.mat[i][j]
        '''

        return Matrix(C)


    def __mul__(self, other):

        rows_self = len(self.mat)
        cols_self = len(self.mat[0])
        rows_other = len(other.mat)
        cols_other = len(other.mat[0])

        if cols_self != rows_other:
         print "Cannot multiply the two matrices. Incorrect dimensions."
         return

        C = [[0 for row in range(cols_other)] for col in range(rows_self)]


        for i in range(rows_self):
            for j in range(cols_other):
                for k in range(cols_self):
                    C[i][j] += self.mat[i][k] * other.mat[k][j]

        return Matrix(C)


    def mult2(self, num):

        rows_self = len(self.mat)
        cols_self = len(self.mat[0])

        C = [[self.mat[row][col]*num  for row in range(rows_self)] for col in range(cols_self)]

        '''
        for i in range(rows_self):
            for j in range(cols_self):
                C[i][j] = self.mat[i][j] * num
        '''

        return Matrix(C)


    def transp(self):

        rows_self = len(self.mat)
        cols_self = len(self.mat[0])


        C = [[self.mat[row][col] for row in range(cols_self)] for col in range(rows_self)]

        '''
        C = [[0 for row in range(cols_self)] for col in range(rows_self)]


        for i in range(rows_self):
            for j in range(cols_self):
                C[i][j] = self.mat[j][i]
        '''


        return Matrix(C)


    def simet(self):
        return len(self.mat) == len(self.mat[0]) and self==self.transp()


    '''
        rows_self = len(self.mat)
        cols_self = len(self.mat[0])

        if rows_self == cols_self and self.equal(self.transp()) is True:
            return True

        else:
            return False
    '''
    def det(self):
        n=len(self.mat)
        if (n>2):
            i=1
            t=0
            sum=0
            while t<=n-1:
                d={}
                t1=1
                while t1<=n-1:
                    m=0
                    d[t1]=[]
                    while m<=n-1:
                        if (m==t):
                            u=0
                        else:
                            d[t1].append(self.mat[t1][m])
                        m+=1
                    t1+=1
                l1=[d[x] for x in d]
                sum=sum+i*(self.mat[0][t])*Matrix(l1).det()
                #sum=sum+i*(l[0][t])*(det(l1))
                i=i*(-1)
                t+=1
            return sum
        else:
            return (self.mat[0][0]*self.mat[1][1]-self.mat[0][1]*self.mat[1][0])

    def inver(self):

        rows_self = len(self.mat)
        cols_self = len(self.mat[0])
        
        if rows_self != cols_self:
         print "Matrix is not square."
         return
        

        if rows_self > 2:

            C = [[0 for row in range(rows_self)] for col in range(cols_self)]
    
    
            for i in range(rows_self):
                for j in range(cols_self):
                    T = [[self.mat[row][col] for row in range(rows_self) if row!=i] for col in range(cols_self) if col !=j]
                    C[i][j] = Matrix(T).det() *1.0/self.det()
                    if (i + j) % 2 != 0: C[i][j] = -C[i][j] 
                    
            
            
            
            return Matrix(C).transp()
            
        
            
            
        else:
            
            C = [[0 for row in range(rows_self)] for col in range(cols_self)]
            
            a = self.mat[0][0]
            b = self.mat[0][1]
            c = self.mat[1][0]
            d = self.mat[1][1]
            
            det2 = Matrix(self.mat).det()    
            C[0][0] = 1.0*d/det2
            C[0][1] = 1.0*b*(-1)/det2
            C[1][0] = 1.0*c*(-1)/det2
            C[1][1] = 1.0*a/det2
                        
            return Matrix(C)


mat1 = Matrix([[1.0,2.0],[3.0,4.0]])
mat2 = Matrix([[2.0,3.0],[1.0,4.0]])
mat3 = mat1 + mat2
mat4 = mat1 * mat2
mat5 = mat4.mult2(5)
mat6 = Matrix([[3,0,2],[2,0,-2],[0,1,1]])
mat7 = Matrix([[1,0,0,0,0],[0,5,0,0,0],[0,0,6,0,0],[0,0,0,8,0],[0,0,0,0,9]])
mat8 = mat6 * mat6.inver()


mat6.mprint()
print mat6.det()
mat6.inver().mprint()

mat8.mprint()