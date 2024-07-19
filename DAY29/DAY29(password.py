from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip



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

    #設定確認的彈跳視窗(messagebox)
    if len(website) == 0 or len(password) == 0:
        #如果有欄位沒輸入(文字長度=0)的話
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
                   #showinfo只會出現標題與文字
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
                            # askokcancel 會出現OK = TRUE /cancel = FALSE按鈕
        if is_ok:
            #創建文件，a=append擴充
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                #創建完文件後，使用delete 刪除entry輸入的文字，從0=頭,到END=最後
                website_entry.delete(0, END)
                password_entry.delete(0, END)

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
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
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
generate_password_button = Button(width=15,text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()