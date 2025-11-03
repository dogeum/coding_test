from itertools import combinations
def solution(d, budget):
    count=0
    a = 0
    for i in sorted(d):
        a += i
        
        if a > budget:
            break
            
        count += 1
        
    return count