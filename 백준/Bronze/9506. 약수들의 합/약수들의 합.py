import sys
input = sys.stdin.readline

a = int(input())

while a!=-1:
    b = []
    for i in range(1, a):
        if a%i == 0:
            b.append(i)

    
    if sum(b) == a:
        print(a, "=", ' + '.join(map(str, b)))
    else:
        print(a, "is NOT perfect.")
    a = int(input())