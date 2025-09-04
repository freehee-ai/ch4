# 모듈 불러오기
# 모듈 : 특정 기능을 미리 만들어둔 파일
# 깊은 복사를 위해 모듈 불러오기

# 객체 복사하기
dic = {'name': '둘리', 'age': 20}
copy = dic.copy()

# 복사본의 내용 수정하기
# 복사본을 수정해도 원본에는 영향이 없다.
# => 완벽하게 복사되었다, 고 한다.
copy['age'] = 25
print('원본',dic)
print('복사본:', copy)

dic['hobby'] =['축구', '야구']
print(dic)
copy = dic.copy()

# 축구 -> 테니스
copy['hobby'][0] = '탁구'
# 복사본 수정 -> 원본 함께 수정 : 얕은 복사
# 리스트 -> 참조변수 : 주소값이 저장되어 있다.
print(dic)
print(copy)


