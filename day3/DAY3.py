print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#print("Welcome to Treasure Island.")
#print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


print("歡迎來到傳說中的寶藏島")
print("你的任務是尋找到藏在此處的寶藏")
mission1 = input("在旅途的開始，請問你要往左邊?還是右邊?\n")
if mission1 == "left"
    mission2 = input("你來到一條湍急的河流旁，請問要游泳渡河?還是原地等待?\n")
    if mission2 == "wait" or mission2 == "waiting":
        mission3 = input("過了一陣子後，河水退潮，你順利渡河，來到高聳的城堡前。在你面前有藍色、紅色、黃色的門，你選哪一道?\n")
        if mission3 == "yellow" or mission3 == "yellow color":
            print("你順利來到城堡的寶藏庫，找到了傳說中海盜留下的黃金。回家後成為億萬富翁，幸福的過一輩子！")
        elif mission3 == "blue" or mission3 == "blue color":
            print("你進門後觸發陷阱，被牆上射出的箭，萬箭穿身而死。(Game over)")
        else:
            print("你進門後觸發地板陷阱，從地板掉落至城堡地底深處摔死。(Game over)")
    else:
        print("你的體力不足以過河，沉入河中溺死。(Game over)")
else:
    print("你誤入熔岩區，被火燒死。(Game over)")


#老師版本
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")




















# Ccondition(if and else 必同時出現)------------------------------
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
#
# if height >= 120: (縮排後的內容皆代表他符合此條件(>=120)後的處理)
#     print("You can ride the rollercoaster")
# else: (縮排後的內容皆代表他符合此條件(<120)後的處理)
#     print("Sorry, You have to grow taller before you can ride")

# 運算符號 >大於 <小於 >= (需靠在一起) <= 小於等於 == 等於 != 不等於 a % 2 = 0 (代表雙數 a / 2 = 0 ) a % 2 != 0 代表單數(顯示的數字為a / 2 後的餘數)
# = 代表要把=右邊的參數分配給左邊的， == 代表=左右邊需一致


# Nested if / else (在條件內在加條件) 若有多層條件 if(第一層條件) / elif(中間層可一直加) / else(皆不符合上述條件時)------------------------
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("please pay $5.")
#     elif age <=18:
#         print("please pay $7.")
#     elif age <22:
#         print("please pay $10.")
#     else:
#         print("please pay $12.")
# else:
#     print("Sorry, You have to grow taller before you can ride")


# Mutiple if (在各分支後加一個相同的條件，與各分支縮排相同即可)---------------------------------------------------------
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <=18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your finall bill is ${bill}")
#
# else:
#     print("Sorry, You have to grow taller before you can ride")


# Logical Operators(and (兩者皆成立為true) / or (其一成立為true) / not(皆不符合為true))---------------------------

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <=18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <=55:
#         bill = 0
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your finall bill is ${bill}")
#
# else:
#     print("Sorry, You have to grow taller before you can ride")


# lower() 將string全部換成小寫---------------------------
# name1 = "ANGEL"
# print(name1.lower())

# count() 將string全部換成小寫---------------------------
# word_name1 = "anger"
# final_score_true = word_name1.count('r')  (單個字母要分開加，若放在一起則代表看那個字串出現幾次)
# print(final_score_true)


# print("The Love Calculator is calculating your score...")
# name1 = input(What is your name?)
# name2 = input(What is your name2?)
#
# combined_name = name1 + name2
# lower_name= combined_name.lower()
#
# final_score_true = lower_name.count("t") + lower_name.count("r") + lower_name.count("u") + lower_namet.count("e")
# final_score_love = lower_name.count("l") + lower_name.count("o") + lower_name.count("v") + lower_name.count("e")
#
# Love_Scores = int(str(final_score_true) + str(final_score_love))
#
# if Love_Scores < 10 or Love_Scores > 90:
#   print(f"Your score is {Love_Scores}, you go together like coke and mentos.")
# elif Love_Scores >= 40 and Love_Scores <= 50:
#   print(f"Your score is {Love_Scores}, you are alright together.")
# else:
#   print(f"Your score is {Love_Scores}.")