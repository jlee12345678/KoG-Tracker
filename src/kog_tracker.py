import pandas as pd

# Displays basic information about the program and the options available to the user.
print("This is a tracker for the KoG mod for DDNet. It tracks your map completions.")
print("It is not affiliated with DDNet or the KoG mod in any way.")
print("Enter an option below:")
print("1. Track a new map completion")
print("2. View every map you have completed")
print("3. View your total maps and points")
print("4. Exit the program")

# Basic decision tree to handle user input based on the options provided. 
option = input("Enter your option (1-4): ")
while option != "4":
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        pass
    else:
        print("Invalid option. Please enter a number between 1 and 4.")
    option = input("Enter your option (1-4): ")