personal_info = {}  # Initialize a dictionary to store personal information

name_invalid_chars = [63, 123, 125, 91, 93, 36, 42, 37, 33, 38, 64, 94, 124, 92, 47, 60, 62, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57] # Use ASCII for format conditions on name

address_invalid_chars = [33, 42, 126, 96, 60, 62, 92, 124, 37, 34, 39, 36, 43]

# Create a main loop for all personal information
while True:

    while True:   # Loop for name
        input_name = input("Please input a name: ")

        if any(ord(char) in name_invalid_chars for char in input_name):  # Check if the inputted name include invalid characters for name
            print("Please input a valid name.")  # If yes, print an error message
            continue 
        else:
            break  # Break the loop if the inputted name is valid

    while True:   # Loop for gender
        input_gender = input("Please input your gender (female/male): ").lower()  # Use lower function to handle all cases of letter

        if input_gender not in ["female", "male"]:    # If the inputted gender is not female or male,
            print("Please choose between female or male")   # Print an error message
        else:
            break   # Break the loop if the inputted gender is valid

    while True:  # Loop for age
        try:
            input_age = int(input("Please input age: "))  # Ask the user to input number only in age 
            break  # If the age is valid, break the loop
        except:
            print("Please input a valid number for age.")  # Else, print an error message

    while True:  # Loop for marital status
        input_marital_status = input("Please input your marital status (single/married/separated/divorced/widowed): ").lower()  # Use lower function to handle all cases of letter

        if input_marital_status not in ["single", "married", "separated", "divorced", "widowed"]:    # If the inputted marital status is not valid,
            print("Please input a valid marital status")   # Print an error message
        else:
            break   # Break the loop if the inputted marital status is valid

    while True:  # Loop for Address
        input_address= input("Please input an address: ")

        if any(ord(char) in address_invalid_chars for char in input_address):  # Check if the inputted address include invalid characters for address
            print("Please remove characters that are not allowed in an address.")  # If yes, print an error message
            continue 
        else:
            break  # Break the loop if the inputted address is valid

    while True: # Loop for Phone Number
        input_phone_number = input("Please input a phone number: ")
  
        if not input_phone_number.isdigit() and any(char not in "0123456789-+" for char in input_phone_number):  # Check if any invalid characters (non-digit and invalid symbols) are included
            print("Please input a valid phone number, international or local format.")  # If yes, print an error message
            continue 
        else:
            break  # Break the loop if the inputted phone number is valid





        