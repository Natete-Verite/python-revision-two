def attendance():
    held_classes = int(input("Enter number of classes held: "))
    attended_classes = int(input("Enter number of classes attended: "))
    percentage = (attended_classes/held_classes)*100
    print(f"You attended the class {percentage} percent")
    if percentage > 75:
        print("You are allowed to sit for the exam")
    else:
        print("You are not allowed to sit for the exam")    
attendance()        