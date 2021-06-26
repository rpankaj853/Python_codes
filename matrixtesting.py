import numpy as np
t=[]
R = int(input())
for i in range(0,R*R):
    t.append(input())  
    
n= np.asarray(t)
r = n.reshape(R,R)
q = np.matrix(r)
p = np.rot90(q,k=1,axes=(0,1))
print(p)




 
