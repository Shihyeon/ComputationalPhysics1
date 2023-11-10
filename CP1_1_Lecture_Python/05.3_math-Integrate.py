# 전산물리학1 5강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언



f = exp(-x**2)

int_f = sympy.integrate(f, (x, 0, oo))


#-----------[print]-------------

print(int_f)