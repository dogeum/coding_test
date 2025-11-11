N = input()
long = len(N)//10
N = list(N)
for i in range(0, long):
    print(''.join(N[10*i:(i*10)+10]))
if (len(N)%10)!=0:
    print(''.join(N[(long*10):len(N)]))