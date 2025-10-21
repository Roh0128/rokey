from scipy.linalg import solve
# ax+b
# 3x+1y=9
# 1x+2y=8
a=[[3,1],[1,2]]
b=[9,8]
x=solve(a,b)
print(f"solution:{x}")

from scipy.optimize import minimize
def f(x):
    return x**2+4*x+4

result=minimize(f,x0=0)
print(f"Optimal value:{result.x}")


from scipy.optimize import root
def equation(x):
    return x**2-4
sol=root(equation, x0=1)
print(f"Root:{sol.x}")


from scipy.stats import describe
data=[1,2,3,4,5,6,7]
stats=describe(data)
print(stats)
# 외도는 분포의 비대칭 정도
# 첨도는 분포의 뾰족한 정도

from scipy.sparse import csr_matrix
data=[
    [0,0,3],
    [4,0,0],
    [0,5,0]
]

sparse_matrix=csr_matrix(data)
print(sparse_matrix)
print(sparse_matrix.data)
