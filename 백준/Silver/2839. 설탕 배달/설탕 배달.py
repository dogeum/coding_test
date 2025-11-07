N = int(input())
def sugar(N):
    five = N//5
    if N %5 == 0:
        return five
    while five>=0:
        remain = N-(5*five)
        if remain % 3 == 0:
            three = (N-5*five)//3
            return five + three
        else:
            five-=1
    return(-1)

print(sugar(N))