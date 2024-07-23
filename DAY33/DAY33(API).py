import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "a8303103@gmail.com"
MY_PASSWORD = "rlygzdmmmznkqdkw"
MY_LAT = 25.030239 # Your latitude
MY_LONG = 2281.442871 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        #若現在小時>日落 或 小於日出 ，代表是晚上
        return True

#寄信
while True:
    time.sleep(60)
    #每隔60秒執行一次
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )



#API 與對外的接口

#API Endpoint (一個url 資料的存放點)
    #eg:http://api.open-notify.org/iss-now.json


#API Requset (Python request)

    # import requests
    # response = requests.get(url="http://api.open-notify.org/iss-now.json")
    #                     #放資料的存放點
    # print(response)
    #         # = Response[200]
    # print(response.status_code)
    #         # = 200
    #
    # response_err = requests.get(url="http://api.open-notify.org/iss.json")
    # print(response_err.status_code)
    #         # = 404 網址不存在

    # type(https://www.webfx.com/web-development/glossary/http-status-codes/)
        # 1xx Informational = Hold On (繼續等待，還不是結束)
        # 2×× Success = Here You Go (一切成功，取得所需資料)
        # 3×× Redirection = Go Away (沒有權限)
        # 4×× Client Error = You Screwed Up (客戶端出錯，如404=資料不存在)
        # 5×× Server Error = I Screwed Uo (伺服器出錯、癱瘓)

#檢驗API Request
    # import requests
    # response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # response.raise_for_status()
    #     #可得到詳細的錯誤原因
    # data = response.json()["iss_position"]
    #             #變成json的dict  [放key]
    # print(data)
    #
    # data_2 = response.json()
    # longitude = data_2["iss_position"]["longitude"]
    # latitude = data_2["iss_position"]["latitude"]
    # iss_location = (longitude, latitude)
    # print(iss_location)

# API parameters API參數 (eg - https://sunrise-sunset.org/api)
    # import requests
    # from datetime import datetime
    #
    # MY_LAT = 25.030239
    # MY_LONG = 2281.442871
    #
    # parameters = {
    #     "lat": MY_LAT,
    #     "lng": MY_LONG,
    #     "formatted": 0
    # }
    #
    # response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    #                                                                     #指定參數
    # response.raise_for_status()
    # data = response.json()
    # sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    #                                         # 用""內的項目進行分割，可用.split一直分割下去(先用T分割後，取第二個項目，在第二個項目中用:分割，取第一個項目)
    # sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    # time_now =datetime.now()
    #
    # print(data)
    # print(sunrise)
    # print(sunset)
    # print(time_now.hour)
    #     # 比較小時
