# calculate
from replit import clear
from art import logo
print(logo)

#Addition
def add(n1, n2):
    return int(n1) + int(n2)

# Subtraction
def subtraction(n1, n2):
    return int(n1) - int(n2)

# Division
def division(n1, n2):
    return int(n1) / int(n2)

# Multiplication
def multiply(n1, n2):
    return int(n1) * int(n2)

# dictionary
operations = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": division
}

operaction_finished = False

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while not operaction_finished:
        operaction_symbol = input("Pick an operaction: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operaction_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operaction_symbol} {num2} = {answer}")
    # continue
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = True
            clear()
            calculator()
            #務必注意須設定條件才能使用自己

calculator()





# Function
    # def my_function():
        # do this
        # then do this
        # finally do this

# Function with input
    # def my_function(something): 在每個動作內都加上 something
        # do this with something
        # then do this
        # finally do this

# Function with Output ,運行此函數時，會被result取代
    # def my_function():
        # result = 3*2
        # return result
        # finally do this

    # def format_name(f_name, l_name):
    #     formated_f_name = f_name.title()
    #     formated_l_name = l_name.title()
    #     print(f"{formated_f_name} {formated_l_name}")  # result = formated_f_name
    #
    # format_name("angel", "WANG")

#上下相同
    # def format_name(f_name, l_name):
    #     formated_f_name = f_name.title()
    #     formated_l_name = l_name.title()
    #     return f"{formated_f_name} {formated_l_name}"
    #
    # print(format_name("angel", "WANG"))


# 不可能有多個return，除非是條件式
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide vailid inputs."
#         formated_f_name = f_name.title()
#         formated_l_name = l_name.title()
#         return f"{formated_f_name} {formated_l_name}"
#         # print("this is print") -> 在return後的永遠不會出現
#         print(format_name(input("What is your first name? "),input("What is your last name? ")


# Docstings function的說明文字。需要再Function的下一行 """ content """ 可以斷行並且多行 (滑鼠移到該FUNCTION就會顯示說明文字)

#already uesd functions with outputs.
# length = len(formatted_name)

# return as an early exit
# def format_name(f_name, l_name):
#     """Take a first and last name and format it
#     to return the title case version of the name."""
#
#     if f_name == "" or l_name == "":
#         return "You didn't provide vailid inputs."
#         formated_f_name = f_name.title()
#         formated_l_name = l_name.title()
#         return f"{formated_f_name} {formated_l_name}"
#         # print("this is print") -> 在return後的永遠不會出現
#         print(format_name(input("What is your first name? "),input("What is your last name? ")
#



