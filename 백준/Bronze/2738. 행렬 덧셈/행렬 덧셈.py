import sys
input = sys.stdin.readline #백준용 입력 코드

N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

c = [[a[i][j] + b[i][j] for j in range(M)] for i in range(N)]
        
for row in c:
    print(*row) #print(row)는 리스트형식으로 출력되고
                #print(*row)는 리스트 값을 하나씩 꺼내 공백으로 구분해 출력함