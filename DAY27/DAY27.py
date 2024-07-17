# Mile to Kilometer Converter
from tkinter import *


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300,height=150)
window.config(pady=30)


def button_clicked():
    new_text = round(int(input.get()) * 1.609,2)
    answer.config(text=new_text)
    #answer.config(text=f"{new_text}")




#設定Mile位置
Miles = Label(text=" Miles")
Miles.grid(column=2,row=0)


#設定is equal to位置
is_equal_to = Label(text="is equal to",width=20)
is_equal_to.grid(column=0,row=1)

#設定km位置
km = Label(text="Km")
km.grid(column=2,row=1)

#設定answer位置
answer = Label(text="0")
answer.grid(column=1,row=1)

#input mile位置

input = Entry(width=10)
input.get()
input.grid(column=1,row=0)


#設定Button

button = Button(text = "Calculate",command=button_clicked)
                                    #下指令
button.grid(column=1,row=2)





window.mainloop()


# # TKinter
# # import tkinter
# # =
# from tkinter import *
#                     #*代表導入每一個Class，就可以省去 tkinter.Tk() 的tkinter.
#
#
# #定義button作用
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     #新的文字為輸入框內輸入的字
#     my_label.config(text=new_text)
#     #點擊後改變label
#
#
# window = Tk()
# #建立畫面
# window.title("my first gui program")
# window.minsize(width=500,height=300)
# #相關設定
# window.config(padx=20,pady=20)
# #設定整個視窗的周圍留白處
#
#
# #設定label
# my_label = Label(text="I am a label",font=("Arial",24,"bold"))
# my_label.config(text = "new Text")
# # my_label.pack()
# ##讓label顯示在畫面上。沒有pack就不會出現。()預設字中，()內可設定位置，如(side="left")
# # my_label.place(x=100,y=200)
# # #使用place 設定精準的XY顯示位置
# my_label.grid(column=0,row=0)
# #Grid為相對位置，只有一個項目的時候(column=0,row=0) =(column=5,row=5)
# my_label.config(padx=20,pady=20)
# #設定單項的周圍留白處
#
# #Button
#
# # 設定button位置
# button = Button(text = "click me",command=button_clicked)
#                                     #下指令
# # button.pack()
# # #讓button顯示在畫面上。沒有pack就不會出現。()預設字中，()內可設定位置
# button.grid(column=1,row=1)
#
# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)
#
#
# #Entry (輸入)
#
# input = Entry(width=10)
#         #輸入框
# input.get()
#         #回傳輸入的文字type=str
# input.grid(column=3,row=2)




# TK類型（不可混用）
    #Pack 一般都是從頂部開始，依序往下。無法自訂位置
    #Place 可精準定位，缺點是每個都必須要設定X,Y軸
    #Grid 網格管理(用行列，從0起算)，為相對位置




# Label修改

    # my_label["text"] = "new text"
    # #當成dict修改值
    # my_label.config(text = "new Text")
    # #也可以直接使用config修改 (兩者相同)



#Entry
    # entry = Entry(width=30)
    # #Add some text to begin with(初始文字，可更改，END代表非預設，不用顯示)
    # entry.insert(END, string="Some text to begin with.")
    # #Gets text in entry
    # print(entry.get())
    # entry.pack()



# text entry
    # text = Text(height=5, width=30)
    # #Puts cursor in textbox.(提示打字區)
    # text.focus()
    # #Adds some text to begin with.
    # text.insert(END, "Example of multi-line text entry.")
    # #Get's current value in textbox at line 1, character 0
    # print(text.get("1.0", END))
    # text.pack()



#spinbox (可點擊上下修改數據，會記錄所有點擊的數據)
    # def spinbox_used():
    #     #gets the current value in spinbox.
    #     print(spinbox.get())
    # spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
    # spinbox.pack()


#scale(上下滑動軸，會記錄所有移動到的數據)
    # #Called with current scale value.
    # def scale_used(value):
    #     print(value)
    # scale = Scale(from_=0, to=100, command=scale_used)
    # scale.pack()


#checkbox
    # def checkbutton_used():
    #     #Prints 1 if On button checked, otherwise 0.
    #     print(checked_state.get())
    # #variable to hold on to checked state, 0 is off, 1 is on.
    # checked_state = IntVar()
    # checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
    # checked_state.get()
    # checkbutton.pack()


# #radiobutton(單選框)
    # def radio_used():
    #     print(radio_state.get())
    # #Variable to hold on to which radio button value is checked.
    # radio_state = IntVar()
    # radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
    # radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
    # radiobutton1.pack()
    # radiobutton2.pack()


# #listbox
    # def listbox_used(event):
    #     # Gets current selection from listbox
    #     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
    # fruits = ["Apple", "Pear", "Orange", "Banana"]
    # for item in fruits:
    #     listbox.insert(fruits.index(item), item)
    # listbox.bind("<<ListboxSelect>>", listbox_used)
    # listbox.pack()
    # window.mainloop()


# window.mainloop()
# #讓螢幕留在畫面上，必放最後








# Unlimited Arguments

    #原本只能加兩個
        # def add(n1,n2):
        #     return n1 + n2

    #使用*args(*=可以適用任何參數)

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

    #使用**kwargs 變成dict形式
        # def calculate(**kwargs):
                # n代表起始值，kwargs代表dict

        #印出dict
        # print(kwargs)

        # 使用dict looop
        # for key,value in kwargs.items():
        #     print(key)
        #     print(value)

        # 只印出其中一個dict
        # print(kwargs["add"])

        # print(calculate(add=3, multiply=5))

    #使用**kwargs 進行運算
        # def calculate(n, **kwargs):

        # n代表起始值，kwargs代表dict
        # print(kwargs)
        # n += kwargs["add"]
        # n *= kwargs["multiply"]
        # print(n)

        # calculate(2, add=3, multiply=5)
        # # n=2先加3，得5再*5=25


#創造Class 運用**kw
    # class Car:
    #
    #     def __init__(self, **kw):
    #         # self.model = kw["model"]
    #         self.model = kw.get("model")
    #         # 使用get，即便dict內沒有對應的數據，不會error，只會回傳none
    #         self.make = kw.get("make")
    #         self.color = kw.get("color")
    #         self.seats = kw.get("seats")
    #
    #
    # my_car = Car(make="Nissan", model="GT-R")
    # print(my_car.model)
    # print(my_car.make)



