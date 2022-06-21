def ages():
    first = int(input("Enter the first age: "))
    second = int(input("Enter the second age: "))
    third = int(input("Enter the third age: "))
    print(f"the oldest age is {max(first,second,third)} and the youngest age is {min(first,second,third)}")
ages()    