def ternary(n):
    result = ""
    while n > 0:
        result = str(n%3) + result
        n //= 3
    return result or "0"

def solution(n):
    return int((str(ternary(n))[::-1]), 3)