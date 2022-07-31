#!/usr/bin/env python3

import sys
import csv
import os
import datetime

raw_data = "raw.csv"


def create_csv():
    with open(raw_data, "w", newline="") as csv_file:
        fieldnames = ["Name", "Restaurant", "Count", "Timestamp"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    return fieldnames


def save_raw_data(user_name, restaurant):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    with open(raw_data, "a", newline="") as csv_file:
        fieldnames = ["Name", "Restaurant", "Count", "Timestamp"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow(
            {
                "Name": user_name,
                "Restaurant": restaurant,
                "Count": 1,
                "Timestamp": timestamp,
            }
        )
        # print(f"{user_name} has voted for {restaurant}")


def ranking_data():
    with open(raw_data, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        # results = {row["Restaurant"]: row["Count"] for row in reader}
        result_d = {}
        for row in reader:
            result_d["Restaurant"] = row["Restaurant"]
            # result_d["Count"] += 1
        print(result_d)


# def main():
# create_csv()
# save_raw_data(user_name, restaurant)
# try:
#     if not os.path.exists(raw_data):
#         create_csv()
#         print("CSV file created!")
#     # save_raw_data("Mark", "びっくりドンキー")
# except FileNotFoundError as e:
#     print(e)
#     sys.exit(1)
# else:
#     save_raw_data("ぺこら", "二郎")
# finally:
#     print("Done!")

# ranking_data()

# if __name__ == "__main__":
#     main()
