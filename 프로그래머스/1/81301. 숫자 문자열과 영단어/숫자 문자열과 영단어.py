def solution(s):
    answer = ''
    temp = ''
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_al = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    letter = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in number_al:
                answer += str(number_al.index(temp))
                temp = ''
            
        
    return int(answer)