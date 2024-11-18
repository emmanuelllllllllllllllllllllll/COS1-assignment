print("welcome to cos101 ")
print("BHU|24|04|05|0064")
print("EMMANUEL IGBERAESE")


def a():
    displacement = int(input("enter velocity:"))
    time = int(input("enter time:"))
    # velocity = displacement/time
    output = str(displacement/time)
    print(output +"m/s^1")

def b():
    a = int(input("a:"))
    b = int(input("b:"))
    # multiply = a*b
    output = str(a / b)
    print(output )

def c():
    force= int(input("enter force :"))
    length= int(input("enter length:"))
    # surface tension = force/length
    output = str(force/length)
    print(output + "N/m")

def d():
    mass= int(input("enter mass:"))
    volume= int(input("enter volume:"))
    # surface tension = mass/volume
    output = str(mass/volume)
    print(output + "pa")


def e():
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    # division = a/b
    output = str(a**b)
    print(output)

def main():
        user_choice = input("enter choice from(a-e):")
        if user_choice == "a":a()
        elif user_choice == "b":b()
        elif user_choice == "c":c()
        elif user_choice == "d":d()
        elif user_choice == "e":e()
if __name__ == '__main__':
    main()

