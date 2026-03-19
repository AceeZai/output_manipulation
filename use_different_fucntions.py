# Prog01: manual lstrip
def remove_leading_spaces(input_string):
    index_position = 0
    while index_position < len(input_string) and input_string[index_position] == " ":
        index_position += 1
    return input_string[index_position:]


# Prog02: manual removeprefix
def remove_prefix(input_string, prefix_value):
    if input_string[:len(prefix_value)] == prefix_value:
        return input_string[len(prefix_value):]
    return input_string


# Prog03: manual lower
def to_lowercase(input_string):
    result_string = ""
    for character_value in input_string:
        if "A" <= character_value <= "Z":
            result_string += chr(ord(character_value) + 32)
        else:
            result_string += character_value
    return result_string


# Prog04: manual isupper
def check_all_uppercase(input_string):
    has_letter = False
    for character_value in input_string:
        if "a" <= character_value <= "z":
            return False
        if "A" <= character_value <= "Z":
            has_letter = True
    return has_letter


# Prog05: manual endswith
def check_ends_with(input_string, suffix_value):
    return input_string[-len(suffix_value):] == suffix_value


# Prog06: manual ljust
def left_justify_string(input_string, total_width):
    if len(input_string) >= total_width:
        return input_string
    return input_string + " " * (total_width - len(input_string))


# Prog07: manual center
def center_string(input_string, total_width):
    if len(input_string) >= total_width:
        return input_string
    total_padding = total_width - len(input_string)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    return " " * left_padding + input_string + " " * right_padding


# Prog08: manual swapcase
def swap_case_string(input_string):
    result_string = ""
    for character_value in input_string:
        if "a" <= character_value <= "z":
            result_string += chr(ord(character_value) - 32)
        elif "A" <= character_value <= "Z":
            result_string += chr(ord(character_value) + 32)
        else:
            result_string += character_value
    return result_string


# Prog09: manual capitalize
def capitalize_string(input_string):
    if not input_string:
        return input_string
    first_character = input_string[0]
    if "a" <= first_character <= "z":
        first_character = chr(ord(first_character) - 32)

    remaining_string = ""
    for character_value in input_string[1:]:
        if "A" <= character_value <= "Z":
            remaining_string += chr(ord(character_value) + 32)
        else:
            remaining_string += character_value

    return first_character + remaining_string


# Prog10: manual title
def title_case_string(input_string):
    result_string = ""
    new_word_flag = True

    for character_value in input_string:
        if character_value == " ":
            new_word_flag = True
            result_string += character_value
        else:
            if new_word_flag and "a" <= character_value <= "z":
                result_string += chr(ord(character_value) - 32)
            elif not new_word_flag and "A" <= character_value <= "Z":
                result_string += chr(ord(character_value) + 32)
            else:
                result_string += character_value
            new_word_flag = False

    return result_string