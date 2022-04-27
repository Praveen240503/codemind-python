# Give the number as user input using int(input()) function and store it in a variable.
numb = int(input())
# Take a variable say 'count' and initialize its value with '0'.
count = 0
# Loop from 0 to above-given number using for loop. 
for itr in range(numb):
    # Inside the loop, check if the product of the iterator value and iterator+1 value
    # (consecutive integers) is equal to the given number using the if conditional statement.
    if itr * (itr + 1) == numb:
        # If the statement is true, then increment the value of count (i.e. 1),
        # give the break condition and come out of the loop.
        count = 1
        break
# Check if the value of count is equal to '1' using the if conditional statement.
if count == 1:
  # If the statement is true, then print "The given number is a pronic number".
    print("YES")
# Else print "The given number is Not a pronic number".
else:
    print("NO")