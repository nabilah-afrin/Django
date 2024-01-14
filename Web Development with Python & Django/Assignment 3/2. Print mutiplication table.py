# Write a Python program to take input and generate a multiplication table for numbers from 1 to input-
# value. The table should be displayed in the following format:

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

number = abs(int(input()))

for val in range(1, number+1):

    for base in range(1,number+1):
        print(val*base, end= " ")
        
    print("\n")
