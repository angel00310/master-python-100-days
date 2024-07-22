# birthday wish
#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import random

import pandas
import smtplib
from datetime import datetime



MY_EMAIL = "a8303103@gmail.com"
MY_PASSWORD = "rlygzdmmmznkqdkw"

#設定當天日期
today = datetime.now()
today_tuple = (today.month, today.day)

#讀取TXT
data = pandas.read_csv("birthdays.csv")
#創建dict
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
                   #key                                  value
if today_tuple in birthdays_dict:
    #當天日期        在dict內
    birthday_person = birthdays_dict[today_tuple]
                        #取得value
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
                   #範本路徑                  隨機取1~3的其一數
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
                                    #取代      舊字                 新字

#寄信
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )



#smpt 自動寄信功能
    # import smtplib
    #         #python內建
    # my_email = "a8303103@gmail.com"
    # password = "rlygzdmmmznkqdkw"
    #                 #要放Gmail的APP password
    #
    #
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #                          #設定寄信者的信箱廠商  (若使用with .... as 的方式設定，結尾就可以不用加close()，會自動關閉
    #     connection.starttls()
    #                 #傳輸加密
    #     connection.login(user=my_email,password=password)
    #                 #實際登入帳密
    #
    #     connection.sendmail(from_addr=my_email,to_addrs="A8303103@yahoo.com.tw",msg="subject:Hellow\n\n This is my hellow")
    #                             #寄件者          送達者                            訊息:  標題                內文



#date time
    # import datetime as dt
    #
    # now = dt.datetime.now()
    #     #取得當下日期時間
    #
    # year = now.year
    # month =  now.month
    #             #只取出特定，type=datetime
    # day_of_week = now.weekday()
    #                 #0=星期一；1=星期二
    #
    # date_of_birth = dt.datetime(year=1995 ,month=12 , day=15 )
    #                                                         #hour預設=0:00:00 可以不用設
    # print(date_of_birth)



#Motivation Quotes on Monday
    # import smtplib
    # import datetime as dt
    # import random
    #
    # MY_EMAIL = "a8303103@gmail.com"
    # MY_PASSWORD = "rlygzdmmmznkqdkw"
    #
    # now = dt.datetime.now()
    # weekday = now.weekday()
    # if weekday == 0:
    #     with open("quotes.txt") as quote_file:
    #         all_quotes = quote_file.readlines()
    #                         #將所有list存起來
    #         quote = random.choice(all_quotes)
    #                         #隨機取一個
    #
    #     print(quote)
    #     with smtplib.SMTP("smtp.gmail.com") as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         connection.sendmail(
    #             from_addr=MY_EMAIL,
    #             to_addrs=MY_EMAIL,
    #             msg=f"Subject:Monday Motivation\n\n{quote}"
    #         )