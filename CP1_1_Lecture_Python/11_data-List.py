# 전산물리학1 11강


a = "My favorite food is apple."

print(a.count("a"))    # a에서 "a"가 몇 개인지 count (대소문자 구분)

print(a.find("a"))    # a에서 찾고자 하는 문자(또는 단어) "a"의 첫 번째 위치를 출력 (찾고자 하는 문자가 없을 시 '-1' 출력)

print(a.index("a"))    # a에서 찾고자 하는 문자(또는 단어) "a"의 첫 번째 위치를 출력 (찾고자 하는 문자가 없을 시 에러)


print(", ".join("abcd"))    # "abcd" 사이에 ", "를 join

print(a.upper())    # 소문자를 대문자로 바꾸기

print(a.lower())    # 대문자를 소문자로 바꾸기


b = "     Hi     "

print(b.lstrip())    # 문자열 중 가장 좌측에 있는 연속된 공백을 모두 지운다

print(b.rstrip())    # 문자열 중 가장 우측에 있는 연속된 공백을 모두 지운다

print(b.strip())    # 문자열에 연속된 공백을 모두 지운다


print(a.replace("apple", "cake"))    # a에서 "apple"을 "cake"로 replace


c = "a:b:c:d"

print(a.split())    # 공백을 기준으로 문자열을 나누어 리스트로 만든다.

print(c.split(":"))    # ":"을 기준으로 문자열을 나누어 리스트로 만든다.


print(a[12:16])    # 슬라이싱으로 문자 연결

print(a.split()[2])    # split으로 리스트 내에서 indexting


d = ["a", "b", "c", "d", "e"]    # list는 대괄호([])로 감싸고 반점(,)으로 연결시켜 만들 수 있다

e = [1, 2, [3, 4, 5]]    # list 내에 list를 넣을 수 있다

print(e[0]+e[1])    # list에서 문자열처럼 indexing, slicing, split 등 가능

print(e[2][1])    # list e에서 2인 이중 list [3, 4, 5]에서 1인 '4' indexing

print(e[-1][-1])    # list e에서 -1인 이중 list [3, 4, 5]에서 -1인 '5' indexing


f = ["a", "b", "c", [1, 2, 3, ["d", "e", "f"]]]

print(f[-1][-1][-1])    # 다중 list indexing


print(len(d))    # list의 길이 len은 list 요소의 개수이다


g = [1, 2, 3, 4, 5]

h = ["1", "2", "3", "4", "5"]

print(str(g[0]))    # 정수형을 문자형으로 바꾸기

print(int(h[1]))    # 문자형을 정수형으로 바꾸기


i = [1, 2, 3]

del i[1]    # i의 요소 1번째 삭제 (슬라이싱 기법으로 연속된 삭제 가능)

print(i)


j = [1, 2, 3]

j.append(4)    # list j에 요소 4 추가

print(j)


k = [2, 4, 1, 3]

k.sort()    # list 오름차순 정렬

print(k)


l = ["c", "a", "b"]

l.reverse()    # 정렬하지 않고, 앞/뒤 뒤집기

print(l)


m = [1, 2, 3]

m.insert(0, 4)    # 0번째 위치에 요소 4 삽입

print(m)


n = [1, 2, 3, 3]

n.remove(3)    # list n에서 첫 번째 요소 3을 삭제

print(n)

n.remove(3)

print(n)


o = [1, 2, 3]

print(o.pop())    # 마지막 요소 꺼내고 삭제 (유사 잘라내기)

print(o)


p = [1, 2, 3]

print(p.pop(0))    # 0번째 요소 꺼내고 삭제 (유사 잘라내기)

print(p)


q = [1, 1, 2, 3]

print(q.count(1))    # list q에서 1의 개수 count


r = [1, 2, 3]

r.extend([4, 5])    # list r에 [4, 5] 확장(추가)

print(r)


s = [1, 2, 3]

t = [4, 5]

s.extend(t)    # list r에 list t 확장(추가)

print(s)