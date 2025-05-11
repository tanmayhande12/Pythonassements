def replace_space_with_character(input_string, replacement_character):
 
  return input_string.replace(" ", replacement_character)

# Example usage
my_string = "This is a Python Programming"
new_string = replace_space_with_character(my_string, "-")
print(new_string)

new_string = replace_space_with_character(my_string, "_")
print(new_string)