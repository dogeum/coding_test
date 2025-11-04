def solution(s):
    answer = []
    answer.append(-1)
    for i in range(1, len(s)):
        last_index = s[:i].rfind(s[i])
        if last_index != -1:
            dis = i - last_index
            answer.append(dis)
        else:
            answer.append(-1)
        
        
    return answer