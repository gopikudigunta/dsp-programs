import numpy as np                 #importing numpy and using it as np
a=input('Enter any array:')        #an array as input
b=input('Enter array to append:')  #an array to append
c=a
d=b
x=np.array(c)
y=np.array(d)
e=np.append(x,y)		   #appending using numpy
print(e)
for i in range(0,len(b)):	   #using for loop	
	a.append(b[i])		   #append function 
print('The appended array using for loop:',a)
