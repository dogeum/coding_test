import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
D = int(input())

AD = D//3600
BD = (D%3600)//60
CD = (D%3600)%60

C+=CD
B+=BD
A+=AD

B+=C//60
A += B//60

C%=60
B%=60
A%=24

print(A, B, C)