Age = int(input("Enter age: "))

if Age > -1 and Age <= 12:
    print ("Kid")
else:
    if Age >= 13 and Age <= 17:
        print ("Teen")
    else:
        print ("Others")