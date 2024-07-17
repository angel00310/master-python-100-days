# def add(*args):
#     # 可以只指向一個數
#     print(args[0])
#     # 將所有數字相加
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(3,5,6,7,8,6,1))



def calculate(n, **kwargs):
            #n代表起始值，kwargs代表dict
    print(kwargs)
    #使用dict looop
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # 使用dict looop
    #只印出其中一個dict
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
# n=2先加3，得5再*5=25


class Car:

    def __init__(self,**kw):
        # self.model = kw["model"]
        self.model = kw.get("model")
                        #使用get，即便dict內沒有對應的數據，不會error，只會回傳none
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan",model="GT-R")
print(my_car.model)
print(my_car.make)
