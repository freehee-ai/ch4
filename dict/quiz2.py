cart ={'사과':3, '바나나':5, '딸기':2}
f_cnt = sum(cart.values())
print(f_cnt)

score = {'수학': 95, '영어': 88, '국어': 100}
sum = sum(score.values())
len = len(score)
print(sum/len)

menu = {'아메리카노': 2000, '라떼': 3000, '케이크': 4500}
pay = menu['아메리카노']*2 + menu['라떼']
print(pay)