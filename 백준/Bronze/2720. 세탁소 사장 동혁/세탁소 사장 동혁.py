import sys
input = sys.stdin.readline
Q, D, N, P = int(25), int(10), int(5), int(1)

T = int(input())
for i in range(T):
    C = int(input())
    q = C//Q
    d = (C%Q)//D
    n = ((C%Q)%D)//N
    p = ((C%Q)%D)%N
    print(q, d, n, p)