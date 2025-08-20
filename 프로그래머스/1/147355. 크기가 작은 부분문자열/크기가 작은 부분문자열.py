def solution(t, p):
    count = 0
    
    for i in range(0, len(t) - len(p) + 1):
        substring = t[i:i + len(p)]
        
        if int(substring) <= int(p):
            count += 1
    
    return count