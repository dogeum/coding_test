import sys
input = sys.stdin.readline
while True:
    number = input().strip()
    if number == '0':
        break
    reverseNumber = "".join(reversed(number))
    if int(reverseNumber) == int(number):
        print('yes')
    else:
        print('no')