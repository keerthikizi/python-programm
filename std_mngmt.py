# std={}
# while True:
#     print("1.add student")
#     print("2.view student")
#     print("3.update student")
#     print("4.delete student")
#     print("5.view all student")
#     print("6.exit")

#     choice=int(input("enter your choice : "))

#     if choice==1:

#         phn_no=int(input("enter your phone number : "))
#         if phn_no in std:
#             print("phone number already exists!")
#             continue

#         name=str(input("enter your name : "))
#         age=int(input("enter your age : "))
#         email=str(input("enter your mail id : "))
#         city=str(input("enter your city : "))
#         std[phn_no]={"name" : name, "phone number" : phn_no, "age" : age, 
#                      "email" : email, "city" : city}

#         print("student added successfully!")
#     elif choice==2:
#         phn_no=int(input("enter the phone number : "))

#         if phn_no in std:
#             print(f"name : {std[phn_no]['name']}")
#             print(f"phone number : {std[phn_no]['phone number']}")
#             print(f"age : {std[phn_no]['age']}")
#             print(f"email : {std[phn_no]['email']}")
#             print(f"city : {std[phn_no]['city']}")
#         else:
#             print("student data not found!")

#     elif choice==3:
#         phn_no=int(input("enter the number : "))

#         if phn_no in std:
#             print("if you don't have anything to update, please press enter")
#             i=std[phn_no]
#             new_name=str(input("enter the changed name : "))
#             new_age=input("enter the changed age : ")
#             new_email=str(input("enter the updated email : "))
#             new_city=str(input("enter the changed city : "))

#             if new_name:i['name']=new_name
#             if new_age:i['age']=int(new_age)
#             if new_email:i['email']=new_email
#             if new_city:i['city']=new_city
#             print("student details updated successfully!")
#         else:
#             print("not found!")

#     elif choice==4:
#         phn_no=int(input("enter the phone number of the student that need to be removed : "))

#         if phn_no in std:
#             del std[phn_no]
#             print("student data is deleted")
#         else:
#             print("student phnone number mismatched!")

#     elif choice==5:
#         for phn,s in std.items():
#             print(f"name : {s['name']}")
#             print(f"phone number : {s['phone number']}")
#             print(f"age : {s['age']}")
#             print(f"email : {s['email']}")
#             print(f"city : {s['city']}")
#         else:
#             print("no student records found!")

#     else:
#         break

    




        
