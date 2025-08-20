def solution(my_string):
    answer = []
    
    for i in range(0, len(my_string)):
        char = my_string[i]
        
        if char.isdigit():
            answer.append(int(char))
        
    answer.sort()
    
    return answer