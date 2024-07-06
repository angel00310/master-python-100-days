#  Quiz game
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


















# 創建class (首字母一定要大寫)
    # class User:
    #     pass
    #     # 代表class 或 function下面為空
    #
    # user_1 = User()
    # user_1.id = "001"
    # user_1.username = "angela"

    # user_2 = User()
    # user_2.id = "002"
    # user_2.username = "jack"



# Constructor (initialize) 結構初始化
    # class User:
    #     def __init__(self,user_id, user_name,):
    #         # 代表每次用到user這個class時，都可以直接定義user_id,user_name
    #         self.id = user_id
    #         self.user_name = user_name
    #         self.followers = 0
    #         #若要設定預設值，可以直接在class下定義，不放在()內。在print時也可直接使用
    #
    #
    # user_1 = User("001", "angela")
    # user_2 = User("002", "jack")
    # # 使用class創建object時，如果有用init，那每次在創建object時都必需定義
    #
    # print(user_1.id)
    # print(user_1.followers)


# 創建method (class的function)
    # class User:
    #     def __init__(self,user_id, user_name,):
    #         # 代表每次用到user這個class時，都可以直接定義user_id,user_name
    #         self.id = user_id
    #         self.user_name = user_name
    #         self.followers = 0
    #         self.followering = 0
    #         #若要設定預設值，可以直接在class下定義，不放在()內。在print時也可直接使用
    #
    #     def follow(self, user):
    #         user.followers += 1
    #         self.followering += 1
    # #
    # user_1 = User("001", "angela")
    # user_2 = User("002", "jack")
    #
    # user_1.follow(user_2)
    # #使用class 的follow的 method
    #
    # print(user_1.followers)
    # print(user_1.followering)
    # print(user_2.followers)
    # print(user_2.followering)