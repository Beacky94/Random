# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:40:39 2018

@author: Becky
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:27:54 2018

@author: Becky
"""

import time
import numpy as np
import math

Hola = input("How many options does the consumer see?")
Hello = input("How Many consumers are there?")

t0=time.time()
Hola=int(Hola)
Hello=int(Hello)

empty=np.empty((Hello,Hola))


v = list(range(1,Hola+1))
rows = Hello
cols = 1
a = np.tile(v, (rows,cols))

b=np.vsplit(a,Hello)

for i in range(0,Hello):
    x=b[i]
    y=np.ndarray.flatten(x)
    np.random.shuffle(y)
    empty[i]=y

#print(empty)

#now we create conditions
option=list(range(1,Hola+1))
matrix1=np.ones((Hello,Hola))
matrix2=np.zeros((Hello,math.factorial(Hola)))


for j in range(0,Hello):
    cond=empty[j]
    conds=np.ndarray.flatten(cond)
    condss=list(conds)
    #print(condss)
    for k in range(1, Hola+1):
        indexx=condss.index(k)
        matrix1[j,k-1]=indexx

#print(matrix1)



for l in range(0, Hello):  
     r=0
     for m in range(0, Hola):
         for n in range(0,Hola):
             if n==m:
                 continue 
             elif float(matrix1[l,m]) < float(matrix1[l,n]):
                 matrix2[l,r]=matrix2[l,r]+1
                 r=r+1
             elif float(matrix1[l,m]) > float(matrix1[l,n]):
                 matrix2[l,r]=matrix2[l,r]+0
                 r=r+1
#print(matrix2)  
                     
final=np.zeros((Hola,Hola))     

matrix2=np.asarray(matrix2)


#print(sum(matrix2[:,0]))   
#print(sum(matrix2[:,1]))  
#print(sum(matrix2[:,2]))  
#print(sum(matrix2[:,3]))  
#print(sum(matrix2[:,4]))   
#print(sum(matrix2[:,5]))  

alpha=0
for o in range (0,Hola):
    for p in range(0,Hola):
        if o==p:
            final[o,p]=0
        else:
            final[p,o]=sum(matrix2[:,alpha])
            alpha=alpha+1

#print(final)
beta=0
for a in range(0,Hola):
    for b in range(0,Hola):
        if final[a,b]==final[b,a]:
            continue
        else:
            beta=beta+1
if beta == 0:
    print(empty)
    print(final)
else: 
    gamma=0
    while(gamma<Hello*1000000):
                final=np.zeros((Hola,Hola))
                matrix1=np.ones((Hello,Hola))
                matrix2=np.zeros((Hello,math.factorial(Hola)))
                b=np.vsplit(empty,Hello)
                empty=empty
                for i in range(0,Hello):
                    x=b[i]
                    y=np.ndarray.flatten(x)
                    np.random.shuffle(y)
                    empty[i]=y


                for j in range(0,Hello):
                    cond=empty[j]
                    conds=np.ndarray.flatten(cond)
                    condss=list(conds)
                    #print(condss)
                    for k in range(1, Hola+1):
                        indexx=condss.index(k)
                        matrix1[j,k-1]=indexx

                for l in range(0, Hello):  
                    r=0
                    for m in range(0, Hola):
                        for n in range(0,Hola):
                            if n==m:
                                continue 
                            elif float(matrix1[l,m]) < float(matrix1[l,n]):
                                matrix2[l,r]=matrix2[l,r]+1
                                r=r+1
                            elif float(matrix1[l,m]) > float(matrix1[l,n]):
                                matrix2[l,r]=matrix2[l,r]+0
                                r=r+1
                alpha=0
                for o in range (0,Hola):
                    for p in range(0,Hola):
                        if o==p:
                            final[o,p]=0
                        else:
                            final[p,o]=sum(matrix2[:,alpha])
                            alpha=alpha+1
                beta=0
                for a in range(0,Hola):
                    for b in range(0,Hola):
                        if final[a,b]==final[b,a]:
                            continue
                        else:
                            beta=beta+1
                if beta == 0:
                    break
                else:
                    gamma=gamma+1
t1=time.time()
print(t1-t0)
print(empty)
print(final)
print(gamma)



