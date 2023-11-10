# 전산물리학1 14강


s1 = set([1, 2, 3])    # 집합 s1 생성
print(s1)

s2 = set('Hello')
print(s2)    # 출력하면 각각의 알파벳이 원소로 set s2를 출력하나 중복된 원소는 하나로 통일된다. 이때, 원소의 순서가 없다(unordered). -> 순서가 없으므로 index 불가능

s3 = set([3, 4, 5])

print(s1&s3)    # set s1과 s3의 intersection(교집합)
print(s1.intersection(s3))    # set s1과 s3의 intersection

print(s1|s3)    # set s1과 s3의 union(합집합)
print(s1.union(s3))    # set s1과 s3의 union

print(s1-s3)    # set s1과 s3의 difference(차집합) (교환법칙 성립 X)
print(s1.difference(s3))    # set s1과 s3의 difference


t = True    # class <bool>
f = False    # class <bool>

print(1 == 1)
print(2 > 1)
print(2 < 1)

# 자료형에서 값이 비어있으면 False이고, 비어있지 않으면 True이다.

# while은 반복 구문으로 True일 때 작동하며 False일 때 중지된다.

while s1:
    print(s1.pop())

s1.update([1, 2, 3])    # set s1에 원소 {1}, {2}, {3} 추가