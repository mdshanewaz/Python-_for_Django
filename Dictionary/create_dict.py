my_dict = {
    'key1' : 'hello',
    'key2' : 'world!',
    'key3' : 'Feni'
}
print(my_dict, "\n")

new_dict = dict(key1 = 'Shah', key2 = 'Newaz', key3 = 26)
print(new_dict, "\n")

new_dict2 = dict(zip(['key1', 'key2', 'key3'], ['Jannatul', 'Ferdousi', 'Rimi']))
print(new_dict2, "\n")

new_dict3 = dict([('key1', 'Shah'), ('key2', 'Newaz'), ('key3', 'Shawon')])
print(new_dict3, "\n")

new_dict4 = dict({'key1': 'Shah', 'key2': 'Newaz', 'key3': 'Shawon'})
print(new_dict4, "\n")

new_dict5 = dict({'key1': 'Shah', 'key2': 'Newaz'}, key3 = 'Shawon')
print(new_dict5 ,"\n")

print(new_dict5.pop('key3'), "\n")

my_list = list(new_dict4)
print(my_list, "\n")