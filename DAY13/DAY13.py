############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# edit
    # my_function()
    # def my_function():
    #   for i in range(1, 21):
    #     if i == 20:
    #       print("You got it")
    # my_function()

#bug = 因為range(1, 20) 不包含20，所以不會print，要改成(1,21)才會印出


# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 5)
# print(dice_imgs[dice_num])

# edit

    # from random import randint
    # dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    # dice_num = randint(0, 5)
    # print(dice_imgs[dice_num])

#因為[]第一個數為0，所以實際只對應到0~5，因此若骰到六，會出現超出list，error



# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# edit
    # year = int(input("What's your year of birth?"))
    # if year > 1980 and year < 1994:
    #   print("You are a millenial.")
    # elif year > 1994:
    #   print("You are a Gen Z.")

# if 的and 兩邊條件都要視為True。因此若要檢定1980 1994 應該要包含=



# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# edit
    # age = int(input("How old are you?"))
    # if age > 18:
    #    print(f"You can drive at age {age}.")

#1.if 的下一行須縮排 2. '>' not supported between instances of 'str' and 'int' 因此要把input變為int形式3.用f結合不同的變數型態


#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# edit
    # pages = 0
    # word_per_page = 0
    # pages = int(input("Number of pages: "))
    # print(pages)
    # word_per_page = int(input("Number of words per page: "))
    # print(word_per_page)
    # total_words = pages * word_per_page
    # print(total_words)


#用print後發現word_per_page為0，將重複的=拿掉後，得正解（原本的==代表判對左右是否相同，若不同則是為false，起始為0)



#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

# edit
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

#因為append是在roop完後才執行，因此只有加到最後一個數，只要縮排進roop的範圍即可