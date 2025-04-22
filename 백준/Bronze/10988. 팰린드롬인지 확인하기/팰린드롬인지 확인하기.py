n = list(input())
count = 0
for i in range(len(n)//2):
    if n[i] != n[len(n)-1-i]:
        count+=1

if count>=1:
    print("0")
else:
    print("1")