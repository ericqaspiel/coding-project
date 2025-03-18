def add_student():
    # Getting input from user for student ID if is not digit will print error
    sid = input("Student ID: ").strip()
    if not sid.isdigit():
        print("Please enter a valid number for Student ID.")
        return

    # Getting input from user for student name if empty will print error
    sname = input("Student Name: ").strip()
    if not sname:
        print("Student Name cannot be empty.")
        return

    # getting input from user for contact information and if user enter anything beside integer then will show error
    contact_info = input("Contact Information: ").strip()
    if not contact_info.isdigit():
        print("Please enter a valid number for Contact Information.")
        return

    # Checking if student already exist or not
    try:
        with open("student.txt", "r") as students_file:
            for line in students_file:
                if sid == line.strip().split(",")[0]:
                    print("Student ID already exists.")
                    return
    except FileNotFoundError:
        print("No existing student file found. A new one will be created.")

    # Write new student details into student.txt
    with open("student.txt", "a") as students_file:
        students_file.write(f"{sid},{sname},{contact_info}\n")
        print()
        print(f"(Student ID: {sid}) (Student Name: {sname}) added successfully!\n")


def add_course():
    # Getting input from user for course id & course name
    cid = input("Course ID: ").strip()
    if not cid:
        print("Please enter the valid Course ID")
        return

    cname = input("Course name: ").strip()
    if not cname:
        print("Please enter the valid course Name")

    # Getting input from user for max seats and if user enter anything beside integer then will show error
    max_seats = input("Max seats: ").strip()
    if not max_seats.isdigit():
        print("Please enter a valid number for seats.")
        return

    # This to check if courses existed and file not created.
    try:
        with open("course.txt", "r") as course_file:
            for line in course_file:
                if cid == line.strip().split(",")[0]:
                    print("Course already exist!")
                    return
    except FileNotFoundError:
        print("New file for course has created!")
    # this is check if file not created/found, tell the user new file has created

    # This to append the information from user to the file
    with open("course.txt", "a") as course_file:
        course_file.write(f"{cid},{cname},{max_seats}\n")
        print()
        print(f"(Course ID:{cid}) (Course Name:{cname}) (Max Seats:{max_seats}) added successfully!\n")


def view_courses():
    try:
        with open("course.txt", "r") as courses:
            course_list = courses.readlines()

        for line in course_list:
            cid, cname, max_seats = line.strip().split(",")
            print(f"Course ID: {cid} | Course Name: {cname} | Max Seats: {max_seats}")

    except FileNotFoundError:
        print("No available course now.")


def view_students():
    try:
        with open("student.txt", "r") as students:
            students_list = students.readlines()

        for line in students_list:
            sid, sname, contact_info = line.strip().split(",")
            print(f"Student ID: {sid} | Student Name: {sname} | Contact Information: {contact_info}")

    except FileNotFoundError:
        print("No existing student now.")


while True:
    print("=============================================")
    print("Sunway Course Registration System")
    print("Enter [1] To Add A New Student")
    print("Enter [2] To Add A New Course")
    print("Enter [3] To Enrol In A Course")
    print("Enter [4] To Drop A Course")
    print("Enter [5] to View Available Courses")
    print("Enter [6] To View Student Information")
    print("Enter [7] to Exit")
    selection = int(input("Enter Your Selection Here: "))

    match selection:
        case 1:
            add_student()
        case 2:
            add_course()
        case 3:
            enrol_course()
        case 5:
            view_courses()
        case 6:
            view_students()
        case 7:
            print("Exiting The Program. SEE YOU AGAIN!")
            break
        case _:
            print("Invalid Selection, Please Choose Between 1 to 7")
