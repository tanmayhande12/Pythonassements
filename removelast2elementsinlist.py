def func(lst):
    new_list = []
    rm_list = [0, 4, 5]
    for i in range(len(lst)):
        if i not in rm_list:
            new_list.append(lst[i])
    return new_list
     
l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(func(l))