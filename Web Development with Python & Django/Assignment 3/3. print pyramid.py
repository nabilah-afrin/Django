# Write a Python program to ta generate a pyramid pattern using numbers. The user should input the
# height of the pyramid, and the program should display the pattern as follows:
# For example, if the user enters 5:
#       1
#      121
#     12321
#    1234321
#   123454321

height = abs(int(input()))

for level in range(1, height + 1):
    
    number_left=""
    number_right =""

    for numbers in range(1,level):
        number_left+=str(numbers)
    for numbers in range(level-1,0,-1):
        number_right+=str(numbers)

    print(" "*(height - level) + number_left + str(level) + number_right + " "*(height - level), end='')
    print("\n")