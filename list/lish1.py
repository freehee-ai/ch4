# 리스트 만들기

# 빈 리스트
# 대괄호를 쓰고 값의 목록 넣기
# lis =[]

# 숫자 리스트
lis2 = [1, 2, 3]

# 문자 리스트
lis3 = ['a', 'b', 'c']

# 혼합형 리스트
lis4 = [1, 2, 'abc', True]

upper_apb = ['A', 'B', 'C']
fruits = ['사과', '바나나', '딸기']
nums = [2, 4, 6, 8, 10]
lis_mix = ['hello', True]

# 3개 크기의 리스트 생성
lis = ['a', 'b', 'c']

# 첫번째 요소 꺼내기
# 리스트[인덱스번호]
print(lis[0])
print(lis[1])
print(lis[2])
#마지막 요소
print(lis[-1])

# 리스트 슬라이스
lis_sl = ['a', 'b', 'c', 'd', 'e']
# 리스트[시작:끝]
# 끝은 포함 안됨
print(lis_sl[0:2])
print(lis_sl[ :2])
print(lis_sl[2: ])
