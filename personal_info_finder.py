
import json

# Load personal_info from the file to access data
with open("personal_info.json", "r") as file:
    personal_info = json.load(file)  

# Define text colors using ANSII color codes
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
pink = "\033[38;5;213m"
reset_color = "\033[0m"

# Ask for the name and print its details
while True:
    if personal_info:  # Ensure data is loaded before asking for input to avoid errors
        name = input(f"{pink}Whose personal information do you want to access?:{reset_color} ").strip()

    # Check if name exists and print the details
        if name in personal_info:
            print(f"{green}\nPersonal Info for {blue}{name}:{reset_color}")
            for key, value in personal_info[name].items():
                print(f"{key}: {value}")
        else:
            print(f"{red}No information found for {name}.")  # Check if name does not exist, print an error message.

    another_name = input(f"{pink}Do you want to access other personal information?(yes/no):{reset_color} ").lower().strip()
    if another_name not in ["yes", "no"]:
            print(f"{red}Please choose between yes or no{reset_color}")
            continue
    if another_name == "yes": 
         continue
    break