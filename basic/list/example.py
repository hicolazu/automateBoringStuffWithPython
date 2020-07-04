animals = [
    'Cat',
    'Dog',
    'Elephant',
    'Mouse'
]

print(animals[1])
print(animals[-1])  # last one
print(animals[0:2])  # slice (could be just [:2])
animals[3] = 'Fish'
print(animals[3])

numbers = [
    [
        10,
        20,
        30,
        40,
        50
    ],
    [
        1,
        2,
        3,
        4,
        5
    ]
]

print(numbers[0][0])
print(numbers[1][0])
del numbers[0][4]
print(numbers[0])

hello = 'hello'
print(list(hello))

print('h' in list(hello))
print('h' not in list(hello))
