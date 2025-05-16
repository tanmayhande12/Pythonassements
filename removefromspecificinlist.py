
def remove_elements(input_list):
    indices_to_remove = [0, 4, 5]
    return [item for index, item in enumerate(input_list) if index not in indices_to_remove]

my_list = [10, 20, 30, 40, 50, 60, 70]
result = remove_elements(my_list)
print(result)

