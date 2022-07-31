#!/usr/bin/env python3

import os
import greeting.greeting
import save_data.save_to_csv

# def get_user_input():
#     user_name = input("What is your name?\n")
#     restaurant = input("What restaurant do you like?\n")
#     return user_name, restaurant

def main():
    # user_name, restaurant = get_user_input()
    user = greeting.greeting.GreetAndQuestions()
    user.say_hello()
    user_name = user.your_name
    print(f"You are {user.your_name}, aren't you?")

    user.ask_restaurant()
    restaurant = user.restaurant

    if not os.path.exists("raw.csv"):
        save_data.save_to_csv.create_csv()
    else:
        save_data.save_to_csv.save_raw_data(user_name, restaurant)

    print(f"{user_name} has voted for {restaurant}!")

if __name__ == "__main__":
    main()
