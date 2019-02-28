# -*-coding:utf-8
import sys 

# 변수
# C나 자바와 같은 다른 언어와 달리 변수 선언 시 자료형을 입력할 필요가 없음
# C#, javascript 에는 var 타입이 존재함
# php 는 변수 선언 시 $로 통일함
# 위의 언어들은 모두 값의 자료형을 자동으로 유추함

# 파이썬은 변수 선언 시 자료형을 입력하지 않음
# 파이썬은 모든 데이터형이 모두 객체형임
# 파이썬은 자바와 달리 모든 자료형이 참조형임

# 아래는 자바에서의 값타입과 참조타입 차이점
# int num1 = 100;
# int num2 = 100;

# if (num1 == num2) // true

# string java1 = "자바";
# string java2 = new String("자바");

# if (java1 == java2) // false

# 파이썬은 모든 자료형이 참조형이기 때문에 참조하는 곳이 같은지 확인하는 is 명령어를 사용하여 확인함
# 값을 확인해도 동일함
a = 3
b = 3
print("a와 b가 참조하는 곳이 같다 : {0}".format(a is b))

if (a == b):
    print("a와 b는 참조하는 곳이 같다.")
else:
    print("a와 b는 참조하는 곳이 다르다.")

c = 3
print(sys.getrefcount(3))
d = 3
print(sys.getrefcount(3))
e = 3
print(sys.getrefcount(3))
f = 3
print(sys.getrefcount(3))


# 변수 선언의 여러가지 방법
# 2개의 변수와 2개의 값을 동시에 선언하고 변수 하나에 하나의 값을 순서대로 대입함
print()
a, b = ("Python", "life")
print("변수 a의 값: {0}".format(a))
print("변수 b의 값: {0}".format(b))

# string a = "python"; // 자바의 기본 변수 선언
# string a, b = "python"; // 자바에서 동시에 2개의 변수 선언

# 변수를 튜플 형태로 선언하고 값도 튜플 형태로 대입함
# 튜플은 괄호를 입력하지 않아도 튜플로 인식함
print()
(a, b) = "Python", "life" # 괄호를 삭제해도 튜플로 인식
print("변수 a의 값: {0}".format(a))
print("변수 b의 값: {0}".format(b))

# 변수를 리스트 형태로 선언하고 값도 리스트 형태로 대입함
print()
[a, b] = ["Python", "life"]
print("변수 a의 값: {0}".format(a))
print("변수 b의 값: {0}".format(b))

# 변수를 2개 이상 선언하고 하나의 값으로 대입
print()
a = b = "Python"
print("변수 a의 값: {0}".format(a))
print("변수 b의 값: {0}".format(b))

# 변수의 값 스왑
# 파이썬은 함수를 만들 필요가 없음

# a = 10
# b = 20
# temp = 0

# temp = a
# a = b
# b = temp

a = 3
b = 5
(a, b) = (b, a)
print("변수 a의 값: {0}\n변수 b의 값 : {1}".format(a,b)) 

# 변수 삭제하기
# del() 메모리에서 해당 변수를 삭제

a = 3
b = 3
print("a의 값은 : {0}".format(a))
print("b의 값은 : {0}".format(b))
print("a의 참조 카운트 : {0}".format(sys.getrefcount(a)))
print("b의 참조 카운트 : {0}".format(sys.getrefcount(b)))
del(a)
del(b)
# del 함수를 사용하여 변수 a와 b를 삭제하여 변수 a와 b를 더 이상 사용할 수 없음
# print("del 사용 후의 a의 참조 카운트 : {0}".format(sys.getrefcount(a)))
# print("del 사용 후의 b의 참조 카운트 : {0}".format(sys.getrefcount(b)))

# 리스트 복사
# 리스트를 복사하는 일반적인 방법은 반복문을 사용하여 리스트 내용을 다른 리스트에 대입하는 방법

# 반복문을 사용하여 리스트 복사
a = [1, 2, 3]
print("원본 리스트 출력 : {0}".format(a))
b = a
# 변수 b에 리스트 a를 대입
# 변수 b에 리스트 값 [1, 2, 3] 이 대입된 것이 아니라 변수 b에 리스트 a의 주소가 대입됨
print("리스트 b 출력 : {0}".format(b)) # 출력 내용을 보고 제대로 복사가 되었구나 생각을 한다.
# 리스트 a의 index 2의 값 수정
a[2] = 10 # b는 고친 적이 없지만 출력 내용을 보면 b의 값도 변경되어있다.
print("리스트 a 수정 후 출력 : {0}".format(a))
# 리스트 비의 요소를 수정하지 않았으나 리스트 에이와 같이 값이 수정됨
# 변수 에이에 리스트 에이의 주소가 대입되었기 때문에 리스트 에이의 요소가 수정되면 리스트 비의 요소도 함께 수정된 것처럼 보임
# 이유는 동일한 주소를 참조하고 있기 때문
print("리스트 b 출력 : {0}".format(b))


print("a와 b는 같다 : {0}".format(a is b))

# 그럼 어떻게? 반복문 이용하기

# 파이썬이 다른 언어에서 복사 함수를 시용하지 않고 베열이나 리스트를 다른 리스트로
count = 0
c = []
while (count < len(a)):
    c.append(a[count])
    count += 1

print("리스트 c 출력 : {0}".format(c)) # 지금까지는 똑같다.
a[2] = 100
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
print("리스트 c 출력 : {0}".format(c)) # 다른 값

# 파이썬의 리스트 출력 방식을 사용하여 리스트 a의 모든 값을 리스트 b로 복사
print()
a = [1, 2, 3]
b = a[:] # [:] 맨 처음부터 맨 끝까지
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
a[2] = 100
print("수정 후 리스트 a 출력 : {0}".format(a))
print("수정 후 리스트 b 출력 : {0}".format(b))

# 
print()
from copy import copy
a = [1, 2, 3]
b = copy(a)
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
# a[2] = 100
#print("수정 후 리스트 a 출력 : {0}".format(a))
#print("수정 후 리스트 b 출력 : {0}".format(b))