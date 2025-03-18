def add_student():
    # Getting input for Student ID and checking if it's valid
    sid = input("Student ID: ").strip()
    if not sid.isdigit():
        print("Please enter a valid number for Student ID.")
        return

    # Getting input for Student Name and checking if it's not empty
    sname = input("Student Name: ").strip()
    if not sname:
        print("Student Name cannot be empty.")
        return

    # New contact information inputs:
    email = input("Email: ").strip()
    if not email:
        print("Email cannot be empty.")
        return

    phone = input("Phone Number: ").strip()
    if not phone.isdigit():
        print("Please enter a valid phone number.")
        return

    address = input("Address: ").strip()
    if not address:
        print("Address cannot be empty.")
        return

    # Checking if student already exists
    try:
        with open("student.txt", "r") as students_file:
            for line in students_file:
                # Assuming the first field is the student ID
                if sid == line.strip().split(",")[0]:
                    print("Student ID already exists.")
                    return
    except FileNotFoundError:
        print("No existing student file found. A new one will be created.")

    # Write new student details into student.txt
    with open("student.txt", "a") as students_file:
        # Now storing five fields: Student ID, Student Name, Email, Phone, Address
        students_file.write(f"{sid},{sname},{email},{phone},{address}\n")
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
        return

    # Getting input from user for max seats and validating that it's a number
    max_seats = input("Max seats: ").strip()
    if not max_seats.isdigit():
        print("Please enter a valid number for seats.")
        return

    # Checking if course already exists
    try:
        with open("course.txt", "r") as course_file:
            for line in course_file:
                if cid == line.strip().split(",")[0]:
                    print("Course already exists!")
                    return
    except FileNotFoundError:
        print("New file for course has been created!")

    # Append the course information to course.txt
    with open("course.txt", "a") as course_file:
        course_file.write(f"{cid},{cname},{max_seats}\n")
        print()
        print(f"(Course ID: {cid}) (Course Name: {cname}) (Max Seats: {max_seats}) added successfully!\n")


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
            # Updated to expect five fields now: Student ID, Name, Email, Phone, Address
            sid, sname, email, phone, address = line.strip().split(",")
            print(f"Student ID: {sid} | Student Name: {sname} | Email: {email} | Phone: {phone} | Address: {address}")

    except FileNotFoundError:
        print("No existing student now.")


while True:
    print("=============================================")
    print("Sunway Course Registration System")
    print("Enter [1] To Add A New Student")
    print("Enter [2] To Add A New Course")
    print("Enter [3] To Enrol In A Course")
    print("Enter [4] To Drop A Course")
    print("Enter [5] To View Available Courses")
    print("Enter [6] To View Student Information")
    print("Enter [7] To Exit")
    try:
        selection = int(input("Enter Your Selection Here: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match selection:
        case 1:
            add_student()
        case 2:
            add_course()
        case 3:
            # enrol_course() needs to be defined or implemented
            print("Enrol in a course functionality is not yet implemented.")
        case 5:
            view_courses()
        case 6:
            view_students()
        case 7:
            print("Exiting The Program. SEE YOU AGAIN!")
            break
        case _:
            print("Invalid Selection, Please Choose Between 1 to 7")
