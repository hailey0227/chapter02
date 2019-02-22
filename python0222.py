# 주석을 남기기 위한 기호는 #
# 파이썬이 지원하는 숫자형
# 정수, 실수, 복소수, 8진수, 16진수
# 8진수 : 0o숫자 (영문 소문자 혹은 대문자 o을 사용)
# 16진수 : 0x숫자 (영문 소문자 x를 사용)

print("정수형 출력")
print(123)
print(-178)

print("실수형 출력")
print(3.14)
print(-3.14)

print("8진수 출력")
print(0o177)

print("16진수 출력")
print(0x1234)
print(-0x1234)


print("복소수 출력")
a = 1 + 2j
print(a)
b = 3 - 4j
print(b)

a = 1 + 2j
print("실수 부분 출력 : %s" % a.real)
print("허수 부분 출력 : %s" % a.imag)
print("켤레복소수 출력 : %s" % a.conjugate())
print("절대값 출력 : %s" % abs(a))


# 숫자형을 활용하기 위한 연산자
# 기본 4칙연산
# +, -, *, /, **(제곱 연산), %(나머지 연산)

a = 3
b = 4
c = a + b
print("a + b = %s" %c)
c = a - b
print("a - b = %s" %c)
c = a * b
print("a * b = %s" %c)
c = a / b
print("a / b = %s" %c)
c = a % c
d = "%" 
print("a %s b = %s" %d, %c)