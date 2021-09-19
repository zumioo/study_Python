class Student:
    def __init__(self,name): #インスタンス化する際に引数として持ってくることで、初期値として登録可能
        self.name = name


    def avg(self,math,english):
        print((math + english)/2)


a001 = Student("sato") #インスタンス化
#a001.name = "sato" #アトリビュートを定義
print(a001.name)

a002 = Student("kato") 
print(a002.name)