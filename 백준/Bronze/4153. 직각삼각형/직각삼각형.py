while True:
    A, B, C = map(int, input().split(" "))
    if A==B==C==0:
        break
    else:
        triangle = [A, B, C]
        triangle = sorted(triangle)
        
        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
            print("right")
        else:
            print("wrong")