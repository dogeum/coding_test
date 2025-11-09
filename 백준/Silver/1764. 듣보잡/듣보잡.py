import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n = set()
m = set()
k = set()
for _ in range(N):
    n.add(input().strip())
for _ in range(M):
    m.add(input().strip())

k = n & m
k = sorted(list(k))
print(len(k))
print(*k, sep='\n')