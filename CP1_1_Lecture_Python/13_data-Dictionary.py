# 전산물리학1 13강


dic = {'name':'john', 'birth':'0206', 'sun':'2002'}    # dictionary : {'Key1':'Value1', 'Key2':'Value2', 'Key3':'Value3', ...}, dic은 함수와 비슷한 개념이다.


a = {1:'hi'}    # dic a 선언
print(a)

b = {'a':[1, 2, 3]}    # dic b 선언
print(b)


a[2] = 'b'    # dic a에 key가 2인 value 'b'를 추가
print(a)


del a[1]    # dic a에 key가 1인 것을 삭제
print(a)


Capital = {'Korea':'Seoul', 'USA':'Wa DC', 'Japan':'Tokyo'}

print(Capital['Korea'])    # dic Capital의 Korea key인 Seoul value 출력


# dic은 key 값으로 value에 접근한다.
# list는 key로 쓸 수 없고, tuple은 key로 쓸 수 있다. (key는 변하면 안 되는 값이기 때문)


print(Capital.keys())    # dic Capital의 key를 출력

print(list(Capital.keys()))    # dic Capital의 key를 list로 출력


for i in Capital.keys():
    print('%5s:    %5s' %(i, Capital[i]))    # 특정 패턴을 반복할 때, for 구문을 사용


print(Capital.values())    # dic Capital의 value를 출력

print(list(Capital.values()))    # dic Capital의 value를 list로 출력


print(Capital.items())    # dic Capital의 key와 value 쌍을 출력

print(list(Capital.items()))    # dic Capital의 key와 value 쌍을 list로 출력


b.clear()    # dic b를 clear
print(b)


print(Capital.get('Korea'))    # print(Capital['Korea'])와 동일

# get에서 key가 없으면 None을 출력하는데, print(Capital['Korea'])는 오류를 출력