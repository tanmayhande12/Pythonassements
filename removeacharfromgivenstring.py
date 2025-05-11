def remove_char(input_string, char_to_remove):
  new_string = input_string.replace(char_to_remove, "")
  return new_string

my_string = "Hello, World!"
char_to_delete = ","
modified_string = remove_char(my_string, char_to_delete)
print(modified_string)

my_string2 = "programming"
char_to_delete2 = "g"
modified_string2 = remove_char(my_string2, char_to_delete2)
print(modified_string2)