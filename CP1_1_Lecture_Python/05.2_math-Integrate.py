# 전산물리학1 5강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

y = sympy.Symbol("y")    # y 변수 선언

a = sympy.Symbol("a")    # a 문자 선언

b = sympy.Symbol("b")    # b 문자 선언



f = sympy.Function('f')(x)    # 변수가 x인 일변수 함수 f




#-----------[print]-------------

print()

print(sympy.integrate(f))    # f를 부정적분

print()

print(sympy.integrate(f, (x, a, b)))    # f를 x에 대해 a에서 b로 정적분