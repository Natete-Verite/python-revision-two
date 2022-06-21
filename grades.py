def students_grades():
    student = int(input("Enter your grades: "))
    if student < 25:
        print("F")
    elif student >= 26 and student <= 45:
        print("E")   
    elif student >= 46 and student <= 50:
        print("D")     
    elif student >= 51 and student <= 60:
        print("c")  
    elif student >= 61 and student <= 79:
        print("B")  
    elif student >= 80:
        print("A")                    
students_grades()        