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

v=np.zeros(n)
delta=100; epsilon=0.001;

while (delta>epsilon):
    q=np.zeros((m,n))
    for i in range(m):
          q[i]=f[i]+alpha*p[i].dot(v)
    w=q[0]
    
    for i in range(n):
        for j in range(m):
            if q[j][i]<w[i]:
                w[i]=q[j][i]
    delta=max(abs(v-w))
    v=w
    print(v)
    


for i in range(m):
    q[i]=f[i]+alpha*p[i].dot(v)
w=q[0]
a=np.zeros(n,dtype=np.int64)
for i in range(n):
     for j in range(m):
          if q[j][i]<w[i]:
              w[i]=q[j][i]
              a[i]=j
print(a)
    


