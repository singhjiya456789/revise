# #Calculator
# while True:
#     print("1.ADD")
#     print("2.Substract")
#     print("3.Multiply")
#     print("4.Divide")

#     choice=input("Enter the choice between 1-4:")
#     if choice =="1":
#         a=int(input("Enter the 1st no.:"))
#         b=int(input("Enter the 2nd no.:"))
#         print("Result:",a+b)
#     elif choice == "2":
#         a=int(input("Enter the 1st no.:"))
#         b=int(input("Enter the 2nd no.:"))
#         print("Result:",a-b)
#     elif choice == "3":
#         a=int(input("Enter the 1st no.:"))
#         b=int(input("Enter the 2nd no.:"))
#         print("Result:",a*b)
#     elif choice == "4":
#         a=int(input("Enter the dividend no. :"))
#         b=int(input("Enter the divider no. :"))
#         print("Result:",a/b)
#         break
#     else:
#         print("Invalid choice!")
#     print()

#even odd 

# a= int(input("Enter the no. :"))
# if a %2 ==0:
#     print("even")
# else:
#     print("odd")

#student mark analysis
name=input("Enter the Student name:")

math=int(input("Enter the Math marks:"))
sci=int(input("Enter the science marks:"))
eng= int(input("Enter the English marks:"))
total=math+sci+eng
percent=(total/300)*100

print("TOtal MArks:",total)
print("Your PErcentage:",percent)

if percent >=90:
    print("you got A")
elif percent >=75:
    print("YOU got B")
elif percent >=50:
    print("YOu got C")
else:
    print("Failed")