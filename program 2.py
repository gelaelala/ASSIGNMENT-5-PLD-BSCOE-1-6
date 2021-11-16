
def getnumbers():
    firstnumber = int(input("Enter first number: "))
    secondnumber = int(input("Enter second number: "))
    thirdnumber = int(input("Enter third number: "))
    return firstnumber, secondnumber, thirdnumber

def lowestnumber(firstnum, secondnum, thirdnum):
    if firstnum < secondnum and firstnum < thirdnum:
        return firstnum
    else:
        if secondnum < thirdnum:
           return secondnum
        else:
             return thirdnum

def display (lowest_number):
    print (f"{lowest_number} is the smallest number.")

first_num, second_num, third_num = getnumbers()

lowestnum = lowestnumber(first_num, second_num, third_num)

display (lowestnum)