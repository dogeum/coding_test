N = int(input())
for i in range(N):
    X = input()
    sum = 0
    before = 0
    for i in range(len(X)):
        if X[i] == 'O':
            before+=1
            sum+=before
        else:
            before = 0
    print(sum)
