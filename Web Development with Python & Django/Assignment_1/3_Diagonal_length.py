# You are a civil engineer tasked with designing a pedestrian bridge that spans across a river. To ensure the safety and stability of the bridge, you need to calculate the length of the diagonalsupport cables using the Ppythagorean Theorem. The bridge forms a right angled triangle with one side representing the horizontal distance across the rive, the other side representing the vertical height difference between the two banks, and the diagonal as the cable support. Write a Python program that takes user input for the horizontal and vertical distances, then displays the length of the diagonal support cable. 

# user input
horizontal_length = float(input())
vertical_length = float(input())

# result
diagonal_length = (horizontal_length**2 + vertical_length**2)**0.5
print(f"The diagonal length is {diagonal_length:.2f} meters")
