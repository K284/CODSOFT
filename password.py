import string
import random
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
punc = string.punctuation
g=1

s = list(upper+lower+digit+punc)
#print(s)
while g==1:
    l = int(input("\n\nEnter the length: "))
    print("\nYour password is: ")
    print("".join(random.sample(s,l)))
    g = int(input("\nDo you want to continue? (0/1): "))


print("Thank you")

