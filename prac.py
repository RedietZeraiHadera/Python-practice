# #Write a function that takes two numbers as input and returns their sum.
# def sum(num1,num2):
#     return num1+num2
# result = sum(5, 10)
# print(result)
# Write a function that takes a string as input and returns the length of the string.
def string_length(str):
    return len(str)
result1 = string_length("Hello World")
print(result1)

# Write a function that takes a list of numbers as input and returns the average of the numbers.
def sum_numbers(*args):
    sum = 0
    for arg in args:
        sum+=arg
        avg = sum/len(args)
    return avg
# Write a function that takes a string as input and
# returns True if the string is a palindrome, and False otherwise.    
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    return s == s[::-1]
# Write a function that takes a list of numbers as input 
# and returns the maximum number in the list.
def max_number(*numbs):
    max = numbs[0]
    for numb in numbs:
        if numb> max:
            max = numb
    return max        
# Write a function that takes a list of numbers as 
# input and returns the minimum number in the list.
def min_number(*nums):
    min = nums[0]
    for num in nums:
        if num<min:
            min = num
    return min        
# A function named concatenate_args that takes any number of string arguments in
# positional arguments format and concatenates them into a single string       
def concatenate_args(*str):
    new = ""
    for s in str:
        new+=s
    return new    
# A function named concatenate_kwargs that takes any number of string arguments in 
# keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    newest =""
    for key,value in kwargs.items():
        newest+=value
    return newest    
# Write a function that takes a list of numbers as input and returns a new list with all duplicate numbers removed.
def remove_duplicates(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique      
numbers = [1,2,1,2,3,4,3,4,5,6,7,8]
unique = remove_duplicates(numbers) 
print(unique)
# Write a program that creates a list of integers from 1 to 10,
# and then prints the sum of all the even numbers in the list.
def even_numbers(nums):
    even = []
    for num in nums:
        if num%2==0:
            even.append(num)
    return even
nums = range(1,11)        
even = (even_numbers(nums))
print(even) 
# Write a program that prompts the user to enter a sentence,
# and then prints out a list of all the unique words in the sentence 
# (i.e., no word should appear twice in the list).


# Write a function to reverse a string in Python 
# without using any built-in functions.
def reverse_join(s):
    s1 = ''.join(reversed(s))
    return s1
res = reverse_join('loving')
print(res)
   

# Write a Python function to find the sum of all the elements in a list.
def sum1(*nums1):
    sum = 0
    for n in nums1:
        sum+=n
    return sum    
summed = sum1(1,2,3,4,5)
print(summed)

# Write a Python function to find the largest element in a list.
def largest_element(*nums2):
    numlist = nums2[0]
    for n in nums2:
        if n>=nums2[0]:
            numlist=n
    return numlist
newlist = largest_element(1,2,3,5,8,9)
print(newlist)
        

# Write a Python function to create a set from a given list.
def create_set(*list1):
    newlist1 = set(list1)
    return newlist1
created = create_set(1,2,3,4,5)
print(created)
    
    
# Write a Python function to add an element to a set.
def add_to_set(set1,element):
    
    set1.add(element)
    return set1
setnew = {1,2,3}
set2 = add_to_set(setnew,4)
print(set2)

# Write a Python function to create an empty dictionary.
def empty_dictionary():
    my_dict ={}
    return my_dict
empty_dict = empty_dictionary()
print(empty_dict)


# Write a Python function to add an element to a dictionary.
def add_to_dictionary(my_dict,key,value):
    my_dict[key] = value
my_dict = {'name':'Rediet','age':22}
add_to_dictionary(my_dict,'counry','Ethiopia')
print(my_dict)
    









# def add_to_dictionary(my_dict,key,value):
#     my_dict[key] = value
# my_dict = {'a': 1, 'b': 2}
# add_to_dictionary(my_dict, 'c', 3)
# print(my_dict) 


 
    








    
    

    

    


        
    


    
