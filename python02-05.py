# 딕셔너리 사용하기
# key와 value로 구성되어 있는 자료형
# 기존의 배열 및 리스트, 튜플은 index 와 value 로 구성되어 있는 형태의 자료형임
# index가 없기 때문에 자료의 저장 순서가 없음
# 딕셔너리는 {} 기호를 사용
# key와 value의 구분은 : 을 사용
# 각 데이터의 구분은 , 로 구분함

dic = {"name" : "pey", "phone" : "01012345678", "birth" : "1118"}
print("딕셔너리를 사용한 자료형 : {0}".format(dic))
print("딕셔너리에서 원하는 값 출격 : {0}".format(dic["name"]))

testlist = ["pey", "01012345678", "1118"]

# 리스트를 for 문을 통하여 모든 값을 출력
for value in testlist:
    print(value)

# 딕셔너리의 모든 값을 for 문을 통하여 출력
for value in dic:
    print(dic[value])    

# 자바의 경우 일반적인 for 문으로 hashmap(딕셔너리)의 내용을 모두 출력할 수 없음
# foreach(향상된 for문)문을 사용하여 hashmap의 내용을 출력해야 함

# 딕셔너리에 key와 value 추가하기

# 변수 a 에 딕셔너리를 직접 대입함
a = {1 : "a"}
print("원본 딕셔너리 출력 : {0}".format(a))

# 딕셔너리 변수 a에 a[key] = value 형태로 값을 대입함
a[2] = "b" # 숫자 2가 key가 된 것
print("추가된 딕셔너리 출력 : {0}".format(a))
a[10] = "c"
print("다시 추가된 딕셔너리 출력 : {0}".format(a))
a["dic"] = "딕셔너리"
print("다시 또 추가된 딕셔너리 출력 : {0}".format(a))
a[10] = "10"
print("key가 10인 요소 수정: {0}".format(a))
a["list"] = [1, 2, 3, 4, 5]
print("딕셔너리의 요소로 리스트 추가 : {0}".format(a))
a["tuple"] = ("a", "b", "c", "d", "e") # 원하는 것을 다 넣을 수 있다.
print("딕셔너리에 튜플 추가 : {0}".format(a))

# 딕셔너리 요소 삭제
# del() 함수를 사용하여 딕셔너리의 요소 삭제
# del(dic[key])

print()

del(a["tuple"])
del(a["list"])
print("del 함수를 이용하여 요소 삭제 : {0}".format(a))

# 딕셔너리 key 리스트 (keys)
# 딕셔너리의 key만 객체로 반환

dic = {"name" : "pey", "phone" : "01012345678", "birth" : "1118"}
print("keys 함수를 사용하여 딕셔너리의 key의 모음을 출력 : {0}".format(dic.keys()))

for k in dic.keys():
    print(k)

print("dict_keys 객체를 list로 변경 : {0}".format(list(dic.keys())))
print("dict_keys 객체를 tuple로 변경 : {0}".format(tuple(dic.keys())))

# 딕셔너리 value 리스트 (values)
print()
print("values를 이용하여 딕셔너리의 내용을 객체로 출력 : {0}".format(dic.values()))

# list함수와 tuple 함수를 이용하여 형 변환
print("dict_values 객체를 list로 변경 : {0}".format(list(dic.values())))
print("dict_values 객체를 tuple로 변경 : {0}".format(tuple(dic.values())))

# 딕셔너리에서 jey, value 동시에 얻기 (items)
print()
print("items 함수를 이용하여 dict_items 객체 얻기 : {0}".format(dic.items()))
print("dict_items 객체를 list로 변경 : {0}".format(list(dic.items())))

# 딕셔너리 내용 삭제 (clear)
# 딕셔너리 내용을 모두 삭제함
print()
print("원본 딕셔너리 출력 : {0}".format(dic))
print("clear 함수를 이용하여 딕셔너리 삭제 : {0}".format(dic.clear()))

# 딕셔너리 key를 이용하여 value 얻기 (get)
# 기존의 딕셔너리 value 사용 방법인 dic[key]와 결과값은 동일하지만 dic[key] 방식은 없는 키를 통해서 value를 호출하면 에러가 발생하지만 get 함수를 사용 시 없는 키를 통하여 value를 호출하면 None이 출력됨

dic = {"name" : "pey", "phone" : "01012345678", "birth" : "1118"}
print("dic.get(key) 방식으로 없는 키 사용 : {0}".format(dic.get("tel")))
print("dic[key] 방식으로 없는 키 사용 : {0}".format(dic["tel"]))

# 자료형의 참과 거짓
# 문자열은 빈 문자열이 아니면 true, 빈 문자열은 false
# 리스트 빈 리스트가 아니면 true, 빈 리스트는 false
# 튜플은 리스트와 동일
# 딕셔너리도 리스트와 동일
# 숫자형은 0이 아닌 모든 수는 true, 0은 false
# 값 None 은 false
print()