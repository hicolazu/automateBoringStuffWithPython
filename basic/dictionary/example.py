import pprint

myCat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

otherCat = {
    'size': 'fat',
    'disposition': 'loud',
    'color': 'gray'
}

print(myCat['size'])
print(myCat == otherCat)  # there is no order!

print()

print(myCat.values())
print(myCat.keys())

print()
for key in myCat.keys():
    print(key)

print()
for item in myCat.items():
    print(item)  # tuple with (key, value)

print(myCat.get('size', 'default'))
print(myCat.get('sizx', 'default'))

message = 'Hello World from Python!'
count = {}

for char in message.upper():
    if char == ' ':
        count.setdefault('space', 0)
        count['space'] = count['space'] + 1
        continue
    else:
        count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)