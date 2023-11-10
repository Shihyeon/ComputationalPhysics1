# 과제 1 #04 문제

import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E, sqrt
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화


#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

f = x**5 - 1

g = sympy.factor(f)

sol_g = sympy.solve(g)


#-----------[print]-------------

print(sol_g)