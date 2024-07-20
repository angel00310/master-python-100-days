# NATI Alphabet project
# new_dict = {"ney_key": "new_value" for "item" in "list"}
# new_dict = {"ney_key": "new_value" for ("key,value") in "dict.item()"}
# new_dict = {"ney_key": "new_value" for ("key,value") in "dict.item()" if "test"}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#["new_item" for "item" in "list"]

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)



# DAY30 的更新

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        #執行此行
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        #若發生keyError
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
        #重新執行
    else:
        print(output_list)
        #若符合則印出output_list

generate_phonetic()







#List Comprehension (不只能用LIST 也能用string range tueple)
    #舊的方式
    # numbers = [1,2,3]
    # new_list = []
    # for n in list:
    #     add_1 = n + 1
    # new_list.append(add_1)


    # 新的方式 new_list = ["new_item" for "item" in "list"] ""內進行更換
    # numbers = [1,2,3]
    # new_list = [ n + 1 for n in numbers]


    # range_list = [ num * 2 for num in range(1,5) ]

# Conditional List Comprehension :  new_list = ["new_item" for "item" in "list" if "test"] 當test為True更新至list
    # names = ["Alex", "Beth", "Caroline", "Dave" , "Elanor", "Freddie"]
    #
    # short_names = [name for name in names if len(name)< 5]
    # #只有字母小於5的名字，才會加到list中
    #
    # long_names = [name.upper() for name in names if len(name) > 5]
    # #只有字母大於5的名字，才會加到list中，且全大寫


# Dictionary Comprehension :
    # new_dict = {"ney_key": "new_value" for "item" in "list"}
    # new_dict = {"ney_key": "new_value" for ("key,value") in "dict.item()"}
    # new_dict = {"ney_key": "new_value" for ("key,value") in "dict.item()" if "test"}

    # names = ["Alex", "Beth", "Caroline", "Dave" , "Elanor", "Freddie"]
    # import random
    # student_score = {student: random.randint(1,100) for student in names}
    #
    # #用dict進行loop
    # passed_students = {student: score for (student,score) in student_score.items() if score >= 60}


#Pandas DataFrame

student_dict = {
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}


#loop in dict
    # for (key,value) in student_dict.items():
    #     print(value)

#pandas

    # import pandas
    #
    # student_data_frame = pandas.DataFrame(student_dict)
    # print(student_data_frame)
    #
    # #loop through row of a data frame
    # for (index,row) in student_data_frame.iterrows():
    #     print(index)
    #     #印索引
    #     print(row)
    #     #印所有行
    #     print(row.student)
    #     print(row.score)
    #     if row.student == "Angela":
    #         print(row.score)
    #     #印特定item