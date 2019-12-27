import numpy as np
m=3; n=5; alpha=0.95;
I=np.eye(n);

p=[] 
f=[]
x='p{}.txt'
y='f{}.txt'
for i in range(m):
    p.append(np.loadtxt(x.format(i)))
    f.append(np.loadtxt(y.format(i)))

w=f[0]
a=np.zeros(n, dtype=np.int64)
g=np.zeros(n)

for i in range(n):
              for j in range(m):
                  if f[j][i]<w[i]:
                        w[i]=f[j][i]
                        a[i]=j

delta=100; epsilon=0.1

while (delta>epsilon):

           print(a) 
     
           for i in range(n):
               g[i]=f[a[i]][i]
          
          
           
           q=np.zeros((n,n))
           for i in range(n):
               q[i]=p[a[i]][i]
           
    

           v=np.linalg.inv(I-alpha*q).dot(g)
           print(v)

           k=np.zeros((m,n))
           for i in range(m):
                k[i]=f[i]+alpha*p[i].dot(v)
           w=k[0]
          
           
           b=np.zeros(n, dtype=np.int64)
           for i in range(n):
                 for j in range(m):
                     if k[j][i]<w[i]:
                         w[i]=k[j][i]
                         b[i]=j
            
           delta=max(abs(a-b))
           
           a=b
            





    


