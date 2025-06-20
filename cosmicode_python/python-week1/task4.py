def ellipse():
    a=float(input("Enter the value of a: "))
    b=float(input("Enter the value of b: "))
    area=3.14*a*b
    print("Area of ellipse is(πab): ",area)
    print()
    return

def trapezoid():
    a=float(input("Enter the value of a: "))
    b=float(input("Enter the value of b: "))
    h=float(input("Enter the value of height: "))
    area=((a+b)/2)*h
    print("Area of trapezoid((a+b)/2 * h): ",area)
    print()
    return

def Torus():
    r=float(input("Enter the value of r: "))
    R=float(input("Enter the value of R: "))
    area=(2*3.14*r)*(2*3.14*R)
    print("Area of Torus (2πR)(2πr): ",area)
    print()
    return

def Octahedron():
    a=float(input("Enter the value of a: "))
    area=2*1.7321*a*a
    print("Area of Octahedron (2*√3* a^2): ",area)

def main():
    while(True):
        print("1- Ellipse")
        print("2- Trapezoid")
        print("3- Torus")
        print("4- Octahedron")
        print("5- exit")
        choice = int(input("Enter your choice: "))
        if choice==1:
            ellipse()
        elif choice==2:
            trapezoid()
        elif choice==3:
            Torus()
        elif choice==4:
            Octahedron()
        elif choice==5:
            exit()
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
        