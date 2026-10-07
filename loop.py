#for loop

# num=int(input("enter the number : "))
# for i in range(num,11):                             #range from 0-10
#     print(i,end=" ")

# num=int(input("enter the number : "))
# for i in range(num,51):
#     if i%2==0:                                        #even number
#         print(i)

# num=int(input("enter the number : "))
# for i in range(num,51):
#     if i%2!=0:                                         #odd number
#         print(i)

# num1=int(input("enter a starting number : "))
# num2=int(input("enter an ending number : "))
# total_sum=0                                             #sum of numbers
# for i in range(num1,num2 +1):
#     total_sum+=i
# print(f"the sum of numbers from {num1} to {num2} is : {total_sum} ")


# num=int(input("enter the number : "))
# for i in range(1,11):                                    #multiple table
#     print(f"{num} * {i} = {num * i}")

# num=int(input("enter the number : "))
# factorial=1
# for i in range(1,num +1):                                  #factorial
#     factorial*=i
# print(f"the factorial of {num} is {factorial}")

# count=0
# for i in range(1,101):
#     if i%3==0:                                    #count
#         print(i,end=" ")


# num=int(input("enter the number : "))
# reverse=0
# for i in range(len(str(num))):
#     digit= num%10                                 #reverse number
#     reverse= reverse*10 + digit
#     num= num// 10
# print("reversed number is : ", reverse)

# num1=int(input("enter the number : "))
# num2=int(input("enter the number : "))
# even_sum=0
# for i in range(num1,num2 +1):                       #even sum
#     if i%2==0:
#         even_sum += i
# print(f"the sum of number from {num1} to {num2} is : {even_sum}")

# for i in range(1,11):
#     print(f"square of {i} is : {i**2}")             #square root


#while loop

# num=0
# while num<10:
#     num=num+1                             #num 1-10
#     print(num)

# num1=int(input("enter the number : "))
# num2=int(input("enter the number : "))
# while num1<=num2:
#     if num1%2==0:                         #even number
#         print(num1)
#     num1=num1 +1


# num1=int(input("enter the number : "))
# num2=int(input("enter the number : "))
# start_num=num1                                        #sum of numbers
# total_sum=0
# while num1<=num2:
#     total_sum += num1
#     num1 += 1
# print(f"the sum of number from {start_num} to {num2} is : {total_sum}")

# num=int(input("enter the number : "))
# i=1
# while i in range(1,11):                         # multiple table
#     print(f"{num} * {i} = {num * i }")
#     i+=1

# num=int(input("enter the number : "))
# factorial=1
# i=1
# while i in range(1,num+1):                               #factorial
#     factorial*=i
#     i+=1
# print(f"factorial of {num} is {factorial} ")

# num1=int(input("enter the number : "))
# num2=int(input("enter the number : "))
# i=num1
                                                #reverse counting
# while i>=num2:
#     print(i,end=" ")
#     i-=1


# num=int(input("enter the number : "))
# count=0
# while num!=0:                                            #count digits
#     num=num // 10
#     count+=1
# print(f"the number of digits of the number are {count}")


# num=int(input("enter the number : "))
# total=0
# while num!=0:                                       #sum of digits
#     digits= num%10
#     total=total+digits
#     num=num // 10
# print(f"sum of the digits are {total}")

# num=int(input("enter the number : "))
# reverse=0
# i=num
# while num!=0:                                              #reverse number
#     digits=num%10
#     reverse=reverse*10 +digits
#     num=num // 10
# print(f"the reverse of {i} is {reverse}")

# total=0
# while True:
#     num=int(input("enter the number : "))
#     if num==0:
#         break                                                   #sum till 0
#     total=total+num
# print(f"the sum is {total}")



# while True:
#     print("1.add")
#     print("2.sub")
#     print("3.mul")
#     print("4.div")
#     print("5.exit")

#     choice=int(input("enter your choice : "))

#     if choice==1:
#         number1=int(input("enter the first number : "))
#         number2=int(input("enter the second number : "))
#         answer=number1+number2
#         print(answer)
#     elif choice==2:
#         number1=int(input("enter your first number : "))
#         number2=int(input("enter the second number : "))
#         answer=number1-number2
#         print(answer)
#     elif choice==5:
#         break


