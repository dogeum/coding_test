def solution(score):
    answer = []
    answersort=[]
    result = []

    for i in range(len(score)):
        answer.append(sum(score[i])/2)
        answersort.append(sum(score[i])/2)
    for i in answer:
        result.append(sorted(answer, reverse=True).index(i)+1)

    return result