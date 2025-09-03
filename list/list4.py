# 리스트의 CRUD 함수
# 데이터 추가, 조회, 수정, 삭제

lis = [1, 2, 3]

# append : 새로운 요소를 맨 뒤에 추가
lis.append(4)
print(lis)

# 값 수정하기
lis[2] = 4
print(lis)

# 인덱스로 삭제하기
del lis[1]
print(lis)

# 값으로 삭제하기
# 같은 값이 여러개 있을 경우에는 앞에서부터 삭제됨
# 중복 값이 있을 때 remove()는 항상 첫 번째 해당 값만 삭제한다는 점을 알아두는 것이 중요합니다
# 리스트는 가변, 삭제가 있을 시 값들이 이동된다?!
lis.remove(4)
print(lis)

# 마지막 요소를 꺼내면서 삭제
last = lis.pop()
print(lis, last)

# 리스트의 크기 확인
# 파이썬 내장 함수
leng = len(lis)
print(leng)


