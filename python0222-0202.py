# 문자열 사용하기
# 파이썬은 문자 타입과 문자열 타입의 구분이 없음
# 문자열은 "" 로 감싼 문자는 모두 문자열로 표현
# 문자열로 표시 문자 " ", ' ', """ """, ''' ''' 총 4개의 타입이 존재함

print("문자열 출력하기")
print("\" 를 통해서 문자열 출력")
print('\' 를 통해서 문자열 출력')

str = """ 쌍따옴표를 3개 사용하는 방식은
입력하는 그대로
화면에 출력하기 위해서 임 """
print(str)

str = ''' 홀따옴표를 3개 사용하는 방식도
입력하는 그대로
화면에 출력하기 위해서 임 '''
print(str)

# 문자열 사용 시 이스케이프 문자 사용 가능
# \n : 문자열 안에서 줄 바꿈을 실행
# \t : 문자열 안에서 tab 키를 누른 효과
# \a : 컴퓨터에서 알람 효과
# \b : 백스페이스바 키 누른 효과
# \" : 문자열 안에서 문자로서의 "를 출력
# \' : 문자열 안에서 문자로서의 '를 출력
# \\ : 문자열 안에서 문자로서의 \를 출력
# \1000 : 널문자 출력

multiline = "Life is too short\nYou need python"
print(multiline)

multiline = "Life is too short\fYou need python"
print(multiline)

# 문자열 연산
# 파이썬 다른 언어와 달리 여러가지 연산자를 지원함
# +, *
# + : 다른 언어와 같은 기능을 하는 연산자로 문자열끼리 연결시켜 하나의 문자열로 만듬
# * : 다른 언어에는 없는 기능으로 문자열을 반복해서 출력할 수 있는 기능을 지원함

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python" 
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인덱싱
# 문자열은 문자 타입의 베열괴 같다
# 시작 인덱스는 0임
# 해당하는 위치의 인덱스 번호를 사용하면 그 위치의 문자를 알 수 있음
# 자바에서 배열을 사용하듯이 파이썬에서 사용할 수 있음
# a = "My first python program!"
# 위와 같은 문자열리 있을 경우 y를 출력하고 싶은 경우 배열처럼 변수명[index]로 사용함
# a[10]

a = "My first python program!"
print(a[10])

# 문자 술라이싱
# 파이썬에서 문자열 처리 시 특정 위치의 글자를 출력할 때 엑셀에서 특정 셀 범위 설정하는 방법과 같이 사용이 가능함
# a[시작번호:끝번호]
# a[0:10]
# 문자열 변수 a에서 인덱스번호 0 ~ 10까지의 문자를 출력함
print(a[0:10])

print(a[9:15])
# 자바에서는 Substring, split 이라는 메서드를 사용하여 문자열을 잘라서 특정 위치의 문자열을 가지고 와야하지만 파이썬에서는 문자 슬라이싱을 통해서 쉽게 구현이 가능하다

# 문자열 슬라이싱 시 시작 번호나 끝 번호를 입력하지 않으면 처음부터 끝번호까지 출력하거나, 시작번호부터 끝까지 출력함
print(a[:15])
print(a[15:])

# 변수와 함께 사용 시 원하는 부분을 글자만 변수에 저장이 가능함
b = a[:15]
c = a[15:]
d = a[9:15]
print(b)
print(c)
print(d)


print("=" * 100)
print()

# 문자열 포매팅
# 문자열을 화면에 출력할 때 문자열 포멧을 통하여 사용자가 원하는 형태로 출력할 수 있음
# 문자열 포멧 코드
# %s : 문자열 출력
# %c : 문자 1개 출력
# %d : 정수 출력
# %f : 실수 출력
# %o : 8진수 출력
# %x : 16진수 출력
# %% : 문자 % 출력

# %s 는 해당 위치에 문자열을 출력함
# 어떤한 타입의 값을 모두 문자열로 출력함

# 정수인 3을 %d에 대입
print("I have %d apples" % 3)
# 정수인 3을 문자열로 변환하여 %s에 대입
print("I have %s apples" % 3)
# 실수인 3.234를 %f에 대입
print("rate is %f" % 3.234)
# 실수인 3.234를 문자열 3.234로 변환하여 %s에 대입
print("rate is %s" % 3.234)

# 문자열에 % 문자를 출력할 경우 %%를 2번 입력한다.
print("Error is %d%%." % 98)

# 문자열 출력 코드인 %s에 총 문자열의 크기를 입력하여 표시하면 입력한 문자열의 크기만큼 글자가 입력됨
# - 부호가 있을 경우 왼쪽 정렬, 없을 경우 오른쪽 정렬
print("%10s jane" % "hi!")
print("%-10s jane" % "hi!")

# 숫자형에도 %와 기호 사이에 범위 숫자를 입력하면 그 길이만큼 숫자의 자리를 확보함
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

print("%4d" % 10)



# 파이썬 문자열 함수
# count() : 문자 개수 확인
# len() : 문자열의 길이 확인
# find() : 문자 위치 확인
# join() : 문자 삽입하디
# upper() : 영문 소문자를 대문자로 변경
# lower() : 영문 대문자를 소문자로 변경
# strip() : 문자열 양쪽 공백 삭제
# replace() : 문자열 변경하기 - 많이 사용
# split() : 문자열 나누기

