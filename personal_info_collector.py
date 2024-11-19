personal_info = {}  # Initialize a dictionary to store personal information

invalid_characters = [63, 123, 125, 91, 93, 36, 42, 37, 33, 38, 64, 94, 124, 92, 47, 60, 62, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57] # Use ASCII for format conditions on name

# Create a main loop for all personal information
while True:

    while True:   # Loop for name
        input_name = input("Please input a name: ")

        if any(ord(char) in invalid_characters for char in input_name): 
            print("Please input a valid name.")  
            continue 
        else:
            break 
