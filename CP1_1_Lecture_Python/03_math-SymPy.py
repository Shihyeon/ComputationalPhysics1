# 전산물리학1 3강


import sympy
from sympy import I, pi, oo, sqrt, cos

sympy.init_printing()    # 변수값 초기화


# 변수 선언

x = sympy.Symbol("x")

y = sympy.Symbol("y", positive=True)

z = sympy.Symbol("z", negative=True)


#-------------[print]---------------

print()

print(x**2)
print(sqrt(x**2))

print()

print(y**2)
print(sqrt(y**2))

print()

print(z**2)
print(sqrt(z**2))

print()




r1 = sympy.Rational(2, 3)

r2 = sympy.Rational(4, 5)

print(r1*r2)

print()



# 사용자 지정 함수 (함수 만들기)

h = sympy.Lambda(x, x**2)    # 함수 h는 x를 변수로 가진다. h(x) = x**2

print(h(5))

print()
