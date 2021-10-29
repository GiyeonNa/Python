kor = ["사과","바나나","오렌지"]
eng = ["apple","banana","orange"]

print(list(zip(kor, eng)))

mix =[('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

print(list(zip(*mix))) #*로 분리

kor2 , eng2 = zip(*mix)

print(kor2)
print(eng2)
