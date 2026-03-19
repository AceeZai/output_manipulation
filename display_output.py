# Prog01: Display all numbers that have duplicates (10 inputs)
def prog01_show_duplicate_numbers():
    number_list = []
    for index_value in range(10):
        number_value = input(f"Enter number {index_value + 1}: ")
        number_list.append(number_value)

    duplicate_set = set()
    for value in number_list:
        if number_list.count(value) > 1:
            duplicate_set.add(value)

    print("Duplicates:", list(duplicate_set))


# Prog02: Display the number with the most duplicates (until invalid input)
def prog02_most_frequent_number():
    number_list = []

    while True:
        user_input = input("Enter number (or press Enter to stop): ")
        if user_input == "":
            break
        number_list.append(user_input)

    if number_list:
        most_common_value = max(number_list, key=number_list.count)
        print("Most frequent:", most_common_value)
    else:
        print("No input provided")


# Prog03: Display the highest number (until invalid input)
def prog03_highest_number():
    number_list = []

    while True:
        user_input = input("Enter number (or press Enter to stop): ")
        if user_input == "":
            break
        number_list.append(float(user_input))

    if number_list:
        print("Highest:", max(number_list))
    else:
        print("No input provided")


# Prog04: Display numbers from highest to lowest (sort)
def prog04_sort_descending_numbers():
    number_list = []

    while True:
        user_input = input("Enter number (or press Enter to stop): ")
        if user_input == "":
            break
        number_list.append(float(user_input))

    number_list.sort(reverse=True)
    print("Sorted (high to low):", number_list)


# Prog05: Display the average of the numbers
def prog05_compute_average():
    number_list = []

    while True:
        user_input = input("Enter number (or press Enter to stop): ")
        if user_input == "":
            break
        number_list.append(float(user_input))

    if number_list:
        average_value = sum(number_list) / len(number_list)
        print("Average:", average_value)
    else:
        print("No input provided")


# Menu to run all programs
def main_menu():
    while True:
        print("\n--- MENU ---")
        print("1. Prog01 - Duplicates (10 inputs)")
        print("2. Prog02 - Most frequent number")
        print("3. Prog03 - Highest number")
        print("4. Prog04 - Sort descending")
        print("5. Prog05 - Average")
        print("6. Exit")

        choice_value = input("Choose an option: ")

        if choice_value == "1":
            prog01_show_duplicate_numbers()
        elif choice_value == "2":
            prog02_most_frequent_number()
        elif choice_value == "3":
            prog03_highest_number()
        elif choice_value == "4":
            prog04_sort_descending_numbers()
        elif choice_value == "5":
            prog05_compute_average()
        elif choice_value == "6":
            break
        else:
            print("Invalid choice")


main_menu()