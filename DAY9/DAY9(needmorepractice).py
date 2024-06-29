#HINT: You can call clear() to clear the output in the console.
from replit import clear

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(biddding_record):
    highest_bid = 0
    winner = ""
    # biddding_record = {"angel": 123. "jay": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finisheda = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()


# Dictionaries (key and value)-------------------------
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
# # dictionary[key] key須完全一致，且類型需一致
# print(programming_dictionary["Bug"])
#
# # add the new item in dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over"
# print(programming_dictionary)
#
# # create an empty dictionary
# empty_dictionary = {}
#
# # wipe an existiong dictionary (清除整個字典資料)
# programing_dictionary = {}

# edit an item in a dictionary
# programming_dictionary["Bug"] = "a moth in your computer"
#
#
# # loop through a dictionary
# for thing in programming_dictionary:
#     # 會回傳KEY
#     print(thing)
#     # 會回傳value
#     print(programming_dictionary[thing])



# Nesting 崁套---------------------------------------------------------------------------------------
# [
# {key: [list], key2: {dict}},  0
# {key: value, key2: value}     1
# ]

# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }
#
# #Nesting a List in a Dictionary
#
# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# # Nesting a Dictionary in a Dictionary
# cities_visited ={
# "Paris": "2",
# "Lille": "1",
# "Dijon": "3"
# }
#
#
# travel_log = {
#   "France": cities_visited,
# # or
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": "12" }
# }


# Nesting a Dictionary in a list
# travel_log = [
#     {
#      "country":"France",
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#     },
#   {
#     "country":"Germany",
#    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#    "total_visits": 5 }
# ]
#
# print(travel_log)



