#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
total_money = bill + bill * (tip / 100)
Each_people_money = total_money / people
Each_people = "{:.2f}".format(Each_people_money)

print(f"Each person should pay: ${Each_people}")

# Each_people_money = round(total_money / people,2) 四捨五入到小數第二位，但如果為0不會出現
# Each_people = "{:.2f}".format(Each_people_money) 強制顯示小數第二位


#data types
#print(type(num_char))  用於檢視參數的類型
#str(mun_char) 可轉換參數的類型為字串 #int(mun_char) #float(mun_char)

  #String = "hello" "引號內的皆是字串，無法進行運算"
    #print("hello"[0])  程式皆由0開始，因此運行後會得到"h"  print("hello"[4])

  #Integer (整數) = int
    #print(123456) =print(123_456) 下底線程式會忽略，只是方便閱讀

  #Float (小數)
    #3.14159

  #Boolean
    #True
    #False

#-----------------------------------------------

#len() 只能處理string

#串聯規則-----------------------------------------------
# num_char = len(input("what is your name"))
# print("your name has" + num_char + " characters.") 會失敗，因為只有str可以進行串聯 (num_char 非字串)

# num_char = len(input("what is your name\n"))
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " characters.") 成功

# a = float(123)
#print(70 + float("100.5")) = 170.5

#a = str(123)
#print(70 + str("100.5")) = 70100.5

#運算-----------------------------------------------
# 3 + 5 加
# 7 - 4 減
# 3 * 2 乘
# 6 / 3 除 不論是否整除 皆為float
# 2 ** 3 次方 =2*2*2

#優先度 (PEMDAS) 由左到右LR = PEMDASLR
  # Parentheses    括號 ()
  # Exponents      指數 **
  # Multiplication 乘法  *   # Division       除法  /
  # Addition       加法  +   # Subtraction    減法  -

# print(3 * 3 + 3 / 3 - 3) = Step1. 3 * 3 step2. 3 / 3 step3. 9 + 1 - 3 = 7
# print(3 * (3 + 3) / 3 - 3) = 3

#運算-四捨五入-----------------------------------------------
# print(round( 8 / 3 )) 四捨五入
# print(round( 8 / 3, 2)) 取到小數第二位
# print(8 // 3) = int

# result = 4 / 2
# result /=2 (= result / 2) += -= *= /=
# print(result)) = 4 /2 /2 -1

#f-string{可以直接將不同type轉成string，用大括弧}-----------------------------------------------
# score = 0
# height = 1.8
# inwinning = True
#
# print("your score is " + str(score))
#
# print(f"your score is {score}, your height is {height}, your are winning is {inwinning}")






