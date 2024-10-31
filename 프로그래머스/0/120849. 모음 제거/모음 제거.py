def solution(my_string):
    
    for i in 'aeiou':
        my_string = my_string.replace(i, '')
    return my_string