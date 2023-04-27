#Write a function that takes two numbers as input and returns their sum.
def sum(a,b):
    return a+b
answer = sum(5,6)
print(answer)
# Write a function that takes a string as input and returns the length of the string.
def length_of_string(str):
    return len(str)
length_str = length_of_string("Ruhama")
print(length_str)
# Write a function that takes a list of numbers as input and returns the average of the numbers.
def avrg(list1):
    return sum(list1) / len(list1)
list_of_no = [12,13,14,15]
avg = avrg(list_of_no)
print(avg)    

# Write a function that takes a list of numbers as input 
# and returns the maximum number in the list.

# A function named concatenate_args that takes any number of string arguments in
# positional arguments format and concatenates them into a single string 

# Write a function that takes a list of numbers as input and 
# returns a new list with all duplicate numbers removed.

# Write a program that creates a list of integers from 1 to 10,
# and then prints the sum of all the even numbers in the list.
def even_sum(numms):
    even = 0
    for n in numms:
        if n%2==0:
            even+=n
    return even
numms = range(1,11)
print(even_sum(numms))
        


        
    
        
        

