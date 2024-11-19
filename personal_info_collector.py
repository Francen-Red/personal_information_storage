personal_info = {}  # Initialize a dictionary to store personal information

invalid_characters = [63, 123, 125, 91, 93, 36, 42, 37, 33, 38, 64, 94, 124, 92, 47, 60, 62, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57] # Use ASCII for format conditions on name

# Create a main loop for all personal information
while True:

    while True:   # Loop for name
        input_name = input("Please input a name: ")

        if any(ord(char) in invalid_characters for char in input_name):  # Check if the inputted name include invalid characters
            print("Please input a valid name.")  # If yes, print an error message
            continue 
        else:
            break  # Break the loop if the inputted name is valid

    while True:   # Loop for gender
        input_gender = input("Please type your gender (female/male): ").lower()  # Use lower function to handle all cases of letter

        if input_gender not in ["female", "male"]:    # If the inputted gender is not female or male,
            print("Please choose between female or male")   # Print an error message
        else:
            break   # Break the loop if the inputted gender is valid

            
