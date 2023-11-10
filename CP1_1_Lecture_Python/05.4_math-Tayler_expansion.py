# 전산물리학1 5강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

x0 = sympy.Symbol("{x_0}")

a, b, c = sympy.symbols("a, b, c", positive=True)    # a, b, c 문자 선언


g = sympy.Function('g')(x)    # 변수가 x인 일변수 함수 g

f = sin(x)


#-----------[print]-------------

print()

print(sympy.series(g, x))    # 테일러 전개

print()

print(sympy.series(f, x))    # 테일러 전개

print()

print(g.series(x, x0, n=2))    # 테일러 전개

print()

print(g.series(x, x0, n=2).removeO())    # 테일러 전개 (removeO()는 O항을 삭제 후 출력한다.)

print()

print(f.series(x, 0, n=6))    # 함수 f를 테일러 전개 후, x=0부터 order가 6까지 전개

print()

