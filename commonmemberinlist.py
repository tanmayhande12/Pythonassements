a = [1, 2, 3, 4]
b = [5, 6, 3, 8]
common = set(a) & set(b)
if common:
    print("Common", common)
else:
    print("Not common.")