def find_largest_number(numbers):
    """
    Finds the largest number in a list.

    Args:
        numbers: A list of numbers.

    Returns:
        The largest number in the list, or None if the list is empty.
    """
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage:
numbers = [10, 5, 20, 8, 15]
largest_number = find_largest_number(numbers)

if largest_number is not None:
    print("The largest number is:", largest_number)
else:
    print("The list is empty.")
    