import numpy as np

x=np.loadtxt('m_n_alpha.txt');
m=int(x[0]);
n=int(x[1]);
alpha=x[2];


p=[] 
f=[]
x='p{}.txt'
y='f{}.txt'
for i in range(m):
    p.append(np.loadtxt(x.format(i)))
    f.append(np.loadtxt(y.format(i)))


I=np.eye(n);
A=np.eye(n+1)
A[n][0]=1
A[n][n]=0
for i in range(n):
    A[i][n]=1    

w=f[0]
a=np.zeros(n, dtype=np.int64)
g=np.zeros(n+1)
v=np.zeros(n+1)
h=np.zeros(n)


for i in range(n):
              for j in range(m):
                  if f[j][i]<w[i]:
                        w[i]=f[j][i]
                        a[i]=j

delta=100; epsilon=0.5

while (delta>epsilon):

           print(a) 
     
           for i in range(n):
               g[i]=f[a[i]][i]
           g[n]=0
         
          
           
           q=np.zeros((n+1,n+1))
           for i in range(n):
               for j in range(n):
                   q[i][j]=p[a[i]][i][j]
           for i in range(n):
               q[i][n]=q[n][i]=0
        
           v=np.linalg.inv(A-q).dot(g)  
           print(v) 
          
           
           for i in range(n):
               h[i]=v[i]
           
           
           k=np.zeros((m,n))
           for i in range(m):
                k[i]=f[i]+p[i].dot(h)
           w=k[0]
           
          
           b=np.zeros(n, dtype=np.int64)
           for i in range(n):
                 for j in range(m):
                     if k[j][i]<w[i]:
                         w[i]=k[j][i]
                         b[i]=j
            
           delta=max(abs(a-b))
           a=b
           
          





    

