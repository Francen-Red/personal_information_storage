
import json

# Load personal_info from the file to access data
with open("personal_info.json", "r") as file:
    personal_info = json.load(file)  

# Ask for the name and print its details
while True:
    if personal_info:  # Ensure data is loaded before asking for input to avoid errors
        name = input("Whose personal information do you want to access?: ").strip()

    # Check if name exists and print the details
        if name in personal_info:
            print(f"\nPersonal Info for {name}:")
            for key, value in personal_info[name].items():
                print(f"{key}: {value}")
        else:
            print(f"No information found for {name}.")  # Check if name does not exist, print an error message.
    break
