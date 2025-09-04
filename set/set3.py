# set 의 교집합, 합집합, 차집합 함수

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

# 두 세트의 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s2 - s1)
