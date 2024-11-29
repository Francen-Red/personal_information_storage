
import json

# Load personal_info from the file to access data
with open("personal_info.json", "r") as file:
    personal_info = json.load(file)  

# Ask for the name and print its details
while True:
    if personal_info:  # Ensure data is loaded before asking for input to avoid errors
        name = input("Whose personal information do you want to access?: ").strip()

   