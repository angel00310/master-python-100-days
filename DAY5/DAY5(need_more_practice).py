#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# easy level  (如果變數用不到 可用_代表
# password = ""
# # nr_letters = 4 mean 1-4
# for _ in range(1, nr_letters + 1):
#   password += random.choice(letters)
#
# for _ in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
#
# for _ in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
#
# print(password)


# hard level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")



# loop (for A(參數名) in B(list))循環----------------------------
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie") 在每個變數後加上 pie
#     print(fruits) 有幾個變數，就會重複幾次的list


# For Loop with Range--------------------------------------------------------
# for number in range(1,10): 在1到10之間所有數字(不包含10) 代表執行幾次。
#     print(number)
#
# for number in range(1, 10, 3): 在1到10之間所有數字(不包含10)，每三個呈現一次
#     print(number)

# total = 0  如何算出1~100的加總
# for number in range(1,101):
#     total += number 執行100次
# print(total)

# target = int(input()) # Number between 0 and 1000
# Your code here 👇
# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

