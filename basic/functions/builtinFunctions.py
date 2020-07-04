import random
import pyperclip
from sys import api_version, exit

print(api_version)
print(random.randint(1, 10))

pyperclip.copy('Hello World!')
print(pyperclip.paste())

print('Hello')
exit()
print('Goodbye')
