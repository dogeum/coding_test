N = int(input())
a = map(int, input().split())
number = 0
for i in a:
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count += 1
    if count == 0:
        number += 1
    if i == 1:
        number -=1
print(number)