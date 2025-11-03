def solution(s):
    answer = []
    s_list = s.split(' ')
    for i in range(len(s_list)):
        new_word = ""
        for j in range(len(s_list[i])):
            a = s_list[i][j]
            
            if j%2 == 0:
                new_word += a.upper()
            else:
                new_word += a.lower()
        s_list[i] = new_word
        answer.append(new_word)
    
    return ' '.join(answer)