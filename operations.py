import numpy as np
a=np.array(input('Enter any array:'))
b=np.array(input('Enter another array:'))
c=np.linalg.det(a)  #Det of matrix a
print('Det of a matrix a',c)
d=np.linalg.matrix_rank(a)#Rank of matrix a
print('Rank of a matrix a',d)
e=np.trace(a)#Trace of matrix a
print('Trace of a matrix a',e)
f=np.linalg.inv(a)#Inverse of matrix a
print('Inverse of a matrix a',f)
g=np.linalg.eigvals(a)#Eigen values of matrix a
print('Eigen values of a matrix a',g)
h=np.linalg.matrix_power(a,4) #Matrix power to 4
print('Matrix Power of a matrix a',h)
j=np.add(a,b) #addition of  two matrices
print('Addition of two matrices',j)
i=np.subtract(a,b) #subtraction of two  matrices
print('Subtraction of two matrices',i)
k=np.multiply(a,b)
print('Element by element multiplication of two matrices',k)
l=np.dot(a,b)
print('Multiplication of two matrices',l)
m=np.divide(a,b) #subtraction of matrices
print('Element by element division of two matrices',m)
n=np.linalg.solve(a,b) # solution of linear equations
print('Solution of linear equations',n)
o=np.linalg.qr(a) #Decomposition
print('qr decomposition of matrix',o)


