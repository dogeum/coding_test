def solution(s, n):
    answer=[]
    for i in range(len(s)):
        code = ord(list(s)[i])
        if code == 32:
            answer.append(chr(code))
        elif 65<=code<=90:
            if code+n>90:
                answer.append(chr(code+n-26))
            else:
                answer.append(chr(code+n))
        else:
            if code+n>122:
                answer.append(chr(code+n-26))
            else:
                answer.append(chr(code+n))
            
    return ''.join(answer)