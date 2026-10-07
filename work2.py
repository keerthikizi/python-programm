# def factorial(n):
#     fact=1
#     for i in range(1,n+1):                             #factorial
#         fact=fact*i
#     return fact

# num=int(input("enter a number to find it's factorial : "))
# result=factorial(num)
# print(f"factorial of {num} = {result}")


# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):                           #prime
#         n%i==0
#         return False
#     return True

# num=int(input("enter a number : "))
# result=is_prime(num)
# print(result)


# def count_vowels(text):
#     count=0
#     for i in text:
#         if i in "aeiouAEIOU":                              #count vowels
#             count=count + 1
#     return count

# text=str(input("enter a word or sentence : "))
# result=count_vowels(text)
# print(result)


# def reverse_string(text):
#     reverse=""

#     for i in text:
#         reverse=i+reverse                            #reverse
#     return reverse

# text=str(input("enter a word or a sentence : "))
# result=reverse_string(text)
# print(f"the reverse of {text} is : ({result})")



# def is_palindrom(text):
#     reverse=""

#     for i in text:
#         reverse=i + reverse                          #palindrom

#     if text==reverse:
#         return True
#     else:
#         return False

# text=str(input("enter a string : "))
# result=is_palindrom(text)
# print(result)


# def list_sum(numbers):
#     total=0

#     for i in numbers:
#         total=total + i                   #sum of numbers
#     return total

# numbers=list(map(int, input("enter a numbers to find their sum : ").split(",")))
# answer=list_sum(numbers)
# print(answer)


# def find_largest(numbers):
#     largest=numbers[0]

#     for i in numbers:
#         if i>largest:
#             largest=i                         #largest value

#     return largest

# numbers=list(map(int, input("enter the list of numbers to find the maximin among : ").split(",")))
# answer=find_largest(numbers)
# print(f"the largest among the list is : {answer}")



# def count_even(numbers):
#     count=0

#     for i in numbers:
#         if i%2==0:
#             count= count + 1                    #even numbers
#     return count

# numbers=list(map(int, input("enter the list of numbers : ").split(",")))
# answer=count_even(numbers)
# print(f"the list has '{answer}' number of even numbers")


# def multiplication_table(n):
#     for i in range(1,11):
#         print(n, "x" , i, "=" , n*i)               #multiple table

# num=int(input("enter the number : "))
# multiplication_table(num)


# def calculate_result(mark1,mark2,mark3):
#     average=(mark1+mark2+mark3)

#     if average>=50:
#         return "Pass"                             #average marks
#     else:
#         return "Fail"

# mark1=float(input("enter the first mark : "))
# mark2=float(input("enter the second mark : "))
# mark3=float(input("enter the third mark : "))

# result=calculate_result(mark1,mark2,mark3)
# print(result)


# def is_disarium(n):
#     total=0
#     num_str=str(n)

#     for i,char in enumerate(num_str):
#         digits=int(char)
#         position=i+1
#         total+=digits**position                      #disarium number

#     return total==n

# num=int(input("enter the number : "))
# if is_disarium(num):
#     print(f"{num} is a disarium number")
# else:
#     print(f"{num} is not a disarium number")


# def reverse(s):
#     vowels="aeiouAEIOU"
#     char=list(s)
#     left=0
#     right=len(char)-1

#     while left<right:

#         if char[left] not in vowels:                    #reverse vowels
#             left+=1
#         elif char[right] not in vowels:
#             right-=1
#         else:
#             char[left],char[right]=char[right],char[left]
#             left+=1
#             right-=1

#     return"".join(char)
# string=str(input("enter the word or sentence : "))
# result=reverse(string)
# print(f"the reverse of {string} is '{result}'")


