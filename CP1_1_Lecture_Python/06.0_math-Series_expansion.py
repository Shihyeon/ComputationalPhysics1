# 전산물리학1 6강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

x0 = sympy.Symbol("{x_0}")

f = sympy.Function("f")(x)



#-----------[print]-------------

print()

print(sympy.series(f, x))    # 함수 f를 Tayler extansion (order은 default=6)
print(f.series(x))    # 위와 같다.

print()

print(f.series(x, x0, n=2))    # x=x_0에서 order이 2까지 함수 f를 Tayler extansion (order을 안 적을 시 기본값 n=6)

print()
