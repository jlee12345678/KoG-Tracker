import pandas as pd

# Displays basic information about the program and the options available to the user.
print("This is a tracker for the KoG mod for DDNet. It tracks your map completions.")
print("It is not affiliated with DDNet or the KoG mod in any way.")
print("Enter an option below:")
print("1. Track a new map completion")
print("2. View every map you have completed")
print("3. View your total maps and points")
print("4. Exit the program")

# Creates a dataframe from the map_completions.csv file, which contains information about the maps the user has completed.
maps_df = pd.read_csv("map_completions.csv", names=["Map Name", "Points", "Difficulty", "Sub-Difficulty", "Date Completed"])
# A list of valid map difficulties.
map_difficulties = ["Easy", "Medium", "Hard", "Insane", "Extreme"]

# This function gets the necessary information about a map from the user and sanitizes those inputs.
def obtain_map_info():
    map_name = input("Enter the name of the map you completed: ")
    points = input("Enter the points you earned for this map: ")
    # Checks to see if the input is a number (points can only be a number).
    while not points.isdigit():
        print("Invalid number of points. Please enter a number.")
        points = input("Enter the points you earned for this map: ")
    difficulty = input("Enter the difficulty of the map (Easy, Medium, Hard, Insane, Extreme): ")
    # Checks to see if the input is a valid map difficulty.
    while difficulty not in map_difficulties:
        print("Invalid difficulty. Please enter one of the following: Easy, Medium, Hard, Insane, Extreme.")
        difficulty = input("Enter the difficulty of the map (Easy, Medium, Hard, Insane, Extreme): ")
    sub_difficulty = input("Enter the number of stars that the map has (1-3): ")
    # Checks to see if the input is a valid number of stars.
    while sub_difficulty not in ["1", "2", "3"]:
        print("Invalid number of stars. Please enter a number between 1 and 3.")
        sub_difficulty = input("Enter the number of stars that the map has (1-3): ")
    date_completed = input("Enter the date you completed the map (MM/DD/YYYY): ")
    while True:
        # Attemps to convert the date input into a datetime object to make sure it is in the correct format. 
        try:
            pd.to_datetime(date_completed, format="%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in MM/DD/YYYY format.")
            date_completed = input("Enter the date you completed the map (MM/DD/YYYY): ")
    return map_name, points, difficulty, sub_difficulty, date_completed

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