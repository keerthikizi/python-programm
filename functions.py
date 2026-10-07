# def add():
#     print(1+2)                 #declaration and definition
                               #without argument-without return

# add()                          #function calling


# def addition(a,b):
#     return a+b                 #with argument-with return

# num1=int(input("enter your first number : "))
# num2=int(input("enter your second number : "))

# answer=addition(num1,num2)
# print(answer)

# def addition(a,b):
#     print(a+b)                 #with argument-without return

# num1=int(input("enter your first number : "))
# num2=int(input("enter your second number : "))

# addition(num1,num2)

# def addition1234():
#     num1=int(input("enter your first number : "))
#     num2=int(input("enter your second number : "))
#     return(num1+num2)                 #without argument-with return


# answer=addition1234()
# print(answer)

# def course(name,course_name="data analytics"):
#     print(name,course_name)

# name="keerthi"                                  #default fn
# course_name="python"
# course(name,course_name)

# def total_marks(*args):                            #no limit to assign values to do operations
#     return sum(args)

# answer=total_marks(5,10,15,20,25)
# print(answer)

# def details(**a):
#     for key,value in a.items():                    #key-value pair
#         print(key,value)                           #**-stores in dict as key-value pair
#                                                    #*- stores in tuple
# details(name="keerthi",age=24,course="data analytics")


# x=10                 #global value-can be called anywhere
# def test():
#     print(x)

# test()
# print(x)               #will show error


# count=0
# def increase():
#     global count                   #global-direct access of value
#     count+=1
#     pass

# increase()
# print(count)


# water=float(input("enter the liter of water : "))
# if water<=100:
#     amount = water*5
# elif water<=200:
#     amount=(water*5)+((water-100)*10)
# else:
#     amount=(water*5)+(water*10)+((water-100)*20)

# print("liter used : ",water)
# print("amount : ", amount)

