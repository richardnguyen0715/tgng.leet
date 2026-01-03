a, b, c, d, e = [0, 1, 3], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [2, 4], [5]

print(list(set(a).intersection(set(b))))
print(list(set(a).intersection(set(c))))
print(list(set(a).intersection(set(d))))
print(list(set(a).intersection(set(e))))

word = {
    "" : 124
}