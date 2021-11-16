def getnumbers ():
    firstnumber = int(input("Enter first number: "))
    secondnumber = int(input("Enter second number: "))
    thirdnumber = (input("Enter third number: "))
    return firstnumber, secondnumber, thirdnumber

def lowestnumber (firstnum, secondnum, thirdnum):
    if firstnum < secondnum:
        if firstnum < thirdnum:
            lowestnum = firstnum
            print (firstnum,"is the smallest number.")
        else:
            lowestnum = thirdnum
            print (thirdnum, "is the smallest number.")

first_number, second_number, third_number = getnumbers()