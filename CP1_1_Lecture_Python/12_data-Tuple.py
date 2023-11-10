# 전산물리학1 12강



# 리스트는 '[]'로 표현하지만 튜플은 '()'으로 표현한다.
# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만, 튜플은 그 값을 변화시킬 수 없다.

t1 = ()    # 비어있는 tuple

t2 = (1,)    # 요소가 하나인 tuple. 단, 요소가 하나일 때는 요소 뒤에 반점(,)를 붙여야 한다.

t3 = (1, 2, 3)

t4 = 1, 2, 3    # tuple에서는 소괄호()를 생략해도 무방하다.

t5 = ('a', 'b', ('ab', 'cd'))    # tuple 내에 tuple이 있어도 된다.

print(t1)