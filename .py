#   Question  1.i.a. Student Marks

# student_marks
# studentMarks


#   Question  2.i.b. total_Average Mark

# total_average_marks
# totalAverageMarks


#   Question 1.ii

variable_age =float(22)
print(variable_age)
print(type(variable_age))


#    Question 2.i

import statistics

x= 20
y= 30

print(statistics.mean([x, y]))


#   Question 2.ii 

# find minimum number
# my_data = [1,2,3]

minimum_number = min(1,2,3)
print(minimum_number)


#   Question 3.i.
# student_marks = [78, 83, 90, 88, 75]

a = 78
b = 83
c = 90
d = 88
e = 75

student_marks = a + b + c + d + e

print(student_marks)

print("The sum of the items in the student marks list is " + "" + str(student_marks))


#   Question 3.ii

# First mark 
# student_marks = [78, 83, 90, 88, 75]

first_mark = max(78, 83, 90, 88, 75)
print(first_mark)


# Last mark student 
# student_marks = [78, 83, 90, 88, 75]
last_mark = min(78, 83, 90, 88, 75)
print(last_mark)



#   Question 3.iii

student_marks1 = [78, 83, 90, 88, 75]
student_marks1.append(96)

print(student_marks1)


#   Question 3.iv

student_marks1[0] = 87
print(student_marks1)
