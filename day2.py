#条件分岐

age = 19

if age >= 20:
    print("adult")
elif age ==0:
    print("baby")
else:
    print("child")


#繰り返し

for i in range(5):
    if i == 3:
        break #処理を終了させる
    print(i)


for i in range(5):
    if i == 3:
        continue #処理をスキップさせる
    print(i)

for i in range(3):
    for j in range(3):
        print(i, j, sep="-") 


arr = [2, 4, 6, 8, 10]
for i in arr:
    print(i)

sum = 0

for i in arr:
    sum += i
    print(sum)
