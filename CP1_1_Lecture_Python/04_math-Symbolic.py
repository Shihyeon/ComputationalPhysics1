# 전산물리학1 4강


import sympy    # sympy 가져오기
from sympy import I, pi, oo, sin, cos, exp, log
from sympy.solvers.solveset import substitution    # sympy에서 문자 정의

sympy.init_printing()    # 변수값 초기화






#-----------[변수(문자) 정의]-------------

x = sympy.Symbol("x")    # x 변수 선언

y = sympy.Symbol("y")    # y 변수 선언

z = sympy.Symbol("z")    # z 변수 선언

a = sympy.Symbol("a", real=True)    # a 수학적 문자 선언

b = sympy.Symbol("b", real=True)    # b 수학적 문자 선언





#-----------[수식 정의]-------------

expr = ( 5*x ) ** ( x - y )   # 수식 expr 정의

expr1 = sin ( x + y )

expr2 = log(a) - log(b)

expr3 = sin(x+y) + cos(x-y)

expr4 = 1/(x**2 + 3*x + 2)

expr5 = 1/(y*x + y) + 1/(1+x)

expr6 = y/(y*x + y)

expr7 = x + y




#-----------[print]-------------

print()

print("일반 수식 expr 출력")
print(expr)    # 수식 expr 출력

print()

print("symplipy 수식 expr 출력")
print(sympy.simplify(expr))    # simplipy : 수식 expr, 간결하게 출력 (인수분해 느낌의 형태)

print()

print("expand 수식 expr 출력")
print(sympy.expand(expr))    # expand : 수식 expr, 간결하게 출력 (전개 형태)

print()

print(sympy.expand(expr1, trig=True))    # expand(trig=True) : 수식 expr1, 간결하게 출력 (삼각함수 전개 형태)

print()

print(expr.expand(power_base=True, power_exp=False))    # base 부분만 expand 출력

print()

print(expr.expand(power_base=False, power_exp=True))    # exp 부분만 expand 출력

print()

print("factor 수식 expr 출력")
print(sympy.factor(expr))    # factor : 수식 expr, 인수분해 출력

print()

print("logcombine 출력")
print(sympy.logcombine(expr2))    # 로그 하나로 통일 후 출력

print()

print(expr2.collect(x))    # collect : 결합법칙, x에 대하여 묶기

print()

print("expand, collect")
print(expr3)    # expr 출력
print(expr3.expand(trig=True))    # expand(trig=True) 출력
print(expr3.expand(trig=True).collect([sin(x), cos(x)]))    # expand(trig=True), [sin(x), cos(x)]로 묶어 출력
print(expr3.expand(trig=True).collect([sin(x), cos(x)]).collect([cos(y)-sin(y)]))    # collect는 여러 겹 중첩 사용 가능

print()

print("분수형태")
print(sympy.apart(expr4, x))    # apart(x) : x 변수에 대해 부분분수 생성

print()

print(sympy.together(expr5))    # together : 통분

print()

print(sympy.cancel(expr6))    # cancel : 약분

print()

values = { x:4, y:2 }    # value 설정

print(expr7.subs(x, y))    # substitution : x를 y로 치환 후 출력

print(expr7.subs({x:exp(y), y:sin(y)}))    # substitution : x를 exp(y), y를 sin(y)로 치환 후 출력

print(expr7.subs(values))    # substitution(values) : expr7 함수에서 각 변수를 values로 치환 후 연산 출력

