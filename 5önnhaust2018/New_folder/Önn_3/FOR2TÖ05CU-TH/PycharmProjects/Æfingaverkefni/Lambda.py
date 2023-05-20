#Along A. Loftsson
print("1.")
print()

three_list = [1, 2, 3, 4, 5, 6, 9, 13, 53, 23, 27]
new_list = list(filter(lambda x: (x%3 == 0), three_list))

print(new_list)

print()
print("2.")
print()

quadruple = [1, 4, 8, 9, -3]
newer_list = list(map(lambda x: x * 4, quadruple))

print(newer_list)