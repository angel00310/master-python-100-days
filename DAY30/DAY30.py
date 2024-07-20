#FileNotFoundError
    # with open("a_file.txt") as file:
    #     file.read()
import json

#KeyError
    # a_dictionary = {"key": "value"}
    # value = a_dictionary["non_key"]

#IndexError
    # fruit_list = ["apple", "banana", "pear"]
    # fruit = fruit_list[3]

#TypeError
    # text = "abc"
    # print(text + 5)



#Catching Exceptions

    #try (嘗試若發生甚麼事件)

        # try:
        #     file = open("a_file.txt")
        #     a_dictionary = {"key": "value"}
        #     print(a_dictionary["abc"])
    #except (若TRY出錯，要做甚麼其他動作，但須明確定義是甚麼錯(第一part)！)
        # except FileNotFoundError:
        #         #若發生FileNotFoundError時執行以下動作，但若有其他error系統仍會跳錯
        #     file = open("a_file.txt","w")
        #     file.write("something")
        #     #若找不到a_file.txt，就直接創一個

        # except KeyError:
        #         #若KEY不存在
        #     print("not key")

    #except進階
        # except KeyError as error_message:
        #                     #將KeyError的原因印出
        #     print(f"The key {error_message} does not exist")

    #else (若try的設想不成立，永遠不會到else，會先到except。當try成立，才會到else)
        # else:
        #     content = file.read()
        #     print(content)

    #finally(無論如何皆會運行)
        # finally:
        #     file.close()
        #     print("File was closed")




#Raising your own Except (創造不存在的error = raise xxxError("") ->(內可定義要出現文字訊息)
    # height = float(input("Height: "))
    # weight = int(input("Weight: "))
    #
    # if height > 3:
    #     raise ValueError("Human Height should not be over 3 meters")
            #創造特殊的Error類型
    #
    # bmi = weight / height ** 2
    # print(bmi)



    # try:
    #     file = open("a_file.txt")
    #     a_dictionary = {"key": "value"}
    #     print(a_dictionary["abc"])
    #
    # except FileNotFoundError:
    #     file = open("a_file.txt","w")
    #     file.write("something")
    #
    # except KeyError as error_message:
    #     print(f"The key {error_message} does not exist")
    #
    # else:
    #     content = file.read()
    #     print(content)
    #
    # finally:
    #     raise TypeError("this is an an error that i made up")



#JSON
    # json.dump()
        # = write
    # json.load()
        # = read
    # json.update()
        # = update