# 전산물리학1 6강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

y = sympy.Symbol("y")

a, b, c = sympy.symbols("a, b, c")


equation1 = x

equation2 = x**2 + 2*x

equation3 = x**3

equation4 = a*x**2 + b*x + c


eq5 = sin(x) - cos(x)

eq6 = exp(x) + 2*x

eq7 = exp(x) - 2/pi*x


l_eq1 = x + 2*y - 1

l_eq2 = x - y + 1

l_sol1 = sympy.solve([l_eq1, l_eq2], [x, y], dict=True)    # 연립방정식 : 두 방정식 l_eq1, l_eq2을 연립하여 두 변수 x, y의 해를 구함 (dictionary는 '[]'로 주변을 감싸어 깔끔하게 출력, dict를 사용하지 않을 시 순서쌍으로 출력)


l_eq3 = x**2 -y

l_eq4 = y**2 -x

l_sol2 = sympy.solve([l_eq3, l_eq4], [x, y], dict=True)    # 연립방정식 : 두 방정식 l_eq3, l_eq4을 연립하여 두 변수 x, y의 해를 구함



#-----------[print]-------------

print()

print(sympy.solve(equation1))    # equation1 함수의 해 출력

print()

print(sympy.solve(equation4, x))    # equation4 함수의 변수 x의 해 출력 (a, b, c는 상수로 취급)

print()

print(sympy.solve(eq5))    # eq5=tan(x)의 해를 닫힌구간 [x=0, x=pi/2] 사이 구간에서 출력

print()

print(l_sol1)    # l_sol1을 출력

print()

print(l_sol2)    # l_sol2을 출력

print()