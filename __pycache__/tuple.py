my_tuple = ("apple", "banna", "mango", "orange", 1, 3, 4.8, ["a", "b", "c"], "mango")

print(my_tuple)
print(type(my_tuple))

sports = ("Badminton", "Cricket", "Football", "Tennis")
print(sports)
print(type(sports))

sports_list = list(sports)
sports_list[0] = "Hadud"
print(sports_list)
print(type(sports_list))

sports = tuple(sports_list)
print(sports)
print(type(sports))

sports[1] = "Hadud"

my_tpl = ("mango", "orange", "banana")
my_tpl = list(my_tpl)

my_tpl[1] = "apple"

my_tpl.append(1)
my_tpl.append(2)
my_tpl.append(3)

my_tpl.remove(1)

my_tpl = tuple(my_tpl)
print(my_tpl)

print(len(my_tpl))
i = 0

while i in range(0, len(my_tpl)):
    print(my_tpl[i])
    i=i+1
    



