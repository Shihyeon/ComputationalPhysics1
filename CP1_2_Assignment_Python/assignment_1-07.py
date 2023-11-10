# 과제 1 #07 문제

import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E, sqrt
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화


#-----------[변수(문자) 정의]-------------

A = sympy.Matrix([[3, 1, 5], [2, 1, 7], [5, 3, 1]])

det_A = sympy.det(A)

inv_A = A.inv()


#-----------[print]-------------

print(det_A)

print(inv_A)