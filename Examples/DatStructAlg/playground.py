lst = [1, 2, 3, 4]

# print(list(map(lambda x: x**3, lst)))

# print(list(filter(lambda x: x < 3, lst)))

print("\n".join(dir(lst)))

print(dir(lst).__sizeof__())
print(lst.__sizeof__())
