def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b
def Modulus(a,b):
    return a%b
def Exponent(a,b):
    return a**b

while True:
    print("""
Calculator:

Addition(+)
Subtraction(-)
Multiplication(*)
Division(/)
Modulus(%)
Exponent(**)
""")

    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    op=input("Enter operation[Add/Sub/Mul/Div/Mod/Exp]: ")

    match op:
        case "Add":
            print(Addition(a,b))
        case "Sub":
            print(Subtraction(a,b))
        case "Mul":
            print(Multiplication(a,b))
        case "Div":
            print(Division(a,b))
        case "Mod":
            print(Modulus(a,b))
        case "Exp":
            print(Exponent(a,b))
        case "default":
            print("Invalid Operator")

    rep = input("\nRepeat?[y/n]: ")  # Continuous input to calculator until explicitly stopped
    if rep.lower()=="n":
        break