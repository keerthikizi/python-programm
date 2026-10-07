# class Car:                                                          #blueprint 
#     def __init__(self,brand,colour):                                #defining the attributes and special method to initialize an object when created
#         self.brand=brand                                            #stores the brand 
#         self.colour=colour                                          #stores the colour

#     def drive(self):                                                #defining the action/method
#         print(f"I love {self.colour} {self.brand} car so much")


# car1=Car("Audi" , "Black")                                          #datas
# car2=Car("Ciaz", "Red")

# print(car1.brand)                                                   #car1 brand is printed
# car2.drive()                                                        #car2 action is printed
# print(car2.colour)
# car1.drive()




# class Dog:
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#     def bark(self):
#         print(f"the dog of breed {self.breed} with name {self.name} barks so bad!")


# dog1=Dog("Ronny","Golden retriever")
# dog2=Dog("sirus","Husky")
# dog3=Dog("mark","lab")

# print(dog1.name)
# print(dog2.name)
# print(dog3.name)
# dog1.bark()
# dog2.bark()
# dog3.bark()
# print(dog1.breed)
# print(dog2.breed)
# print(dog3.breed)

# class students:
#     def __init__(self,name,age,course,city):
#         self.name=name
#         self.age=age
#         self.course=course
#         self.city=city
#     def exam(self):
#         print(f"{self.name} from {self.city} of {self.course} have attended the exam.")

# std1=students("keerthi",24,"MBA","Kollam")
# std2=students("Riya",25,"BBA","Kochi")
# std3=students("Sooraj",28,"BA","TVM")
# std4=students("Dhiya",24,"Bcom","EKM")

# print(std1.name)
# print(std2.age)
# print(std3.course)
# print(std4.city)
# std1.exam()
# std2.exam()
# std3.exam()
# std4.exam()

# class calculator:
#     def multiply(self,a,b):
#         return a*b
#     def addition(self,a,b):
#         return a+b
#     def subtraction(self,a,b):                 #method with parameters
#         return a-b
#     def division(self,a,b):
#         return a/b

# my_cal=calculator()
# print(my_cal.multiply(10,10))
# print(my_cal.addition(5,10))
# print(my_cal.subtraction(10,50))
# print(my_cal.division(10,2))


# class employee:
#     def __init__(self,name,dept,salary):
#         self.name=name
#         self.dept=dept
#         self.salary=salary
#     def display_details(self):
#         print("name : ",self.name,"\n","dept : ",self.dept,"\n","salary : ", self.salary)
#     def medical(self):
#         print(f"the medical checkup of {self.name} from {self.dept} department has been completed ")

# emp1=employee("keerthi","HR",25000)
# emp2=employee("Riya","safety",45000)
# emp3=employee("Sooraj", "logistics", 50000)
# # emp1.display_details()
# # emp1.medical()
# emp2.display_details()
# emp2.medical()




# class student:
#     def __init__(a,name):
#         a.name= name
# s= student("anu")
# print(s.name)


# class std:
#     def __init__(self):
#         print("student created")
# s=std()


# class Class:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age                          #parametized constructor
# s=Class("Keerthi",24)
# print(s.name)
# print(s.age)


# class parent:
#     def __init__(self):
#         print("parent constructor")
# class child(parent):
#     def __init__(self):
#         super().__init__()  
#         print("child constructor")

# c=child()