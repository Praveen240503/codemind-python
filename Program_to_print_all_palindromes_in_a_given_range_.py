gvn_lowrlmt = int(input())
gvn_upprlmt = int(input())

for m in range(gvn_lowrlmt, gvn_upprlmt+1):
    
    given_num = m
   
    duplicate_num = given_num
    reverse_number = 0
    
    while (given_num > 0):
        
        remainder = given_num % 10
        reverse_number = (reverse_number * 10) + remainder
        given_num = given_num // 10
 
    if(duplicate_num == reverse_number):
    
        print(duplicate_num, end=" ")