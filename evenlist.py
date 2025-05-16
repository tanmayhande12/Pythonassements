def remove_even_numbers(input_list):
    odd_numbers = [num for num in input_list if num % 2 != 0]
    return odd_numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = remove_even_numbers(my_list)
print(result_list)
