# Prog01: Print the bigger number of 2 inputs
def prog01_bigger_number():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("Bigger number:", max(first_number, second_number))


# Prog02: Print "Equal" if both numbers are the same
def prog02_check_equal():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    if first_number == second_number:
        print("Equal")
    else:
        print("Not Equal")


# Prog03: Print the sum of 2 numbers
def prog03_sum():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("Sum:", first_number + second_number)


# Prog04: Print the product of 2 numbers
def prog04_product():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("Product:", first_number * second_number)


# Prog05: Print the quotient (with decimal)
def prog05_quotient():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("Quotient:", first_number / second_number)


# Prog06: Print first number raised to second number
def prog06_power():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print("Result:", first_number ** second_number)


# Prog07: Sum of 10 numbers
def prog07_sum_10():
    total_sum = 0
    for _ in range(10):
        total_sum += float(input("Enter number: "))
    print("Total Sum:", total_sum)


# Prog08: Count odd numbers from 10 inputs
def prog08_count_odd():
    odd_count = 0
    for _ in range(10):
        number_value = int(input("Enter number: "))
        if number_value % 2 != 0:
            odd_count += 1
    print("Odd numbers count:", odd_count)


# Prog09: Print even numbers from 0 to 100
def prog09_even_numbers():
    for number_value in range(0, 101):
        if number_value % 2 == 0:
            print(number_value)


# Prog10: Print numbers from 0 to 100 except those ending in 0
def prog10_skip_ending_zero():
    for number_value in range(0, 101):
        if number_value % 10 != 0:
            print(number_value)


# Main Menu
def main_menu():
    while True:
        print("\n--- MENU ---")
        print("1. Prog01 - Bigger number")
        print("2. Prog02 - Check equal")
        print("3. Prog03 - Sum")
        print("4. Prog04 - Product")
        print("5. Prog05 - Quotient")
        print("6. Prog06 - Power")
        print("7. Prog07 - Sum of 10 numbers")
        print("8. Prog08 - Count odd numbers")
        print("9. Prog09 - Even numbers (0-100)")
        print("10. Prog10 - Skip numbers ending in 0")
        print("11. Exit")

        choice_value = input("Choose an option: ")

        if choice_value == "1":
            prog01_bigger_number()
        elif choice_value == "2":
            prog02_check_equal()
        elif choice_value == "3":
            prog03_sum()
        elif choice_value == "4":
            prog04_product()
        elif choice_value == "5":
            prog05_quotient()
        elif choice_value == "6":
            prog06_power()
        elif choice_value == "7":
            prog07_sum_10()
        elif choice_value == "8":
            prog08_count_odd()
        elif choice_value == "9":
            prog09_even_numbers()
        elif choice_value == "10":
            prog10_skip_ending_zero()
        elif choice_value == "11":
            break
        else:
            print("Invalid choice")


main_menu()