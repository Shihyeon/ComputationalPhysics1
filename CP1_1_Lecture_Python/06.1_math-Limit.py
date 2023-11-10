# 전산물리학1 6강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

x0 = sympy.Symbol("{x_0}")

h = sympy.Symbol("h")

f = sin(x)/x

g = (1+1/x)**x


j = sympy.Function("j")

k = sympy.Function("k")(x)

diff_limit = ( j(x+h) - j(x) )/h


#-----------[print]-------------

print()

print(sympy.limit(f, x, 0))    # 함수 f(x)에서 x를 0으로 limit

print()

print(sympy.limit(g, x, oo))    # 함수 g(x)에서 x를 oo으로 limit

print()

print(sympy.limit(diff_limit.subs(j, cos), h, 0))    # limit을 이용하여 미분(함수 j의 미분계수 부분에서 h를 0으로 limit) : 함수 j를 cos로 치환하여 미분

print()

print(sympy.limit(diff_limit.subs(j, k), h, 0))    # limit을 이용하여 미분(함수 j의 미분계수 부분에서 h를 0으로 limit) : 함수 j를 k(x)로 치환하여 미분

print()