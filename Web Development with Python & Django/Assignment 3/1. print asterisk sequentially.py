# Write a Python program that uses nested loops to create a pattern of asterisks as follows:
# *
# * *
# * * *
# * * * *
# * * * * *
# Your program should allow the user to input the number of rows they want in the pattern.
rows = abs(int(input("total number of rows: ")))

for row in range(1,rows+1):
    print("*"*row)
