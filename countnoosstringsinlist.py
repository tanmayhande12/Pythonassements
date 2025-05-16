
def count_matching_strings(string_list):
    count = 0
    for string in string_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Example usage
strings = ["aba", "xyz", "aa", "b", "cdc", "d"]
result = count_matching_strings(strings)
print(result)
