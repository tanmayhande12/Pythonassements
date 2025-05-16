a = ["Hello", "for", "Python", "programming"]

res = len(sorted(a, key=len, reverse=True)[0])
print(res)