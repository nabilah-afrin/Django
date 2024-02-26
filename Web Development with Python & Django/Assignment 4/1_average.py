'''1. `calculate_average(grades)`: This function should take a list of grades `grades` as input and return the
average grade.

2. `get_letter_grade(average)`: This function should take the average grade `average` as input and
return the corresponding letter grade based on the following grading scale:
- A: 90 - 100
- B: 80 - 89
- C: 70 - 79
- D: 60 - 69
- F: Below 60'''

def avg_grade(grade_list):
    return sum(grade_list)/len(grade_list)
#average = avg_grade(grade_list=[90,67,79,23,99])
# print(average)

def get_letter_grade(average):
    if 90<=average<= 100: return"A"
    elif 80<=average<=89: return "B"
    elif 70<=average<=79: return "C"
    elif 60<=average<=69: return "D"
    else: return "F"
# letter_grade= get_letter_grade(average)
# print(letter_grade)

def display(average, letter_grade):
    print(f"Average grade is {average}\n" 
          f"letter_grade is {letter_grade}")
# display(average, letter_grade)


user_grade=[]
total_subject= int(input("total subjects: "))
for grades in range(total_subject):
    grade = int(input())
    user_grade.append(grade)
print(user_grade)
average = avg_grade(user_grade)
letter_grade= get_letter_grade(average)
display(average, letter_grade)