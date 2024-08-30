# In order to manage student grades, we must declare where the data of the students shall be properly placed
# Declare a list variable named "students" to store student information
students = []
# First, we will asks each student about their information
def get_student_information():
    # Will collect their name
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    # Will collect their grades for subjects GED0103, DSC1101, and DSC1103
    grades={}
    for subject in ["GED0103", "DSC1101", "DSC1103"]:
        subject_grade = float(input(f"""
        Enter subject grade for {subject}: """))
        grades[subject] = subject_grade
    add_student(first_name, last_name, grades)
    # the function add_student() will executed repeatedly as each iteration in main() remains TRUE;
# Function to add a student and their grades
def add_student(first_name, last_name, grades):
    student = {
        'fname': first_name,
        'lname': last_name,
        'grades': grades,
        'average': calculate_average(grades)
        # Will proceed to the function calculate_average()
    }
    students.append(student) 
    # Remember the empty array list students = []  that we were mentioned at the uppermost part of this phyton, we will insert student = {} entry on the students
# A Function to calculate the average of the grades
def calculate_average(grades):
    return sum(grades.values()) / len(grades)
# Final function to display the students' information
def display_student_information():
    for student in students:
        print(f"""Student Name: 
                {student['fname']}
                {student['lname'] }
            """)
        print("Grades:")
        for subject, grade in student['grades'].items():
            print(f"  {subject}: {grade}")
        print(f"Average Grade: {student['average']:.2f}")
        print("-" * 30)
# Execution of the python application
def main():
    while True:
        get_student_information()
        another = input(f"""
        Would you like to add another student's information before displaying?
        [Yes/No]
        
        Answer: """).strip().lower()
        
        if another != "yes" and another != "y":
            break
    display_student_information() 
# Let us call the function main() where the experiments to gather and display informations will be happened
main()
