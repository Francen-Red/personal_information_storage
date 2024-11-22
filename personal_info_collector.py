personal_info = {}  # Initialize a dictionary to store personal information

# Define invalid characters for name, address, and email using ASCII values
name_invalid_chars = [63, 123, 125, 91, 93, 36, 42, 37, 33, 38, 64, 94, 124, 92, 47, 60, 62, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57] 

address_invalid_chars = [33, 42, 126, 96, 60, 62, 92, 124, 37, 34, 39, 36, 43]

email_invalid_chars = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 94, 96] 

# Define text colors using ANSII color codes
red = "\033[31m"
orange = "\033[38;5;214m"
yellow = "\033[33m"
green = "\033[32m"
blue = "\033[34m"
pink = "\033[38;5;213m"
violet = "\033[35m"
brown = "\033[38;5;94m"
reset_color = "\033[0m"

# Create a main loop for all personal information
while True:

    while True:   # Loop for name
        input_name = input("Please input a name: ").strip()  # Strip any unnecessary spaces

        if any(ord(char) in name_invalid_chars for char in input_name):  # Check if the inputted name include invalid characters for name
            print(f"{red}Please input a valid name.{reset_color}")  # If yes, print an error message
            continue 
        elif not input_name:   # Check if input is empty
            print(f"{red}Name cannot be empty. Please input a name{reset_color}")
            continue
        else:
            break  # Break the loop if the inputted name is valid

    while True:   # Loop for gender
        input_gender = input("Please input your gender (female/male): ").lower().strip()  # Use lower function to handle all cases of letter, and strip function to remove unnecessary spaces

        if input_gender not in ["female", "male"]:    # If the inputted gender is not female or male,
            print(f"{red}Please choose between female or male{reset_color}")   # Print an error message
        else:
            break   # Break the loop if the inputted gender is valid

    while True:  # Loop for age
        try:
            input_age = int(input("Please input age: "))  # Ask the user to input number only in age
            if 1 <= input_age <= 120:  # Check if the person's age is valid (116 is so far the oldest age of a person)
                break  # If the age is valid, break the loop
            else:
                print(f"{red}Please input a valid age. Type 1 if the person is months old only{reset_color}")
        except:
            print(f"{red}Please input a valid number for age.{reset_color}")  # Else, print an error message

    while True:  # Loop for marital status
        input_marital_status = input("Please input your marital status (single/married/separated/divorced/widowed): ").lower().strip()  # Use lower function to handle all cases of letter, and strip function to remove unnecessary spaces

        if input_marital_status not in ["single", "married", "separated", "divorced", "widowed"]:    # If the inputted marital status is not valid,
            print(f"{red}Please input a valid marital status.{reset_color}")   # Print an error message
        else:
            break   # Break the loop if the inputted marital status is valid

    while True:  # Loop for Address
        input_address= input("Please input an address: ").strip()

        if any(ord(char) in address_invalid_chars for char in input_address):  # Check if the inputted address include invalid characters for address
            print(f"{red}Please remove characters that are not allowed in an address.{reset_color}")  # If yes, print an error message
            continue 
        elif not input_address:  # Check if input is empty
            print(f"{red}Address cannot be empty. Please input an address.{reset_color}")
        else:
            break  # Break the loop if the inputted address is valid

    while True: # Loop for Phone Number
        input_phone_number = input("Please input a phone number: ")
  
        if not input_phone_number.isdigit() and any(char not in "0123456789-+" for char in input_phone_number):  # Check if any invalid characters (non-digit and invalid symbols) are included
            print(f"{red}Please input a valid phone number, international or local format.{reset_color}")  # If yes, print an error message
            continue 
        else:
            break  # Break the loop if the inputted phone number is valid

    while True: # Loop for Email Address
        input_email = input("Please input an email address: ").strip()

        if any(ord(char) in email_invalid_chars for char in input_email): # Check if the inputted email address include invalid characters for email address
            print(f"{red}Please input a valid email address.{reset_color}")  # If yes, print an error message
            continue
        elif not input_email:
            print(f"{red}Email cannot be empty. Please input an email.{reset_color}")
        else:
            break  # Break the loop if the inputted email address is valid

    while True:  # Loop for confirmation
        confirmation = input(f"\n{red}Name = {reset_color}{input_name}\n"   # Use formatted strings to display every information of the user's input
            f"{orange}Gender = {reset_color}{input_gender}\n"
            f"{yellow}Age = {reset_color}{input_age}\n"
            f"{green}Marital Status = {reset_color}{input_marital_status}\n"
            f"{blue}Address = {reset_color}{input_address}\n"
            f"{pink}Phone Number = {reset_color}{input_phone_number}\n"
            f"{violet}Email = {reset_color}{input_email}\n"
            f"\n{brown}Is this correct? (yes or no):{reset_color} ").lower()  
        
        if confirmation not in ["yes", "no"]:    # If the confirmation reply is not "yes" or "no"
            print(f"{red}Please choose between yes or no")   # Print an error message

        # If the information is correct, store it in the dictionary
        elif confirmation == "yes":
            personal_info[input_name] = {
            "Gender": input_gender,
            "Age": input_age,
            "Marital Status": input_marital_status,
            "Address": input_address,
            "Phone Number": input_phone_number,
            "Email": input_email
            }
            break    

        elif confirmation == "no":
            while True:
                retry_choice =input("Retry name, gender, age, marital status, address, phone number, or email? Choose one: ").lower()

                if retry_choice not in ["name", "gender", "age", "marital status", "address", "phone number", "email"]:    # If the inputted gender is not female or male,
                    print(f"{red}Please choose one (name/gender/age/marital status/address/phone number/email){reset_color}")
                    continue

                if retry_choice == "name":
                    while True:   # Loop for name
                        input_name = input("Please input a name: ").strip()  # Strip any unnecessary spaces

                        if any(ord(char) in name_invalid_chars for char in input_name):  # Check if the inputted name include invalid characters for name
                            print(f"{red}Please input a valid name.{reset_color}")  # If yes, print an error message
                            continue 
                        elif not input_name:   # Check if input is empty
                            print(f"{red}Name cannot be empty. Please input a name{reset_color}")
                            continue
                        else:
                            break  # Break the loop if the inputted name is valid

                elif retry_choice == "gender":
                   while True:   # Loop for gender
                    input_gender = input("Please input your gender (female/male): ").lower().strip()  # Use lower function to handle all cases of letter, and strip function to remove unnecessary spaces

                    if input_gender not in ["female", "male"]:    # If the inputted gender is not female or male,
                        print(f"{red}Please choose between female or male{reset_color}")   # Print an error message
                    else:
                        break   # Break the loop if the inputted gender is valid

                elif retry_choice == "age":
                     while True:  # Loop for age
                        try:
                            input_age = int(input("Please input age: "))  # Ask the user to input number only in age
                            if 1 <= input_age <= 120:  # Check if the person's age is valid (116 is so far the oldest age of a person)
                                break  # If the age is valid, break the loop
                            else:
                                print(f"{red}Please input a valid age. Type 1 if the person is months old only{reset_color}")
                        except:
                            print(f"{red}Please input a valid number for age.{reset_color}")  # Else, print an error message

                elif retry_choice == "marital status":
                   while True:  # Loop for marital status
                    input_marital_status = input("Please input your marital status (single/married/separated/divorced/widowed): ").lower().strip()  # Use lower function to handle all cases of letter, and strip function to remove unnecessary spaces

                    if input_marital_status not in ["single", "married", "separated", "divorced", "widowed"]:    # If the inputted marital status is not valid,
                        print(f"{red}Please input a valid marital status.{reset_color}")   # Print an error message
                    else:
                        break   # Break the loop if the inputted marital status is valid

                elif retry_choice == "address":
                    while True:  # Loop for Address
                        input_address= input("Please input an address: ").strip()

                        if any(ord(char) in address_invalid_chars for char in input_address):  # Check if the inputted address include invalid characters for address
                            print(f"{red}Please remove characters that are not allowed in an address.{reset_color}")  # If yes, print an error message
                            continue 
                        elif not input_address:  # Check if input is empty
                            print(f"{red}Address cannot be empty. Please input an address.{reset_color}")
                        else:
                            break  # Break the loop if the inputted address is valid

                elif retry_choice == "phone number":
                    while True:
                        input_phone_number = input("Please input a phone number: ")
                        if not input_phone_number.isdigit() and any(char not in "0123456789-+" for char in input_phone_number):
                            print(f"{red}Please input a valid phone number, international or local format.{reset_color}")  # If yes, print an error message
                        else:
                            break

                elif retry_choice == "email":
                    while True:
                        input_email = input("Please input an email address: ").strip()
                        if any(ord(char) in email_invalid_chars for char in input_email):
                            print(f"{red}Please input a valid email address.{reset_color}")
                        elif not input_email:
                            print(f"{red}Email cannot be empty. Please input an email.{reset_color}")
                        else:
                            break

# Break the retry loop once a valid input is given
                break

# Ask if the user wants to input another entry
    another_entry = input("Do you want to input another entry? (yes/no): ").lower()
    if another_entry != "yes":  # If the user does not want to input another entry
        break  # Break the loop

# Store the inputted information in a txt file
with open("personal_info.txt", "a") as file:
        file.write(f"Name: {input_name}\n")
        file.write(f"Gender: {input_gender}\n")
        file.write(f"Age: {input_age}\n")
        file.write(f"Marital Status: {input_marital_status}\n")
        file.write(f"Address: {input_address}\n")
        file.write(f"Phone Number: {input_phone_number}\n")
        file.write(f"Email: {input_email}\n")
        file.write("\n" + "="*40 + "\n\n")   # Add a separator to easily distinguish different information entry