# 전산물리학1 8강



a = "Life is too short, You need Python"

b = a[0] + a[1] + a[2] + a[3]

c = a[0:4]    # 출력이 0 <= c < 4으로 됨. (0부터 3까지)

print(b)

print(c)




a = "I eat %d apples."

print(a %3)    # 문자열 a에서 %d에 3 formatting. (%d는 정수형 숫자 포맷 코드, %f는 실수형 숫자 포맷 코드, %s는 문자열 숫자 포맷 코드)


v1 = 10

v2 = "day"

b = "%d %s"

print(b %(v1, v2))