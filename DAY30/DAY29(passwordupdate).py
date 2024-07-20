from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #運用List[new_item for item in range(nr_letters)]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
                                                        #產生特定範圍的參數
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    #隨機排列組合

    password = "".join(password_list)
                    #join= 用""內的東西，連結list的每個參數
    password_entry.insert(0, password)
                    #更新password_entry的文字
    pyperclip.copy(password)
    #自動複製功能(放入要複製的參數)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    #get 調用entry的data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    #設定確認的彈跳視窗(messagebox)
    if len(website) == 0 or len(password) == 0:
        #如果有欄位沒輸入(文字長度=0)的話
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
                   #showinfo只會出現標題與文字
    else:
        try:
            #嘗試打開file
            with open("data.json", "r") as data_file:
                #read
                data = json.load(data_file)
                        #type會是dict
        except FileNotFoundError:
            #若找不到file
            with open("data.json", "w") as data_file:
                #則將資料寫進json
                json.dump(new_data, data_file, indent=4)
                    #json.update(新數據，寫進data_file，設定縮排格數)
        else:
            #若file存在
            data.update(new_data)
                #將data這個參數，用new_data的dict進行更新

            with open("data.json", "w") as data_file:
                #並將new_data的dict。轉成json儲存到file)
                json.dump(data, data_file, indent=4)

        finally:
            #不管如何都要刪除entry上的文字
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        #開啟file
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        #若找不到file
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        #若有找到file
        if website in data:
            email = data[website]["email"]
                         #找到輸入的website的email
            password = data[website]["password"]
                        #找到輸入的website的password
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                #創立訊息視窗，顯示相關數據
        else:
            #若有file但沒有輸入的website
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

#設定視窗
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#設定logo背景
canvas = Canvas(height=200, width=200)
#匯入圖片
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#輸入
website_entry = Entry(width=28)
website_entry.grid(row=1, column=1)
                                    #橫跨幾個格子（EG columnspan=2 == 從column1(中間設定) 到column2
website_entry.focus()
            #輸入框出現打字符號
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
            #預設文字(可更改):index=起始點 0等於在最前面; END = 在文字最後顯示打字符號
password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)


# Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()