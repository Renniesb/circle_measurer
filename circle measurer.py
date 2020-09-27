import math
#Rennie Bevineau

def main():
    radius = float(input("Radius?")) #used the float function to convert input into a floating point number
    print("\nDiameter is: %.2f"%(2*radius),
          "\nCircumference is: %.2f"%(2*math.pi*radius),
          "\nArea is: %.2f"%(math.pi*radius**2))

main()
