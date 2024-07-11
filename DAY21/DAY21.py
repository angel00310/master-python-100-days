
#Class Inheritance (不只繼承外觀，也能繼承行為)

    # #主項目
    # class Animal:
    #     def __init__(self):
    #         self.num_eyes = 2
    #
    #     def breathe(self):
    #         print("Inhale,exhale.")
    #
    # #想繼承的子項目
    # class Fish(Animal):
    #     #(括號內放想繼承的class名稱)
    #     def __init__(self):
    #         super().__init__()
    #
    #     #繼承全部的function (使用super)
    #
    #     def breathe(self):
    #         super().breathe()
    #         #只想繼承單項的話
    #         print("doing this underwater")
    #         #可再加上其他特性
    #
    #     def swim(self):
    #         print("moving in winter.")
    #
    #
    # nemo = Fish()
    # nemo.breathe()


# snake後半 製作food、scoreboard、撞牆機制


# Slice 切片 在list, tuple 中只抓取其中的一段

#list
piano_keys = ["a","b","c","d","e","f","g"]
#tuple
piano_keys = ("do","re","mi","fa","so","la","ti")


#slice [] 抓取list的2~5
print(piano_keys[2:5])

# 抓取2到最後
print(piano_keys[2:])

# 抓取最前面到第四個)
print(piano_keys[:4])

# 抓取2到5，但間格跳2
print(piano_keys[2:5:2])

#在全部的list中每兩個呈現
print(piano_keys[::2])

#在全部的list中從最後一個排列回來
print(piano_keys[::-1])