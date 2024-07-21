from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


# ---------------------------- 檢驗 ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
            # 將csv用pandas讀取
except FileNotFoundError:
        #若沒有找到file
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
                #將list轉成dict        類型= {KEY:value}
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- function ------------------------------- #
#變換字卡
def next_card():
    global current_card, flip_timer
                            #全區域參數
    window.after_cancel(flip_timer)
    #每次使用次function，倒數機制就要取消重新計算
    current_card = random.choice(to_learn)

    #改變標題與word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    #延遲，三秒後將背景圖由背面改為正面
    flip_timer = window.after(3000, func=flip_card)


#顯示英文字卡(背面)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
                                        #找出current_card的value
    canvas.itemconfig(card_background, image=card_back_img)
                        #將背景圖改為背面


#若是已知的字，就剃除在list內
def is_known():
    to_learn.remove(current_card)
    #將current_card從list內剔除
    print(len(to_learn))
    #紀錄剩餘單字數

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # 將剩餘單字重新記錄起來   #儲存路徑                   #取消自動增加的索引
    next_card()


# ---------------------------- UI ------------------------------- #

#建立視窗
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#設定延遲功能
flip_timer = window.after(3000, func=flip_card)
                            #顯示三秒後，調用flip_card的function


#建立中間區塊
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
                                                                        #斜體
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
                                                                        #粗體
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#wrong button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

#right button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

#啟動程式就顯示字卡
next_card()


window.mainloop()