while True:
    print("\n\nMENU\n")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Floor Division\n7. Exponentiation\n8. Exit")
    ch = int(input("Enter your choice: "))
    if(ch==1):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("The sum of",a,",",b,"is",a+b)
    elif (ch==2):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("The difference of",a,",",b,"is",a-b)
    elif (ch==3):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("The product of",a,",",b,"is",a*b)
    elif(ch==4):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if(b==0):
            print("Division by zero!!!")
            b = int(input("Enter the second number: "))
            print("The quotient got when",a,"divided by",b,"is",a/b)
        else:
            print("The quotient got when",a,"divided by",b,"is",a/b)
    elif(ch==5):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if(b==0):
            print("Division by zero!!!")
            b = int(input("Enter the second number: "))
            print("The remainder got when",a,"divided by",b,"is",a%b)
        else:
            print("The remainder got when",a,"divided by",b,"is",a%b)
    elif(ch==6):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if(b==0):
            print("Division by zero!!!")
            b = int(input("Enter the second number: "))
            print("The integer quotient got when",a,"divided by",b,"is",a//b)
        else:
            print("The integer quotient got when",a,"divided by",b,"is",a//b)
    elif(ch==7):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a,"power",b,"is",a**b)
    elif(ch==8):
        print("Thank you")
        break
    else:
        print("Invalid option try again!!!")



        
        
        
            
            
            
        
        
        
