# guess-the-number
import random
from random import randint
from art import logo



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
            # return代表直接結束
        elif guess != answer:
            print("Guess again.")


game()




























# Scope (不建議將global與local變數取相同的名字！）

    # enemies = 1
    #
    # def increase_enemies():
    #   enemies = 2
    #   print(f"enemies inside function: {enemies}")
    #
    # increase_enemies()
    # print(f"enemies outside function: {enemies}")
    #
    #
 # Local Scope 在function內定義的變數，只有該function內可以使用
    # def drink_position():
    #     position_strength = 2
    #     print(position_strength)
    #
    # drink_position()
    # print(position_strength)
    # #會出現error，顯示position_strength尚未被定義


# Global Scope 在code頂層定義的變數，代表整段code皆可使用
    # player_health = 10
    # #代表在任何地方都可使用
    # def drink_position():
    #     potion_strength = 2
    #     print(player_health)
    #
    # drink_position(player_health)
    # #會出現10，

# there is no block scope (if/else/for/while code block的條件內設下的變數，皆為縮排前同階

    # game_level = 3
    # enemies = ["skeleton", "Zombie", "Alien"]
    # if game_level < 5:
    #     new_enemy = enemies[0]
    #     #即使在if範圍內設定新參數，在if同階下的code皆可以使用
    # print(new_enemy)
    #
    # game_level = 3
    # def create_enemy():
    #     enemies = ["skeleton", "Zombie", "Alien"]
    #     if game_level < 5:
    #         new_enemy = enemies[0]
    #         #因目前在function，只能在create_enemy()使用ew_enemy
    #     print(new_enemy)


# Modifying Global scope 如何在local scope內修改global scope
enemies = 1
#global scope

# 不建議直接在local內變更global參數！！
    # def increase_enemies():
    #     global enemies
    #     #需在local的範圍內，將global變數定義出
    #     enemies += 1
    #     #便可在local scope修改global的值，但修改後的值一樣只能用在local
    #     print(f"enemies inside function: {enemies}")
    #
    # increase_enemies()
    # print(f"enemies outside function: {enemies}")

# 用return的方式改變global
    # def increase_enemies():
    #     print(f"enemies inside function: {enemies}")
    #     return enemies + 1
    #
    # increase_enemies()
    # print(f"enemies outside function: {enemies}")


# global constants (命名全大寫) 全區變數，適用於定義後再也不會改變的變數
    # PI = 3.14159


