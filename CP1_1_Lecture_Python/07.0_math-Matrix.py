# 전산물리학1 7강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

y = sympy.Symbol("y")

a, b, c, d = sympy.symbols("a, b, c, d")

x_1, x_2 = sympy.symbols("{x_1}, {x_2}")

f, g = sympy.symbols("f, g")


v1 = sympy.Matrix([1, 2])    # 2*1 matrix (column-wise matrix)

v2 = sympy.Matrix([[1, 2]])    # 1*2 matrix (row-wise matrix)

v3 = sympy.Matrix([[1, 2], [3, 4]])    # 2*2 matrix (row 1 = [1, 2], row 2 = [3, 4])



M1 = sympy.Matrix([[1, 2], [3, 4]])

u1 = sympy.Matrix([1, 2])


M2 = sympy.Matrix([[a, b], [c, d]])

u2 = sympy.Matrix([x_1, x_2])


M3 = sympy.Matrix(4, 5, lambda m, n : 10*m + n)    # 4*5 matrix인 (lambda)함수, 이때 python은 0부터 시작하기에 0by0부터 이어진다.

M4 = sympy.Matrix(4, 5, lambda m, n : 10*(m+1) + (n+1))    # 위에서 0부터 시작하는 것을 1부터 시작하게 바꾼 것.



#-----------[print]-------------

print()

print(M1*u1)    # 행렬곱

print()

print(M2*M2)    # 행렬곱

print()

print(M2*u2)    # 행렬곱

print()

print(sympy.det(M2))    # 행렬 M1의 determinant

print()

print(M2.inv())    # 행렬 M2의 역행렬

print()

# print(M2.LUsolve())    # 이해 잘 안 됨.

print()

print(M3)

print()

print(M4)