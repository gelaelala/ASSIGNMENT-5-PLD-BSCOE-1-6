grade = float(input("Enter grade: "))

if grade >= 96.5 and grade <= 100.0:
    print(1.0)
    print ("Excellent")
else:
        if grade >= 93.5 and grade <= 96.4:
            print (1.25)
            print ("Excellent")
        else:
            print ("Others")