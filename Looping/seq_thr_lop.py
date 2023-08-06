myTuple = ('a', 'b', 'c', 'd')
myList = [('a', 1, 'USD'), ('b', 2, 'BDT'), ('c', 3, 'CAD')]
myDict = {
    'Name' : 'Shawon',
    'Country' : 'Bangladesh',
    'Age' : 26
}
myStr = "Bohubrihi"
mySet ={"BDT", "CAT", "USD"}

for x in myTuple:
    print(x)
print('\n')

for x, y, z in myList:
    print(f'{x}, {y}, {z}')
print('\n')

for key, value in myDict.items():
    print(f'{key} = {value}')
print('\n')

for ch in myStr:
    print(ch)
print('\n')

for currency in mySet:
    print(currency)
print('\n')