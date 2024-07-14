# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER ="[name]"

# readines 將所有行用LIST回傳
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()



#replace 將指定的短語取代成其他文字

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # strip 刪除所有空白，只留下文字
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
                                             #(舊的文字  ,  新的文字)

        #將每封信都創建新的文件
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as complete_letters:
            complete_letters.write(new_letter)














# Python製作File (預設的mode僅有讀的功能，即mode="r")
    # file = open("my_file")
    # contents = file.read()
    # print(contents)
    # 手動關掉file避免佔資源
    # file.close()

# 另一個開啟方式(無須設定手動關file，完成後會自動關閉)
    # with open("my_file") as file:
    #     contents = file.read()
    #     print(contents)


#寫(全部取代)
    # with open("my_file", mode="w") as file:
    #     file.write("New test")
    #     #會將文件內的所有內容刪掉，改成新write的內容

#寫(既有內容追加)
    # with open("my_file", mode="a") as file:
    #     file.write("\nNew test")
    #     #在既有功能，追加新write的內容

#創建完全不存在的file，一樣用mode="w"，系統會自動創建
    # with open("New_file", mode="w") as file:
    #     file.write("New test")

#看day20 的運用




# File Path
    #/Root/work/report.doc
    #/root/work/project/talk.doc

# Absolute File Path (絕對路徑，使用/分割)
    # /work/project/talk.ppt

# Relative File Path (相對路徑，在當下的資料夾起算，使用./開頭
    #若往下(若在project)
        # ./talk.ppt = talk.ppt (./可省略)

    #若往上(若在project)
    # ../report.doc

#若不再同一層，如何引用Absolute File Path
    # with open("C:/Users/A8303/OneDrive/桌面/my_file") as file:
    #         contents = file.read()
    #         print(contents)

#若不再同一層，如何引用Relative File Path
    # with open("../../my_file") as file:
    #     contents = file.read()
    #     print(contents)