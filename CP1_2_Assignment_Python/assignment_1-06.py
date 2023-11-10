# 과제 1 #06 문제

import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E, sqrt
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화


#-----------[변수(문자) 정의]-------------

x, y = sympy.symbols("x, y")    # x, y 변수 선언

f = x**2 + y**2 - 1

g = 5*x - 7*y

eq = sympy.solve([f, g], [x, y], dict=True)


#-----------[print]-------------

print(eq)