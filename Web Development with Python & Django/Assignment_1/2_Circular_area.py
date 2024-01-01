# You are a landscape architect designing a circular fountain for a public park. To estimate the amountof tiles needed to pave the circular base of the fountain, you need to calculate the area of the circular base. The radius of the circular base is measured in meters. Write a Python program that takes user input for the radius of the circular base, calculates the area and display the output.

# inputs:
radius = float(input("The radius of the circular base in meters: "))
pi = 3.1416

# result
print("The area of the circular base is {:.2f} square meters".format(pi*radius**2))