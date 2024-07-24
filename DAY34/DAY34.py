from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



#TYPE Hint(: tyoe 將參數固定一個type，當type不符時，會先出現提示，若運行會出錯)

    # age: int
    #      #: 將age固定為 int
    # name: str
    # height: float
    # is_human: bool
    #             #true or false

    # def police_check(age: int)    -> bool:
    #                  #指定age要int   #指定回傳的type一定要是bool
    #     if age > 18:
    #         can_drive = True
    #     else:
    #         can_drive = False
    #
    #     return  "twelve"
    #                  # 滑鼠一致上方，會出現錯誤提示
    #
    # if police_check("twelve"):
    #                 #滑鼠一致上方，會出現錯誤提示
    #     print("You may pass")
    # else:
    #     print("Pay a fine")