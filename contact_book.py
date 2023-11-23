import csv
r = ["Name","Ph no", "Email","Address"]
def add(row):
    r = ["Name","Ph no", "Email","Address"]
    with open("contacts.csv",'a', newline = "\n") as f:
        writer = csv.writer(f, delimiter = ',', quotechar = " ")
        writer.writerow(row)
        
            
def view():
    with open("contacts.csv","r",newline="\n") as f:
        data = csv.reader(f)
        for row in data:
            print("\nName:",row[0])
            print("Phone number:",row[1])
            print("Email:",row[2])
            print("Address:",row[3])
def search(p):
    with open("contacts.csv","r",newline="\n") as f:
        data = csv.reader(f)
        for row in data:
            if (p == row[0]) or (p in row[1]):
                print("\nName:",row[0])
                print("Phone number:",row[1])
                print("Email:",row[2])
                print("Address:",row[3])
                break
        else:
            print("Not found. Try again")
    
    
def update(g):
    i=0
    new = []
    a=""
    with open("contacts.csv","r",newline = '\n') as f:
        reader = csv.reader(f)
        data = reader
        
        if g.lower() == "name":
            a = input("Enter the old name: ")
            x = input("Enter the new name: ")
            i=0
            
            for row in data:
                new.append(row)
            for ggg in new:
                if ggg[i]==a:
                    ggg[i] = x.strip()
                    print("\nSuccessfully updated")
                    break
            else:
                print("Details not found try again")
            
        elif g.lower() == "phno":
            x = input("Enter the old phone number: ")
            x = input("Enter the new phone number: ")
            i=1
            new = []
            for row in data:
                new.append(row)
            for ggg in new:
                if a in ggg[i]:
                    ggg[i] = x.strip()
                    print("\nSuccessfully updated")
                    break
            else:
                print("Details not found try again")
            
        elif g.lower() == "email":
            a = input("Enter the old email id: ")
            x = input("Enter the new email id: ")
            i=2
            new = []
            for row in data:
                new.append(row)
            for ggg in new:
                if a in ggg[i]:
                    ggg[i] = x.strip()
                    print("\nSuccessfully updated")
                    break
            else:
                print("Details not found try again")
            
        elif g.lower()== "address":
            a = input("Enter the old address: ")
            x = input("Enter the new address: ")
            i=3
            new = []
            for row in data:
                new.append(row)
            for ggg in new:
                if a in ggg[i]:
                    ggg[i] = x.strip()
                    print("\nSuccessfully updated")
                    break
            else:
                print("Details not found try again")
            
        else:
            print("Wrong option try again!")

    with open("contacts.csv","w",newline = '\n') as f:
        writer = csv.writer(f, delimiter =",", quotechar = " ")
        writer.writerows(new)      
        
        
            
        
                
            
    

def delete():
    new = []
    with open("contacts.csv","r",newline = '\n') as f:
        writer = csv.writer(f, delimiter = "," , quotechar = " ")
        dell = input("Enter the name to delete the record: ")
        reader = csv.reader(f)
        data = reader
        i=0
        
        for row in data:
            if dell not in row:
                new.append(row)
    with open("contacts.csv","w",newline = '\n') as f:
        writer = csv.writer(f, delimiter =",", quotechar = " ")
        writer.writerows(new) 
                
        
    print("\nSuccessfully deleted")
            
        

record=[]
while True:
    print("\n\nCONTACT BOOK")
    print("\nMENU")
    print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
    ch = int(input("\nEnter your choice: "))
    if ch==1:
        n = int(input("Enter the number of contacts you want to save: "))
        for i in range(n):
            name = input("\nEnter the name: ")
            phno = input("Enter the phone number along with country code (+91 999999999): ")
            email = input("Enter the email id: ")
            address = input("Enter the permanent address: ")
            record=[name,phno,email,address]
            add(record)
            print("Successfully saved!!!!")
    elif ch ==2:
        view()
    elif ch ==3:
        norph = input("Enter name or phone number to search: ")
        search(norph)
    elif ch == 4:
        g = input("Which one you want to update?(name, phno, email, address):")            
        update(g)
    elif ch == 5:
        delete()        
    elif ch ==6:
        break
        
