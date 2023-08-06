my_1st_tuple = ("Shah", "Newaz", "Shawon", 27)
v1, v2, v3, v4 = my_1st_tuple
print(v1)
print(v2)
print(v3)
print(v4, "\n")

my_1st_list = ["Ban", "PAK", "MAL", "INDO", "BRU", "MAL", [1, 2, 3, 4]]
b1, b2, b3, b4, b5, b6, [b7, b8, b9, b10] = my_1st_list
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
print(b6)
print(b7)
print(b8)
print(b9)
print(b10, "\n")

my_2nd_tuple = ("GP", "BL", "Robi", "Airtel", "Teletalk", "CityCell")
a1, a2, a3, *a4, a5 = my_2nd_tuple
print(a1)
print(a2)
print(a3)
print(a4)
print(a5, "\n")