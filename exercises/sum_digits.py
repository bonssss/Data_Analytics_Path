def sum_of_digits(num: int):
    # num will be an integer 
    total=0
    
    for i in  str(num):
        total += int(i)
        
        
        
    return  total

print(sum_of_digits(234))