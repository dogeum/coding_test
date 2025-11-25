def solution(s, skip, index):
    alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in skip]
    
    result = []
    L = len(alpha)
    
    for ch in s:
        pos = alpha.index(ch)
        new_pos = (pos + index) % L
        result.append(alpha[new_pos])
    
    return ''.join(result)
