#SETTING FUNCTION
function = int(input('''
Please select one of the followings:
1 = Addition
2 = Subtraction
3 = Multiplication
4 = Division
'''))
if 0 < function < 5:

    #DEFINING NUMBER1
    number_1 = input('Enter your first number: ')
    
    #DEFINING NUMBER2 FOR DIVISION
    if function == 4:
        number_2 = input("Enter your second number, It can't be 0: ")
        if number_2 == "0":
            print('Error incorrect input of second number')
            exit()
        else:
            pass
    elif function != 4:   
    
    #DEFINING NUMBER2 FOR OTHER FUNCTIONS
        number_2 = input('Enter your second number: ')
    else:
        pass
            

    #OPERATION ADDITION
    if function == 1:
        print(str(number_1) + " + " + str(number_2) + " =", int(number_1) + int(number_2))

    #OPERATION SUBTRACTION
    elif function == 2:
        print(str(number_1) + " - " + str(number_2) + " =", int(number_1) - int(number_2))

    #OPERATION MULTIPLICATION
    elif function == 3:
        print(str(number_1) + " * " + str(number_2) + " =", int(number_1)* int(number_2))

    #OPERATION DIVISION
    elif function == 4:
        print(str(number_1) + " / " + str(number_2) + " =", int(number_1) / int(number_2))
    #IF AND ELSE
    else:
        print ("Error incorrect input")

else:
    print("Error incorrect input")    
    
