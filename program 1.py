grade = float(input("Enter grade: "))

if grade >= 96.5 and grade <= 100.0:
    print("Your grade is: 1.0")
    print ("Description: Excellent")
else:
        if grade >= 93.5 and grade <= 96.4:
            print ("Your grade is: 1.25")
            print ("Description: Excellent")
        else:
            if grade >=90.5 and grade <= 93.4:
                print ("Your grade is: 1.5")
                print ("Description: Very Good")
            else:
                if grade >= 87.5 and grade <= 90.4:
                    print ("Your grade is: 1.75")
                    print ("Description: Very Good")
                else: 
                    if grade >= 84.5 and grade <= 87.4:
                        print ("Your grade is: 2.0")
                        print ("Description: Good")
                    else:
                        print ("Others")