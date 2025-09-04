# 딕셔너리 만들기
# 사람의 정보를 저장하는 딕셔너리 생성
dic = {'name':'둘리', 'phone': '010-1234-5678'}

# 값 추가하기
# 딕셔너리는 데이터를 저장할 때 순서가 없음
# 따라서 인덱스 번호가 없음
dic['age'] = 20
print(dic)
dic['address'] = '인천'
print(dic)


# 키목록 조회
print(dic.keys())
print(type(dic.keys()))
# dic_keys(['name','age,'address']) <- 리스트아님

# 값목록 조회
print(dic.values())

# 모든 데이터 조회
print(dic.items())

# 값 꺼내기 : 인덱스연산자 or get 메소드 사용
print(dic['name'])
print(dic.get('age'))

# 특정키가 포함되어 있는지 확인
print('name' in dic)
print('aaa' in dic)


#데이터 삭제
del dic['name']
print(dic)

# 식별자란? 자료구조에서 데이터를 구분하는 요소
# 데이터를 구분하는 중복되지 않는 고유한 값
# 리스트와 튜플은 인덱스
# 딕셔너리는 키
# 데이터베이스의 테이블은 PK

# 학생 목록 딕셔너리 생성
students = {1:'둘리',2:'도우너',3:'또치'}
# 학생추가
# 키값은 중복 안됨
# 대괄호 안 인덱스 아님
students[4] = '고길동'
print(students)
# 학생 삭제
del students[1]
print(students)