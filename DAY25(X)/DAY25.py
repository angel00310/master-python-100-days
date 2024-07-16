import pandas

#U.S States Game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#使用圖片當形狀

#計算圖片上的每個X,Y值的位置
    # def get_mouse_click_coor(x,y):
    #     print(x,y)
    # turtle.onscreenclick(get_mouse_click_coor)
    # turtle.mainloop()



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
#50州的實際名單
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
                                    #title為視窗名稱，prompt為提示文字         #固定讓第一個字母大寫，其他小寫
    #退出遊戲
    # if answer_state == "Exit":
    #     missing_states = []
    #     #只創建沒猜中的州列表
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #     new_data = pandas.DataFrame(missing_states)
    #     new_data.to_csv("states_to_learn.csv")
    #     break

    #使用DAY21 的概念
    missing_states = [state for state in all_states if state not in guessed_states ]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break




    # 確認輸入的文字在50州內
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #擴充猜的List
        t = turtle.Turtle()
        #創造一隻烏龜，讓文字到正確的地圖上
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
                            #確認輸入州包含在50州內
        t.goto(state_data.x.item(), state_data.y.item())
                            #item代表只抓取原始數據(X,Y)
        t.write(answer_state)
        #只顯示輸入的文字





screen.exitonclick()







#松鼠挑戰
    # data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240715.csv")
    # grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
    # red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    # black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
    # print(grey_squirrels_count)
    # print(red_squirrels_count)
    # print(black_squirrels_count)
    #
    # data_dict = {
    #     "Fur Color": ["Gray", "Cinnamon", "Black"],
    #     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
    # }
    #
    # df = pandas.DataFrame(data_dict)
    # df.to_csv("squirrel_count.csv")









#一般開啟
    # with open("weather_data.csv") as data_file:
    #     data = data_file.readline()
    #     print(data)


#import csv
    # import csv
    #
    # with open("weather_data.csv") as data_file:
    #     data = csv.reader(data_file)
    #     temperatures = []
    #     for row in data:
    #         if row[1] != "temp":
    #             temperatures.append(row[1])
    #
    #     print(temperatures)


#Pandas

    # import pandas
    # pandas.read_csv("weather_data.csv")
    # print(data["temp"])


#整個CSV檔是一個data frame，每一列則是series

    # import pandas
    # data = pandas.read_csv("weather_data.csv")
    # # print(type(data))
    # # print(type(data["temp"]))
    #
    # data_dict = data.to_dict()
    # print(data_dict)
    #
    # temp_list =  data["temp"].to_list()
    # print(len(temp_list))
    #
    # print(data["temp"].mean())
    # #算出溫度的平均數
    #
    # print(data["temp"].max())
    # #找出最大值



#Get Data in columns (使用列的名稱)
    # print(data["condition"])
    # print(data.condition)


#Get Data in Row
    # import pandas
    # data = pandas.read_csv("weather_data.csv")
    # print(data[data.day == "Monday"])

#找出最熱的數據
    # print(data[data.temp == data.temp.max()])

#
    # monday = data[data.day == "Monday"]
    # print(monday.condition)


#將星期一的溫度轉化成華氏
    # monday = data[data.day == "Monday"]
    # monday_temp = monday.temp[0]
    # monday_temp_F = monday_temp *9/5 +32
    # print(monday_temp_F)


#Create a dataframe 直接創建CSV
    # data_dict = {
    #     "students":["Amy","James","Angela"],
    #     "score":[76,56,65]
    # }
    #
    # data = pandas.DataFrame(data_dict)
    # data.to_csv("new_data.csv")

