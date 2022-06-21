def bonus():
    salary = int(input("Enter your salary"))
    years = int(input("Enter years of service"))
    bonus = salary * 0.05
    sal= bonus + salary
    if years > 5:
       print(f"Your salary is {sal}")
    else:
        print(f"Your salary is {salary}")  
bonus()         