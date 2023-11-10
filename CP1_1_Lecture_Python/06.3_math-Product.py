# 전산물리학1 6강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

n = sympy.Symbol("n", integer=True)    # n 변수 선언



product1 = sympy.Product(n, (n, 1, 7))    # 수열 n을 1부터 7까지 곱



#-----------[print]-------------

print()

print(product1.doit())    # sum1 출력

print()
