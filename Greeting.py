print("Good Morning")
print("Good afternoon")
print("Good evening")

num = 1

print(num)

num01 = 123
num02 = 1.23

print(type(num01)) #typeでデータ型を見ることができる
print(type(num02))


#bool型→trueかfalseのみの型
a = 10
b = 1 
bool01 = (a < b)

print(bool01)
print(type(bool01))


#リスト
list = ["sato", "kato", "takahashi"]
list[1] = "tanaka"
print(list[0])
print(list[1])
print(list[2])


lists = [["sato", "suzuki"],["taka", "hashi"]]
print(lists[0][0])
print(lists[0][1])
print(lists[1][0])
print(lists[1][1])



#演算子
x = 10
y = 2
z = 10

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

#関係演算子
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print(x == y)
print(x != y)

#論理演算子
xx = 8
yy = 3 

print(xx >= 5 and xx <= 10)
print(yy >= 5 and yy <= 10)

print(xx == 3 or xx == 3)
print(yy == 1 or yy == 1)
