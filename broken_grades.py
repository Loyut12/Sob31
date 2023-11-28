# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))# adding the int class 

exam_three = int(input("Input exam grade three: "))# converting str to int and correcting the exam_3 to exam_three

grades = [exam_one,exam_two,exam_three] #adding commas
sum = 0
for grade in grades: # correcting the name of the variable
  sum = sum + grade

avg = sum / len(grade)# correcting the name of grade 

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: # adding colons 
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"  #correcting the double quotes
elif avg >= 69 and avg < 70: # changing the avg from 65 to 70 for the D grade and < instead of >=
    letter_grade = "D"
else: # ending the if block with a else statement instead of elif
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if grade == "F": #adding the correct syntax and variable names
    print ("Student is failing.")
else:
    print ("Student is passing.")
