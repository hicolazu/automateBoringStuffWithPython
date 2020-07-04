spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

spam.append('whats up')
print(spam)

spam.insert(1, 'hii')
print(spam)

spam.remove('hi')
print(spam)

numbers = [5, 2, 6, 3, 8, 4]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

letters = ['A', 'z', 'Z', 'a']
letters.sort(key=str.lower)
print(letters)