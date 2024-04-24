def MainMenu():
    choice=0
    while choice != 6:
        choice = int(input("Please select one of the following:\n\
1- Add a new student \n\
2- Add a new course \n\
3- Add a new grade \n\
4- Print a students transcript \n\
5- Students who pass a subject \n\
6- Exit \n\
Your choice: "))
        if choice == 1:
            AddNewStudent()
        elif choice == 2:
            AddNewCourse()
        elif choice == 3:
            AddNewGrade()
        elif choice == 4:
            PrintStudentTranscript()
        elif choice == 5:
            StudentsWhoPassSubject()
        elif choice == 6:
            ListtoFileCourses()
            ListtoFileGrades()
            ListtoFileStudents()
            print("Data Saved.")

#Option 1
def AddNewStudent():
    student_id = input("Please enter student ID: ")
    if find_student(student_id) != "":
        print("There is a student with that ID")
    else:
        student_name = input("Enter student name: ")
        mobile = input("Enter student mobile: ")
        Students.append(f"{student_id},{student_name},{mobile},0.0")

#Option 2
def AddNewCourse():
    course_id = input("Please enter course no.: ")
    course_id = course_id.upper()
    if find_course(course_id) != "":
        print("There is already a course with that number")
    else:
        course_name = input("Enter course name: ")
        course_credits = input("Enter course credits: ")
        Courses.append(f"{course_id},{course_name},{course_credits}")

#Option 3
def AddNewGrade():
    student_id = input("Please enter student ID: ")
    student_line = find_student(student_id)
    if student_line != "":
        student = student_line.split(',')
        print(f'Student Name: {student[1]}')
        course_id = input('Enter course No.: ')
        course = find_course(course_id)
        if course != "":
            course=course.split(',')
            print('Course name: ',course[1])
            grade = ""
            grade_letters = ['A','B','C','D','F']
            while grade not in grade_letters:
                grade = input("Enter student Grade: ")
                if grade not in grade_letters:
                    print('Invalid input!')
                else:
                    Grades.append(f"{student_id},{course_id},{grade}")
            points_dictionary = {'A':4 , 'B':3 , 'C':2 , 'D':1 , 'F':0}
            student_grade = find_student_grades(student_id)
            
            pointsCC_sum = 0
            credits_sum = 0
            for grade_info in student_grade:
                info = grade_info.split(',')
                points = points_dictionary[info[2]]
                course_credits = find_course_credits(info[1])
                pointsCC_sum += (points*course_credits)
                credits_sum += course_credits

            GPA = (pointsCC_sum)/credits_sum
            student[3] = str(format(GPA, ".2f"))
            student_index = Students.index(student_line)
            Students[student_index] = f"{student[0]},{student[1]},{student[2]},{student[3]}"
        else:
            print('There is no course with this number.')
    else:
        print("There is no student with this ID")

#Option 4:
def PrintStudentTranscript():
    student_id = input("Please enter student ID: ")
    student_info = find_student(student_id)
    
    if student_info != "":
        info = student_info.split(',')
        print(f'Student Name: {info[1]}')
        print(f'GPA: {info[3]}')
        print()
        student_grades = find_student_grades(student_id)
        for grade_info in student_grades:
            info = grade_info.split(',')
            course_id = info[1]
            course_info = find_course(course_id)
            if course_info != "":
                course_info = course_info.split(',')
                print(course_info[0], course_info[1], info[2])
    else:
        print("No student with this ID")

#Option 5:
def StudentsWhoPassSubject():
    course_id = input("Please enter course number: ")
    course_info = find_course(course_id)
    
    if course_info != "":
        course_info = course_info.split(',')
        print(f'Students who pass {course_info[1]} ({course_info[0]}):')

        for student_line in Students:
            student = student_line.split(',')
            student_grades = find_student_grades(student[0])
            
            for grade_info in student_grades:
                info = grade_info.split(',')
                if info[1] == course_id and info[2] != 'F':
                    print(f'{student[1]}')
                    break
    else:
        print("There is no course with this number")


def find_course_credits(course_id):
    for course in Courses:
        if course.startswith(f"{course_id},"):
            return int(course.split(',')[2])
    return 0

def find_student_grades(student_id):
    student_grade=[]
    for grade in Grades:
        if grade.startswith(f"{student_id},"):
            student_grade.append(grade)
    return student_grade

def find_student(student_id):
    for student in Students:
        if student.startswith(f"{student_id},"):
            return student
    return ""

def find_course(course_id):
    for course in Courses:
        if course.startswith(f"{course_id},"):
            return course
    return ""

def FiletoListStudents():
    Students = []
    try:
        Students_file = open("students.txt", "r")
        student = Students_file.readlines()
        for i in range(len(student)):
            student[i] = student[i].strip()
        Students += student
        Students_file.close()
    except FileNotFoundError:
        print("File 'transactions.txt' not found.")
    return Students

def FiletoListGrades():
    Grades = []
    try:
        Grades_file = open("grade.txt", "r")
        grade = Grades_file.readlines()
        for i in range(len(grade)):
            grade[i] = grade[i].strip()
        Grades += grade
        Grades_file.close()
    except FileNotFoundError:
        print("File 'transactions.txt' not found.")
    return Grades

def FiletoListCorses():
    Courses = []
    try:
        Courses_file = open("course.txt", "r")
        course = Courses_file.readlines()
        for i in range(len(course)):
            course[i] = course[i].strip()
        Courses += course
        Courses_file.close()
    except FileNotFoundError:
        print("File 'transactions.txt' not found.")
    return Courses

def ListtoFileStudents():
    students_file = open("students.txt", "w")
    for student in Students:
        students_file.write(student + "\n")
    students_file.close()
    
def ListtoFileGrades():
    grades_file = open("grade.txt", "w")
    for grade in Grades:
        grades_file.write(grade + "\n")
    grades_file.close()

def ListtoFileCourses():
    courses_file = open("course.txt", "w")
    for course in Courses:
        courses_file.write(course + "\n")
    courses_file.close()
    
Students = FiletoListStudents()
Grades = FiletoListGrades()
Courses = FiletoListCorses()
MainMenu()