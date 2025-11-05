from itertools import combinations
def solution(numbers):
    answer = []
    combi = combinations(numbers, 2)
    for i in combi:
        answer.append(i[0]+i[1])
    return sorted(set(answer))