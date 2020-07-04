total = 0
for num in range(101):  # not includes 101 (100 is the last!)
    total += num
print(total)

for num in range(5, 0, -1):
    print('Time: ' + str(num))