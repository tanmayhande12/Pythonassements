def print_pattern(rows):
    for i in range(1, rows + 1):
        num = 1
        for j in range(i):
            print(num, end=" ")
            num += 1
        num -= 2
        for j in range(i - 1):
            if num > 0:
                print(num, end=" ")
                num -= 1
        print()

print_pattern(4)