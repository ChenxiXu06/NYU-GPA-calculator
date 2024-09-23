valid_course_count = {str(i) for i in range(1, 11)}
valid_credits = {'1', '2', '3', '4', '5', '6'}
gpa_scale = {
    'A': '4.0', 'A-': '3.667', 'B+': '3.333', 'B': '3.0', 'B-': '2.667',
    'C+': '2.333', 'C': '2.0', 'C-': '1.667', 'D+': '1.333', 'D': '1.0', 'F': '0.0'}
credits = []
grades = []
gpa_values = []

course_count = input("How many courses did you have this semester? (Please enter an integer from 1 to 10): ")
while course_count not in valid_course_count:
    print("Invalid course count! You should input an integer ranging from 1 to 10.")
    course_count = input("How many courses did you have this semester? (Please enter an integer from 1 to 10): ")
course_count = int(course_count)

for i in range(1, course_count + 1):
    credit = input("How much is the credit for course #%i? (Please enter an integer from 1 to 6): " % i)
    while credit not in valid_credits:
        print("Invalid credit! You should input an integer ranging from 1 to 6.")
        credit = input("How much is the credit for course #%i? (Please enter an integer from 1 to 6): " % i)
    credit = int(credit)
    credits.append(credit)

for o in range(1, course_count + 1):
    grade = input("Enter your grade for course #%i (e.g., A, B+, etc.): " % o)
    while grade not in gpa_scale:
        print("Invalid grade! Please enter a valid grade from the following options: " + ", ".join(gpa_scale.keys()))
        grade = input("Enter your grade for course #%i (e.g., A, B+, etc.): " % o)
    grades.append(grade)

total_credits = sum(credits)
for grade in grades:
    gpa_values.append(float(gpa_scale[grade]))

weighted_gpa_sum = 0
for i in range(course_count):
    weighted_gpa_sum += (credits[i] / total_credits) * gpa_values[i]

final_gpa = format(weighted_gpa_sum, ".2f")
print("Your final GPA is: " + final_gpa)




