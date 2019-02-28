# 연습 문제

# 문자열 1
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print()

# 문자열 2
pin = "881120-1068234"
print(pin[7])
print()

# 리스트 1
a = [1, 3, 5, 4, 2]
a.sort() # 정렬 [1, 2, 3, 4, 5]
a.reverse()
print(a)
print()

# 리스트 2
a = ["Life", "is", "too", "short"]
result = "{0} {1} {2} {3}".format(a[0], a[1], a[2], a[3])
result = a[0] + " " + a[1] + " " + a[2] + " " + a[3] 
print(result)
print()

# 튜플 
a = (1, 2, 3)
b = (4,)
print(a + b)

a = (1, 2, 3)
a = a + (4,)
print(a)
print()

# 딕셔너리
a = {'A':90, 'B':80, 'C':70}
result = a.pop("B")
# result = a["b"]
# del(a["b"])
print(a)
print(result)
print()

# 변수
a = b = [1, 2, 3]
a[1] = 4 
print(b) # [1, 4, 3] 출력
# 결과 이유: a와 b는 같은 변수이기 때문에