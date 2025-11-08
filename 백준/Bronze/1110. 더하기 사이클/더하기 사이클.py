N = int(input())
newN = N
count = 0
sum = 0

while True:
    sum = newN%10 + newN//10
    newN = (newN%10)*10 + sum%10
    count += 1
    if newN == N:
        break
print(count)