a = "hobby"
print("문자열에서 b의 개수 확인 : %s" % a.count('b'))
print("문자열 길이 확인 : %s" % len(a))

a = "Python is best choice"
print("문자 'b'가 처음 나온 위치는 : %s" % a.find('b'))


# 2019-02-25 수업내용

a = ","
print(a.join("abcd"))

a = "hi" # 데이터베이스와 연동하게 될 때 사용
print("영문 대문자로 출력 : %s " % a.upper())

a = "HI"
print("영문 소문자로 출력 : %s " % a.lower())


a = "     hi"
print("원본 문장 : %s" % a)
print("왼쪽 공백 지우기 : %s" % a.lstrip())

a = "hi     " # 데이터베이스와 함께 사용
print("원본 문장 : %s" % a)
print("오른쪽 공백 지우기 : %s" % a.rstrip())

a = "     hi     " #훨씬 더 많이 사용
print("원본 문장 : %s" % a)
print("양쪽 공백 지우기 : %s" % a.strip())

a = "Life is so short"
print("원본 문장 : %s" % a)
print("수정된 문장 : %s" % a.replace("Life", "your leg"))

# split() 를 사용하면 지정한 문자로 문자열을 나누어서 문자열 배열에 출력함 / 기상청 RSS 등에 이용
a = "Life is too short"
print("원본 문장 : %s" % a)
print("나누어진 문장 : %s" % a.split())

a = "a:b:c:d"
print("원본 문장 : %s" % a)
print("나누어진 문장 : %s" % a.split(":"))

str = "부산, 울산, 경상남도는 2월 28일 오전과 3월 2일 오후~3일 오전에는 기압골 영향으로 비가 오겠으며, 그 밖의 날은 고기압의 영향으로 대체로 맑은 날이 많겠습니다.<br />기온은 평년(최저기온: -4~3℃, 최고기온: 9~12℃)보다 조금 높겠습니다.<br />강수량은 평년(1~3mm)보다 많겠습니다. <br />바다의 물결은 남해동부와 동해남부 전해상에서 3월 2~4일에 기압골 영향으로 1.0~4.0m로 매우 높게 일겠고, 그 밖의 날은 0.5~2.5m로 일겠습니다."
print(str.split("<br />"))


print()
print("=" * 80)
print()

test1 = 10.0
print("화면에 출력한 코드 %f" % test1)
print("화면에 출력한 코드 %d" % test1)

test1 = 100
print("화면에 출력한 코드 %d" % test1)
print("화면에 출력한 코드 %f" % test1)

print()
print("=" * 80)
print()

# 문자열 코드를 사용하지 않고 format() 함수를 이용하여 문자열을 형식에 맞게 출력
# 문자열 코드 대신 {0} 을 사용하여 각종 데이터가 들어갈 부분을 표현
# 입력될 데이터가 여러개일 경우 {0} {1} {2} {n} 으로 표현
# 값은 format(첫번째값, 두번째값, 세번째값, n번째값)으로 데이터를 입력
print(".format() 함수를 이용하여 문자열을 쉽게 표현하기")

# 숫자 대입하기
print("I eat %d apples" % 3)
print("I eat {0} apples".format(3))

# 문자열 대입하기
print("I eat %s apples" % "five")
print("I eat {0} apples".format("five"))

# 변수를 대입하기
number = 3
print("I eat %d apples" % number)
print("I eat {0} apples".format(number))

# 정수와 실수 대입하기
number1 = 100
number2 = 100.0
print("정수 출력 : %d. \n소수 출력 : %f" % (number1, number2))
print("정수 출력 : %f. \n소수 출력 : %d" % (number1, number2))
print("정수 출력 : {0}. \n소수 출력 : {1}".format(number1, number2))

# 2개 이상의 값 넣기
number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days.".format(number, day))

# format() 함수 사용시 {index} 대신 {변수이름} 으로 사용이 가능함
print("I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3))

# {index} 와 {변수이름} 을 동시에 혼용해서 사용이 가능함
print("I ate {0} apples. so I was sick for {day} days.".format(10, day = 3))

# 문자열 왼쪽 정렬
print("문자열 왼쪽 정렬 : %-10s jane" % "hi" )
print("문자열 왼쪽 정렬 : {0: <10} jane".format("hi"))

# 문자열 오른쪽 정렬
print("문자열 오른쪽 정렬 : %10s jane" % "hi" )
print("문자열 오른쪽 정렬 : {0: >10} jane".format("hi"))

# 문자열 중앙 정렬
print("문자열 중앙 정렬 : {0: ^10} jane".format("hi"))

# 공백 채우기
print("문자열 공백 채우기 : {0:!<10} jane".format("hi"))
print("문자열 형식 채워서 표현하기 : {0:0>10}".format(100))

# 소수점 표현하기
y = 3.42134234
# 소수점 4자리까지 표현
print("{0:0.4f}".format(y)) # . 도 갯수로 취급

# 소수점 5자리까지 표현하고, 전체 자리수는 10자리로 표현
print("{0:10.5f}".format(y))

# 문자 {} 표현하기 (%를 화면에 출력하듯이 2번 입력)
print("{{ and }}".format())

