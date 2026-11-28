import pandas as pd
import numpy as np

# Displays basic information about the program and the options available to the user.
print("This is a tracker for the KoG mod for DDNet. It tracks your map completions.")
print("It is not affiliated with DDNet or the KoG mod in any way.")
print("Enter an option below:")
print("1. Track a new map completion")
print("2. View every map you have completed")
print("3. View your total maps and points")
print("4. View the date that you completed the first map of a certain difficulty.")
print("5. Exit the program")

# A list of valid map difficulties.
map_difficulties = ["Easy", "Main", "Hard", "Insane", "Extreme"]

# This function gets the necessary information about a map from the user and sanitizes those inputs.
def obtain_map_info():
    map_name = input("Enter the name of the map you completed: ")
    points = input("Enter the points you earned for this map: ")
    while not points.isdigit():
        print("Invalid number of points. Please enter a number.")
        points = input("Enter the points you earned for this map: ")
    difficulty = input("Enter the difficulty of the map (Easy, Main, Hard, Insane, Extreme): ")
    while difficulty not in map_difficulties:
        print("Invalid difficulty. Please enter one of the following: Easy, Main, Hard, Insane, Extreme.")
        difficulty = input("Enter the difficulty of the map (Easy, Main, Hard, Insane, Extreme): ")
    sub_difficulty = input("Enter the number of stars that the map has (1-3): ")
    while sub_difficulty not in ["1", "2", "3"]:
        print("Invalid number of stars. Please enter a number between 1 and 3.")
        sub_difficulty = input("Enter the number of stars that the map has (1-3): ")
    date_completed = input("Enter the date you completed the map (MM/DD/YYYY) or N/A: ")
    while True:
        # Option to enter N/A (not everyone can remember the date they completed a map).
        if date_completed == "N/A":
            date_completed = np.nan
            break
        # Attemps to convert the date input into a datetime object to make sure it is in the correct format. 
        try:
            pd.to_datetime(date_completed, format="%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in MM/DD/YYYY format.")
            date_completed = input("Enter the date you completed the map (MM/DD/YYYY): ")
    return map_name, points, difficulty, sub_difficulty, date_completed

# This function allows the user to add a new map completion to the CSV file.
def add_map_completion():
    with open ("src/maps.csv", "a") as f:
        map_name, points, difficulty, sub_difficulty, date_completed = obtain_map_info()
        print(f"Map Name: {map_name}, Points: {points}, Difficulty: {difficulty}, Sub-Difficulty: {sub_difficulty}, Date Completed: {date_completed}")
        # Confirms with the user that the information they entered is correct before adding it to the dataframe.
        print("Is this information correct? (y = yes, anything else = no)")
        correct = input().lower()
        if correct == "y":
            # Adds the new map completion to the map_completions.csv file.
            f.write(f"\n{map_name},{points},{difficulty},{sub_difficulty},{date_completed}")
            print("Map added successfully!")
        else:
            print("Map not added.")
    f.close()

# This function allows the user to view the date that they completed the first map of a certain difficulty.
def view_first_difficulty_completion_date():
    difficulty = input("Enter the difficulty you want to view (Easy, Main, Hard, Insane, Extreme): ")
    while difficulty not in map_difficulties:
        print("Invalid difficulty. Please enter one of the following: Easy, Main, Hard, Insane, Extreme.")
        difficulty = input("Enter the difficulty you want to view (Easy, Main, Hard, Insane, Extreme): ")
    # Filters the dataframe to only include maps of the specified difficulty.
    filtered_df = maps_df[maps_df["Difficulty"] == difficulty]
    if filtered_df.empty:
        print(f"You have not completed any {difficulty} difficulty maps.")
    else:
        # Sorts the filtered dataframe by date and gets the first row (the earliest date).
        first_map = filtered_df.sort_values(by="Date").iloc[0]
        if (first_map["Date"] == "Date not specified"):
            print(f"You completed at least one {difficulty} map, but you didn't specify the date(s).")
        else:
            print(f"You completed your first {difficulty} map on {first_map['Date']}.")

# Basic decision tree to handle user input based on the options provided. 
option = input("Enter your option (1-5): ")
while option != "5":
    # Creates a dataframe from the map_completions.csv file, which contains information about the maps the user has completed.
    maps_df = pd.read_csv("src/maps.csv", names=["Name", "Points", "Difficulty", "Sub-Difficulty", "Date"], sep=",", header=0)
    maps_df["Date"] = maps_df["Date"].replace(np.nan, "Date not specified")
    if option == "1":
        add_map_completion()
    elif option == "2":
        print(maps_df)
    elif option == "3":
        maps = len(maps_df)
        points = maps_df["Points"].sum()
        print(f"You have completed {maps} maps and earned a total of {points} points.")
    elif option == "4":
        view_first_difficulty_completion_date()
    else:
        print("Invalid option. Please enter a number between 1 and 4.")
    option = input("Enter your option (1-5): ")