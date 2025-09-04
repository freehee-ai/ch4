# set 만들기
s1 = {1,2,3}
print(s1, type(s1)) #<class 'set'>
# 빈 셋을 만들면 딕셔너리가 된다
s2 = {}
print(s2, type(s2)) #<class 'dict'>

# 형변환
# list -> set
s3 = set([1,2,3])
print(s3)
# string -> set
# 문자열의 몬자들이 쪼개져서 set 으로 저장됨
# set 은 순서없음, 중복불가
s4 = set('string')
print(s4)

s5 =set('hello')
print(s5)

