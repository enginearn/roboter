#!/usr/bin/env python3

import sys


class GreetAndQuestions(object):
    def __init__(self, your_name="anonymous", my_name="roboter", restaurant="somewhere nice place"):
        self.your_name = your_name
        self.my_name = my_name
        self.restaurant = restaurant

    def say_hello(self):
        self.your_name = input(f"Hi! I'm {self.my_name}. What's yours?\n")
        if len(self.your_name) < 1:
            self.your_name = "anonymous"
        print(f"Hello! {self.your_name}! Nice to meet you!")
        # return self.your_name

    def ask_restaurant(self):
        self.restaurant = input("What restaurant do you like?\n")
        counter = 0
        while len(self.restaurant) < 1:
            self.restaurant = input("I couldn't hear you...\nWhat restaurant do you like?\n")
            counter += 1
            if counter == 3:
                print(f"I have asked {counter} times!")
                print("I'm sorry, I can't understand you...")
                break
            continue
        if len(self.restaurant) < 1:
            self.restaurant = "somewhere nice place"
        print(f"{self.your_name} Thank you!\nHave a nice meal at {self.restaurant}!")
        # return self.restaurant

        def recommend_restaurant(self):
            print(f"{self.your_name} I recommend {self.restaurant}!\nDo you like it?")

# greeting_a = GreetAndQuestions()
# greeting_a.say_hello()
# user_name = greeting_a.your_name
# print(f"You are {user_name}, aren't you?")
# greeting_a.ask_restaurant()
# resutraunt = greeting_a.restaurant
# print(f"{user_name} has voted for {resutraunt}!")

if __name__ == "__main__":
    sys.exit(0)
