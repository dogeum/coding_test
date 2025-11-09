import math
A = int(input())
for _ in range(A):
    N, M = map(int, input().split(' '))
    print(math.comb(M, N))