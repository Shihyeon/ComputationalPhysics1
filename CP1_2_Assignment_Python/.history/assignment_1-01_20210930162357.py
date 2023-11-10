# 과제 1 #01 문제

import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E, sqrt
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화


#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

a, m, h = sympy.symbols("a, m, h", positive=True)

f = exp(-2*a*m*x**2/h)

int_f = sympy.integrate(f, (x, 0, oo))

g = abs(1/(2*int_f))

h = sqrt(g)


#-----------[print]-------------

print(h)