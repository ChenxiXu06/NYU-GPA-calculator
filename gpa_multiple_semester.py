valid_credits = {str(i) for i in range(12, 21)}
valid_credits_all = {str(i) for i in range(0, 117)}

# Input overall credits before this semester
credit_all = input("Enter your overall credits before this semester (0 to 116): ")
while credit_all not in valid_credits_all:
    print("Invalid credits! Please enter an integer between 0 and 116.")
    credit_all = input("Enter your overall credits before this semester (0 to 116): ")
credit_all = int(credit_all)

# Input credits for this semester
credit_ = input("Enter your credits for this semester (12 to 21): ")
while credit_ not in valid_credits:
    print("Invalid credits! Please enter an integer between 12 and 21.")
    credit_ = input("Enter your credits for this semester (12 to 21): ")
credit_ = int(credit_)

# Input overall GPA before this semester
while True:
    overall_gpa = input("Please enter your overall GPA before this semester (0.0 to 4.0): ")
    try:
        overall_gpa = float(overall_gpa)
        if 0 <= overall_gpa <= 4:
            break
        else:
            print("Please enter a float between 0.0 and 4.0.")
    except ValueError:
        print("Please enter a valid number.")

# Input GPA for this semester
while True:
    gpa = input("Please enter your GPA for this semester (0.0 to 4.0): ")
    try:
        gpa = float(gpa)
        if 0 <= gpa <= 4:
            break
        else:
            print("Please enter a float between 0.0 and 4.0.")
    except ValueError:
        print("Please enter a valid number.")

# Calculate overall GPA
sum_gpa = credit_all + credit_
final_gpa = (credit_all / sum_gpa * overall_gpa) + (credit_ / sum_gpa * gpa)
final_gpa = format(final_gpa, ".2f")

# Display the final GPA
print("Your overall GPA is: " + final_gpa)












