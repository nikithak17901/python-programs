def circle():
    r = int(input("Enter the radius: "))
    print("Area of circle is", 3.14 * r * r)

def square(a):
    print("Area of square is", a * a)

def triangle():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    return 0.5 * b * h  # Triangle area formula

def rectangle(a, b):
    return a * b  # Rectangle area formula


while True:
    print("\n1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")
    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            a = int(input("Enter the side of square: "))
            square(a)
        case 2:
            circle()
        case 3:
            res = triangle()
            print("Area of the triangle is", res)
        case 4:
            a = int(input("Enter the length of rectangle: "))
            b = int(input("Enter the breadth of rectangle: "))
            res = rectangle(a, b)
            print("Area of the rectangle is", res)
        case 5:
            print("Exiting...")
            exit(0)
        case _:
            print("Invalid option")
