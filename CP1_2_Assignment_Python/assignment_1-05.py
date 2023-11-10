# 과제 1 #05 문제

import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E, sqrt, tan
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화


#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

f = log((sin(x))**2*exp(tan(x)) + 1)

diff_f = sympy.diff(f, x)


#-----------[print]-------------

print(diff_f)
print(sympy.simplify(diff_f))
print(sympy.expand(diff_f))
print(sympy.factor(diff_f))