
def sum():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Sum: " + str(a + b))

def diff():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Difference: " + str(a - b))

def mult():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Product: " + str(a * b))

def div():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Division: " + str(a / b))

print("Enter your choice")
print("Press 1: Addition\n2: Subtraction\n3: Multiplication\n4: Division")
choice = int(input())

if choice == 1:
    sum()
elif choice == 2:
    diff()
elif choice == 3:
    mult()
elif choice == 4:
    div()
