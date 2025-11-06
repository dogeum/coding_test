def solution(name, yearning, photo):
    answer = [0]*len(photo)
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                answer[i]+=yearning[name.index(photo[i][j])]
    return answer