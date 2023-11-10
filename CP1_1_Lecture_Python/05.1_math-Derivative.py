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

f = exp(cos(x))    # 변수가 x인 일변수 함수 f

g = cos(x)*sin(y)*exp(x+y)    # 변수가 x, y인 다변수 함수 g


df = sympy.Derivative(f, x)

dg = sympy.Derivative(g, x, 2, y, 3)


#-----------[print]-------------

print()

print(df)    # df를 출력

print()

print(df.doit())    # f를 미분한 값 출력

# Derivative는 doit을 해야 수식 계산 결과가 출력이 되고,
# diff는 doit 필요 없이 수식 계산 결과가 출력된다.


