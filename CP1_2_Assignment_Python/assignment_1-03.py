# 과제 1 #03 문제

import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E, sqrt
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화


#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

a = sympy.Symbol("a", positive=True)

n = sympy.Symbol("n", integer=True, positive=True)

f = x**2*(sin(n*pi*x/a))**2

int_f = sympy.integrate(f, (x, 0, a))

g = 2/a*int_f


#-----------[print]-------------

print(g)
print(sympy.expand(g))
print(sympy.factor(g))

