'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import numpy as np
n=int(input())
val=0
while(n!=0):
    val+=1
    sol=[]
    N,P=map(int,input().split(' '))
    exmpl=list(map(int,input().split(' ')))
    exmpl.sort()
    prefixarr=np.zeros((N+1,1))
    for i in range(N):
        prefixarr[i+1]=prefixarr[i]+exmpl[i]
    for i in range(P-1,N):
            sums1=exmpl[i]*(P-1)-(prefixarr[i]-prefixarr[i-P+1])
            sol.append(sums1)
    print("Case #"+str(val)+": "+str(int(min(sol))))
    n-=1
