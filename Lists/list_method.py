my_list = ["Soudia Arabia", "Iran", "Turkey", "Pakistan", "Indoneshia", "Egypt", "Albenia", "Bhutan", "Nepal", "France", "Italy", "France"]
print(my_list)

my_list.append("Bangladesh")
print(my_list)

my_list.append(["Maldiv", "Brunei"])
print(my_list)

my_list.extend(["Maldiv", "Brunei"])
print(my_list)

my_list.insert(-1, "Germany")
print(my_list)

my_list.remove("France")
print(my_list)

country_removed = my_list.pop(1)
print(my_list)
print(country_removed)

print(my_list.clear())