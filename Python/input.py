import numpy as np


class Algorithms:
    def __init__(self, delta=100, epsilon=0.0001):
        x = np.loadtxt('m_n_alpha.txt')
        m = int(x[0])
        n = int(x[1])
        alpha = x[2]
        p = []
        f = []
        x = 'p{}.txt'
        y = 'f{}.txt'
        for i in range(m):
            p.append(np.loadtxt(x.format(i)))
            f.append(np.loadtxt(y.format(i)))
        self.p = p
        self.m = m
        self.n = n
        self.f = f
        self.alpha = alpha
        self.delta = delta
        self.epsilon = epsilon

    def ImprovementAlgorithm(self):
        m = self.m
        n = self.n
        alpha = self.alpha
        p = self.p
        f = self.f
        v = np.zeros(n)
        delta = self.delta
        epsilon = self.epsilon
        listV = []
        while delta > epsilon:
            q = np.zeros((m, n))
            for i in range(m):
                q[i] = f[i] + alpha * p[i].dot(v)
            w = q[0]
            a = np.ones(n, dtype=np.int64)

            for i in range(n):
                for j in range(m):
                    if q[j][i] < w[i]:
                        w[i] = q[j][i]
                        a[i] = j + 1
            delta = max(abs(v - w))
            v = w
            listV.append(v)
         

        for i in range(m):
            q[i] = f[i] + alpha * p[i].dot(v)
        w = q[0]
        a = np.zeros(n, dtype=np.int64)
        for i in range(n):
            for j in range(m):
                if q[j][i] < w[i]:
                    w[i] = q[j][i]
                    a[i] = j
                    
                    
        result = dict()
        result['v'] = v
        result['a'] = a+1
        result['listV'] = listV
        return result

    def PolicyImprovementAlgorithm(self):
        m = self.m
        n = self.n
        alpha = self.alpha
        p = self.p
        f = self.f
        v = np.zeros(n)
        delta = self.delta
        epsilon = self.epsilon
        w = f[0]
        a = np.zeros(n, dtype=np.int64)
        g = np.zeros(n)
        I = np.eye(n)
        for i in range(n):
            for j in range(m):
                if f[j][i] < w[i]:
                    w[i] = f[j][i]
                    a[i] = j

        number = 0
        listA=[]
        listV=[]
        while (delta > epsilon):
            number = number + 1
            listA.append(a+1)

            for i in range(n):
                g[i] = f[a[i]][i]

            q = np.zeros((n, n))
            
            for i in range(n):
                q[i] = p[a[i]][i]

            v = np.linalg.inv(I - alpha * q).dot(g)
            listV.append(v)

            k = np.zeros((m, n))
            for i in range(m):
                k[i] = f[i] + alpha * p[i].dot(v)
            w = k[0]

            b = np.zeros(n, dtype=np.int64)
            for i in range(n):
                for j in range(m):
                    if k[j][i] < w[i]:
                        w[i] = k[j][i]
                        b[i] = j

            delta = max(abs(a - b))
            a = b
            
        result = dict()
        result['listA'] = listA
        result['listV'] = listV
        result['number']= number
        return result

    def PolicyImprovementforAverageCosts(self):
        m = self.m
        n = self.n
        p = self.p
        f = self.f
        delta = self.delta
        epsilon = self.epsilon
        A = np.eye(n + 1)
        A[n][0] = 1
        A[n][n] = 0
        for i in range(n):
            A[i][n] = 1

        w = f[0]
        a = np.zeros(n, dtype=np.int64)
        g = np.zeros(n + 1)
        h = np.zeros(n)

        listA=[]
        listH=[]
        listPhi=[]

        for i in range(n):
            for j in range(m):
                if f[j][i] < w[i]:
                    w[i] = f[j][i]
                    a[i] = j

        number = 0
        while (delta > epsilon):
            number = number + 1
            listA.append(a+1)

            for i in range(n):
                g[i] = f[a[i]][i]
            g[n] = 0

            q = np.zeros((n + 1, n + 1))
            for i in range(n):
                for j in range(n):
                    q[i][j] = p[a[i]][i][j]
            for i in range(n):
                q[i][n] = q[n][i] = 0

            v = np.linalg.inv(A - q).dot(g)
            

            for i in range(n):
                h[i] = v[i]
                
            listH.append(h)
            listPhi.append(v[n])

            k = np.zeros((m, n))
            for i in range(m):
                k[i] = f[i] + p[i].dot(h)
            w = k[0]

            b = np.zeros(n, dtype=np.int64)
            for i in range(n):
                for j in range(m):
                    if k[j][i] < w[i]:
                        w[i] = k[j][i]
                        b[i] = j

            delta = max(abs(a - b))
            a = b
            
        result = dict()
        result['listA'] = listA
        result['listH'] = listH
        result['listPhi']=listPhi
        result['number']= number
        return result
