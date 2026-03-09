#Program 1
#Ask for name with leading spaces. ex; ____ Acee Zai Mendez
full_name = input("Enter your full name: ")
#Use lstrip.(), this function removes spaces in the beginning of a string
clean_name = full_name.lstrip()
#Print clean_name
print(clean_name)

#Program 2
#Ask for numbers 0-1000
num_input = int(input("Enter a number (0-1000): "))
num_sixdigit = f"{num_input:06}"
print(num_sixdigit)

#Program 3
#Input mixed lower and uppercase names
full_name = input("Please enter your full name in mixed lower and uppercasing style: ")
#Use upper() function
uppercase_name = full_name.upper()
print(uppercase_name)

#Program 4
#Use the code from upper but use lower() function
full_name = input("Please enter your full name in mixed lower and uppercasing style:  ")
lowercase_name = full_name.lower()
print(lowercase_name)

#Program 5
#A program to convert incorrect casing to proper casing
incorrect_casing = input("Please enter your name with incorrect casing: ")
#Use title() function (Converts the first character of every word in a string to uppercase and the remaining characters to lowercase, returning a new, title-cased string.)
proper_casing = incorrect_casing.title()
print(proper_casing)

#Program 6
#This program will reverse your original casing style.
user_input_name = input("Enter your name: ")
print(user_input_name.swapcase())

# Program 7: Word Count
input_sentence = input("Enter a sentence: ")
# split() creates a list of words; len() counts them
total_words = len(input_sentence.split())
print(f"Word count: {total_words}")

#Program 8
#Will count the number of characters in a name
full_name = input("Enter your full name: ")
character_count = len(full_name)
print(character_count)

# Program 9: Pascal Case (Example: acee zai -> AceeZai)
user_full_name = input("Enter your full name for PascalCase: ")
pascal_case_name = ''.join([word.capitalize() for word in user_full_name.split()])
print(f"Pascal Case: {pascal_case_name}")

# Program 10: Snake Case (Example: Acee Zai -> acee_zai)
user_full_name_input = input("Enter your full name for snake_case: ")
snake_case_name = '_'.join([word.lower() for word in user_full_name_input.split()])
print(f"Snake Case: {snake_case_name}")


