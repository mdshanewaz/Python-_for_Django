my_dict = {
    "key1" : "Hello",
    "key2" : "world",
}
print(my_dict)
print(type(my_dict),"\n")

my_dict2 = {}
print(my_dict2)
print(type(my_dict2),"\n")

my_dict3 = dict()
print(my_dict3)
print(type(my_dict3),"\n")

my_dict["key3"] = "Bangladesh"
print(my_dict)

my_dict["key3"] = "Afganistan"
print(my_dict,"\n")

my_dict["key4"] = 2023
print(my_dict,"\n")

del my_dict["key4"]
print(my_dict)