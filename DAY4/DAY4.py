rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

game_choice = [rock, paper, scissors]

print("user choice")
print(game_choice[user_choice])
print("computer choice")
print(game_choice[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == 2 and computer_choice == 1:
    print("You lose")
elif user_choice == computer_choice:
    print("It's a draw")













# Randomisation 隨機(python的Module。askpython.com)-------------------------------------
# import random
#
# random_integer = random.randint(1,5)
# print(random_integer)

#0.00000 - 0.999999...(隨機小數)
# random_float = random.random()
# print(random_float)
#
# #如何設定在整數間的隨機小數
# random_MIX = random_integer * random_float
# print(random_MIX)

#Module 同一個資料夾內的.py檔，只要import就可使用(分工製造)-----------------------------------------
# import test_module
# print(test_module.pi)


# list[a,b,c,d,e] 順序已固定:左到右，0開始->1代表從第一個數往右數1/-1代表最後一個數往回數(因為沒有-0)-------------------------------------------
# state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(state_of_america[1])
# print(state_of_america[-1])

# state_of_america[1] = "Pennsy" (改list的名字)
# print(state_of_america[1])

# state_of_america.append("Angelland")  (使用append，將單項目加到list的最後 https://docs.python.org/3/tutorial/datastructures.html)
# print(state_of_america)

# state_of_america.extend(["Angelland","Jackland"]) (使用extend，將多個項目加到原list的最後)
# print(state_of_america)


# len() 除了算個數外，也可以算列表的個數----------------------------------------------------------------------------------
# name = "angel"
# print(len(name))

# name_list = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
# print(len(name_list))


#Nestedlist 嵌套(在lsit內放另一組list)--------------------------------------------------------
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Celery", "Pears"]
# vegetables = ["Spinach","Kale","Tomatoes", "Celery", "Potatoes"]
# dirty_dozen =  [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])


# 查看位置的python-------------------------------------------------------------------
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)



# day4- TREASURE MAP
#
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
#
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
#
#
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")
