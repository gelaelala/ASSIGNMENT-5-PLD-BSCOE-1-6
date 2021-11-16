grade = float(input("Enter grade: "))

if grade <= 64.4:
    print ("Invalid input. Please try again.")
else:
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
                        if grade >= 81.5 and grade <= 84.4:
                            print ("Your grade is: 2.25")
                            print ("Description: Good")
                        else:
                            if grade >= 78.5 and grade <= 81.4:
                                print ("Your grade is: 2.5")
                                print ("Description: Satisfactory")
                            else:
                                if grade >= 75.5 and grade <= 78.4:
                                    print ("Your grade is 2.75")
                                    print ("Description: Satisfactory")
                                else:
                                    if grade >= 74.5 and grade <= 75.4:
                                        print ("Your grade is: 3.0")
                                        print ("Description: Passing")
                                    else:
                                        if grade >= 64.5 and grade <= 74.4:
                                            print ("Your grade is: 5.0")
                                            print ("Description: Failure")
                                        else:
                                            print ("Others")