def solution(number, limit, power):
    count = [0] * (number+1)
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            count[j]+=1
            
    total = 0
    
    for k in range(1, number+1):
        personal_power = count[k]
        if personal_power>limit:
            final = power
        else:
            final = personal_power
        total += final
    
    return total