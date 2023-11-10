# 전산물리학1 6강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log, E
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화



#-----------[변수(문자) 정의]-------------

n = sympy.Symbol("n", integer=True)    # n 변수 선언



sum1 = sympy.Sum(1/(n**2), (n, 1, oo))    # 수열 1/(x**2)를 1부터 oo까지 합

sum_z = sympy.Sum(1/(n**3), (n, 1, oo))    # 수열 1/(x**3)를 1부터 oo까지 합 (x**k일 때, k가 홀수이면 제타함수로 출력됨)


#-----------[print]-------------

print()

print(sum1.doit())    # sum1 출력

print()

print(sum_z.doit())    # sum_z 출력 (제타함수)

print()

print(sympy.N(sum_z.doit()))    # sum_z(제타함수) 값을 출력

print()