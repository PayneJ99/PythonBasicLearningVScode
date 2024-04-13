import math


#testing github updates


def listSort(l):
    tempVal = input("How would you like to sort the list? Asc Desc None")
    
    if tempVal == "Asc" or "asc":
        l.sort()
    elif tempVal == "Desc" or "desc":
        l.sort(reverse=True)
    elif tempVal == "None" or "none":
        pass
    else:
        print("that is not one of the accepted values please try again")
        listSort(l)


def listAdd(l):
    tempVal = input("please add what you would like added to the list one at a time" "\n")
    l.append(tempVal)
    YorN = str(input("would you like to add another value? Y or N" "\n"))
    if YorN == "Y" or "y":
        listAdd(l)
    elif YorN == "N" or "n":
        listSort(l)
    else:
        pass
    
    
def convertRtoD(Rval):
    return (Rval)*(180/math.pi)

def calculator(valOne, valTwo, Operator):

    if Operator == "multiply" or "mult" or "Mult" or "Multiply" or "x" or "X" or "*":
        calcedVal = valOne * valTwo
        Operator = "x"
    elif Operator == "Divide" or "divide" or "Div" or "div" or "/":
        calcedVal = valOne / valTwo
        Operator = "/"
    elif Operator == "Add" or "add" or "+":
        calcedVal = valOne + valTwo
        Operator = "+"
    elif Operator == "Subtract" or "subtract" or "-" or "sub" or "Sub":
        calcedVal = valOne - valTwo
        Operator = "-"
    else: 
        print("that is not a valid option please try again")
        calculator(valOne, valTwo, Operator)
    print(valOne + " " + Operator + " " + valTwo + "= " + calcedVal)





print("Select what you would like to do:" "\n")

Option = input("1: Convert radians to degrees" "\n"
"2: Sort a list" "\n""3: Basic Calculator" "\n")

match Option:
    case "1":
        printValue = float(input("What number would you like to convert?" "\n"))
        printValue = convertRtoD(printValue)
        print("This is your Value in Degrees: " + str(printValue) )
        
    case "2":
        unorderedList = []
        listAdd(unorderedList)
        print(unorderedList)

    case "3":
        valOne = float(input("What is the first number used in the calculation?" "\n"))
        operator = float(input("What is the second number used in the calculation?" "\n"))
        valTwo = float(input("What would you like to do to these values? options include multiply, divide, add, subtract" "\n"))
        calculator(valOne,valTwo,operator)
        
        