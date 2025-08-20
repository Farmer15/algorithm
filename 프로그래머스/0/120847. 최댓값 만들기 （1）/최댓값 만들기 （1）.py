def solution(numbers):
    max_number = 0
    
    for number in numbers:
        if number >= max_number:
            max_number = number
    
    next_number = 0
    count = 1
    
    for number in numbers:
        if number == max_number and count == 1:
            count -= 1
            continue
        
        if number >= next_number:
            next_number = number
    
    return max_number * next_number