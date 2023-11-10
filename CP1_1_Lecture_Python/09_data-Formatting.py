# 전산물리학1 9강


import numpy as np


#----------[]----------


a = "%10s"    # 좌측에 10개의 공간을 만들고 %s 출력. (%Ns에서 N만큼의 공간을 추가하고 우측 정렬로 %s 출력. 이때 N이 음수이면 좌측 정렬로 %s 출력.)

print(a %"Hi")



pi = "pi = %f"

print(pi %np.pi)    # numpy로 실수 출력


pi1 = "pi1 = %10.6f"    # %N.nf일 때, N칸의 공백을 만들고 소수 n자리까지 유효숫자 생성하는데 N칸의 공백 안에 우측부터 정렬. (N=0일 때는 정렬을 하지 않는다.)

print(pi1 %np.pi)



b = "I eat {0} apples."    # {0}부터 포맷 코드 만들기

print(b.format(3))    # format 함수 : 포맷 코드에 3 출력

print(b.format("three"))    # format 함수 : 포맷 코드에 three 출력



c = "I eat {0} apples. so I was sick for {1} days."    # {0}부터 포맷 코드 만들기

n = 1

m = "three"

print(c.format(n, m))    # format 함수 : 포맷 코드 {0}부터 출력



d = "I eat {A} apples. so I was sick for {B} days."    # 포맷 코드 변수를 지정

print(d.format(A=10, B="three"))    # format 함수 : 포맷 코드 변수에 출력




print("{0:<10}".format("Hi"))    # format 함수 : 10개의 공간을 만들고 좌측 정렬로 format code 출력

print("{0:>10}".format("Hi"))    # format 함수 : 10개의 공간을 만들고 우측 정렬로 format code 출력

print("{0:^10}".format("Hi"))    # format 함수 : 10개의 공간을 만들고 가운데 정렬로 format code 출력


print("{0:=^10}".format("Hi"))    # format 함수 : 10개의 공간을 만들고 가운데 정렬로 format code 출력하고 나머지 공백에 = 출력

print("{0:!<10}".format("Hi"))    # format 함수 : 10개의 공간을 만들고 좌측 정렬로 format code 출력하고 나머지 공백에 ! 출력



print("pi = {0:10.4f}".format(np.pi))    # format 함수 : 소수점 4개이고 10개의 공간을 만들고 format code 출력



name = "LSY"

age = 20

print("My name is %s. My age is %d." %(name, age))    # format code

print("My name is {0}. My age is {1}.".format(name, age))    # format 함수

print(f"My name is {name}. My age is {age}.")    # f 문자열 : python 3.6이상만 사용 가능


print(f"My name is {name*2}. My age is {age*2+1}.")    # f 문자열 : format code 내에서 연산 가능



print(f"{'Hi':<10}")    # f 문자열 : 10개의 공간을 만들고 좌측 정렬로 format code 출력

print(f"{'Hi':>10}")    # f 문자열 : 10개의 공간을 만들고 우측 정렬로 format code 출력

print(f"{'Hi':^10}")    # f 문자열 : 10개의 공간을 만들고 가운데 정렬로 format code 출력



print(f"{np.pi:0.4f}")    # f 문자열 : 소수점 4개인 실수형 format code에 pi 출력

print(f"{np.pi:10.4f}")    # f 문자열 : 10개의 공간을 만들고 소수점 4개인 실수형 format code에 우측 정렬로 pi 출력