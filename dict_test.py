pairs = [('a', 1), ('a', 2),('b', 2)]

d = {}
for key, value in pairs:
    # print('key-->', key)
    if key not in d:
        d[key] = []
    print(d)
d[key].append(value)
# print(d)