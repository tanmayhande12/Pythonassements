def remove_duplicates(input_list):
    new_list = []
    for element in input_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)  