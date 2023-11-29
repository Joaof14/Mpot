import numpy as np
A = np.array([[3,0,1], [2,2,2], [4,2,5]])
B = np.array([[2,1,0], [2,5,3], [0,1,6]])
n = A.shape[1]
maxit = 10000
ys = []
yo = np.ones(n)
zs = []
autovls = []
p = 0.0000000000001