N = int(input())
sum = N

if N == 0:
    print('1')
else:
    
    while N > 1:
        sum *= N-1
        N -= 1
    print(sum)