import math
math.pi

def main_function():
    r = float(input("Enter the radius of a circle: "))
    calcArea(r)
    print("The area of a circle with radius {} is: {:.2f} ".format(r,calcArea(r)))

def calcArea(r):
    area = math.pi * (r ** 2)
    return area

main_function()

print(input("press enter to exit."))