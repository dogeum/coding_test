def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    total_day = b-1
    for i in range(a - 1):
        total_day += day[i]
    return week[total_day % 7]