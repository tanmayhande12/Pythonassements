def swap_case_string(input_string):
    swapped_string = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            swapped_string += char.upper()
        elif 'A' <= char <= 'Z':
            swapped_string += char.lower()
        else:
            swapped_string += char
    return swapped_string

input_str = "Hello World 123"
result = swap_case_string(input_str)
print(result)