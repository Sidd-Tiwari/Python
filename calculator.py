first_number = int(input("Enter first number :"))
operator = input("Enter an operator(+,-,*,%,/)")
second_number = int(input("Enter second number :"))
if operator=="+":
    print("ans",first_number + second_number)
elif operator=="-":
    print(first_number - second_number)
elif operator=="*":
    print("ans",first_number * second_number)
elif operator=="%":
    print("ans",first_number % second_number)
elif operator=="/":
    print("ans",first_number / second_number)
else:
    print("Invaliid operator ")

