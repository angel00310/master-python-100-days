# 1. logo
import replit

from art import logo
from art import vs
from game_data import data
import random
from replit import clear


# 2.從date隨機取出一個名字
def random_account():
    return random.choice(data)


# 3.改變呈現方式
def describe_date(account):
    people = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{people}, a {description}, from {country}"


# 4.比較追蹤者數量
def check_win(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

# 5.開始遊戲


def game():
    print(logo)
    score = 0
    game_continue = True
    account_A = random_account()
    account_B = random_account()

    while game_continue:
        account_A = account_B
        account_B = random_account()

        #避免重複
        while account_A == account_B:
            account_B = random_account()

        compare_a = describe_date(account_A)
        compare_b = describe_date(account_B)
        print(f"Compare A: {compare_a}.")
        print(vs)
        print(f"Against B: {compare_b}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_A["follower_count"]
        b_follower_count = account_B["follower_count"]
        is_win = check_win(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_win:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")






game()