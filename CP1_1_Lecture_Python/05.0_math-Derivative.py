# 전산물리학1 5강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

y = sympy.Symbol("y")    # y 변수 선언

z = sympy.Symbol("z")    # z 변수 선언



#-----------[함수 선언]-------------

f = sympy.Function('f')(x)    # 변수가 x인 일변수 함수 f

g = sympy.Function('g')(x, y)    # 변수가 x, y인 다변수 함수 g





#-----------[수식 정의]-------------







#-----------[print]-------------

print()

print(sympy.diff(f, x))    # 함수 f를 x에 대해 한 번 미분

print()

print(sympy.diff(f, x, x))    # 함수 f를 x에 대해 한 번 미분하고, x에 대해 미분 (x에 대해 두 번 미분)

print()

print(sympy.diff(f, x, 3))    # 함수 f를 x에 대해 세 번 미분

print()

print(g.diff(x, y))    # 함수 g를 x, y에 대해 각각 편미분

print()

print(g.diff(x, 3, y, 2))    # 함수 g를 x에 대해 3번 편미분하고, y에 대해 2번 편미분

print()

print(g.diff(x, x, x, y, y))    # 함수 g를 x에 대해 3번 편미분하고, y에 대해 2번 편미분

print()

