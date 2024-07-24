from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    #DAY17

    def __init__(self, quiz_brain: QuizBrain):
                                    #quiz_brain的DATA_TYPE 是QuizBrain 這個CLASS
        self.quiz = quiz_brain
                    #最初的問題

        #建立視窗
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #score
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        #中間區塊(問題顯示區)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            #X (300/2)
            125,
            #Y (250/2)
            width=280,
            #文字會自動斷行不超過此範圍
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        #true button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        #false button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        #啟用顯示問題的function

        #運行(如果有此loop就不能用其他的loop (while / for)
        self.window.mainloop()

    #抓取quiz_brain的next question
    def get_next_question(self):
        self.canvas.config(bg="white")
                                 #每次都重製背景為白色
        #確認題目是否還有
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
                                                        #調用quiz_brain的score function
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        #如果沒有
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
                                        #禁用按鈕
            self.false_button.config(state="disabled")

    #true function
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
                                #調用quiz_brain的check_answer function，如果結果是True

    # false function
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
                            #分兩行呈現

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
                                #延遲一秒後  執行此function
