# def add(a):
#     if a==5:                             #recurssion
#         return 0
#     else:
#         print(a)
#         add(a+1)                         #function call itself

# add(1)



# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))

# num=3
# print("the factorial of",num,"is" ,factorial(num))




# def prefix(strings):
#     if not strings:
#         return ""
    
#     prefix=strings[0]

#     for word in strings[1:]:
#         while not word.startswith(prefix):
#             prefix=prefix[:-1]

#             if prefix=="":                                #prefix
#                 return ""


#     return prefix

# words=list(map(str , input("enter the list of words to find the common prefix : ").split(",")))
# result=prefix(words)
# if result:
#     print("longest prefix among the list is ",result)
# else:
#     print("no common prefix")



# def pattern(n):
#     alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for i in range(n):
#         char=alphabet[i]

#         for j in range(n-i-1):                  #pattern
#             print("", end=" ")
#         for k in range(i + 1):
#             print(char,end=" ")
#         print()

# answer=pattern(5)
# print(answer)



