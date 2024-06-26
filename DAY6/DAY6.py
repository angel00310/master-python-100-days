def turn_rignt():
    turn_left()
    turn_left()
    turn_left()

def right_walking():
    turn_rignt()
    move()


while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_on_right():
        move()
    elif wall_in_front() and right_is_clear():
        right_walking()
    elif right_is_clear():
        right_walking()
    else:
        move()

# or
#
# while not at_goal():
#     elif right_is_clear():
#         right_walking()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


#day 15再回來

# 自定義funtions https://docs.python.org/3/library/functions.html-----
# print("hello")
# num_char = len("hello")
# print(num_char)

# step1 defining function
# def my_function():
#     print("hello")
#     print("bye")

#step2 calling function (使用function)
# my_function()



# indentation(縮排) code block(4 space)-----------------------------------------------------------




# for roop ---------------------------------------------

# for item in list
#     do something to each item (對清單內的每個項目做一樣的事)

# for number in range(a,b)
#     print(number)
#     在某個範圍內(a~b-1)的範圍內，對每個數字做操作

# for _ in range(n)
#     執行幾次以下動作


# while roop (當條件為true時，roop該動作，直到false)---------------------------------------------
# while something_is_true:
#     do this
#     then do this
#     then do this

# def turn_rignt():
#     turn_left()
#     turn_left()
#     turn_left()
# def cross():
#     move()
#     turn_left()
#     move()
#     turn_rignt()
#     move()
#     turn_rignt()
#     move()
#     turn_left()

# num_of_hurdles = 6
# while num_of_hurdles >0:
#     cross()
#     num_of_hurdles -= 1
#     print(num_of_hurdles)

# while roop setting (當條件為true時，roop該動作，直到false)---------------------------------------------

# while at_goal() != True:
#     cross()

#     the same

# while not at_goal():
#     cross()

