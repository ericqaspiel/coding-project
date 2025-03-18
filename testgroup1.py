def add_student():
    sid = input("Student ID: ").strip()
    if not sid.isdigit():
        print("Please enter a valid number for Student ID.")
        return

    sname = input("Student Name: ").strip()
    if sname == "":
        print("Student Name cannot be empty.")
        return

    email = input("Email: ").strip()
    if email == "":
        print("Email cannot be empty.")
        return

    phone = input("Phone Number: ").strip()
    if not phone.isdigit():
        print("Please enter a valid phone number.")
        return

    address = input("Address: ").strip()
    if address == "":
        print("Address cannot be empty.")
        return

    # Check if student already exists
    try:
        file_found = True
        with open("student.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        file_found = False
        lines = []

    if file_found:
        i = 0
        while i < len(lines):
            parts = lines[i].strip().split(",")
            if len(parts) == 5:
                existing_sid = parts[0]
                if existing_sid == sid:
                    print("Student ID already exists.")
                    return
            i += 1

    # Append new student data
    with open("student.txt", "a") as f:
        f.write(sid + "," + sname + "," + email + "," + phone + "," + address + "\n")

    print("\n(Student ID: " + sid + ") (Student Name: " + sname + ") added successfully!\n")


def add_course():
    cid = input("Course ID: ").strip()
    if cid == "":
        print("Please enter a valid Course ID")
        return

    cname = input("Course Name: ").strip()
    if cname == "":
        print("Please enter a valid Course Name")
        return

    max_seats = input("Max Seats: ").strip()
    if not max_seats.isdigit():
        print("Please enter a valid number for seats.")
        return

    # Check if course already exists
    try:
        file_found = True
        with open("course.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        file_found = False
        lines = []

    if file_found:
        i = 0
        while i < len(lines):
            parts = lines[i].strip().split(",")
            if len(parts) == 3:
                existing_cid = parts[0]
                if existing_cid == cid:
                    print("Course ID already exists!")
                    return
            i += 1

    # Append the course
    with open("course.txt", "a") as f:
        f.write(cid + "," + cname + "," + max_seats + "\n")

    print(
        "\n(Course ID: " + cid + ") (Course Name: " + cname + ") (Max Seats: " + max_seats + ") added successfully!\n"
    )


def view_courses():
    try:
        with open("course.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No available course now.")
        return

    if len(lines) == 0:
        print("No available course now.")
        return

    i = 0
    while i < len(lines):
        parts = lines[i].strip().split(",")
        if len(parts) == 3:
            cid = parts[0]
            cname = parts[1]
            max_seats = parts[2]
            print("Course ID: " + cid + " | Course Name: " + cname + " | Max Seats: " + max_seats)
        i += 1


def view_students():
    try:
        with open("student.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No existing student file found.")
        return

    students_list = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        parts = line.split(",")
        if len(parts) == 5:
            students_list.append(parts)  # [sid, name, email, phone, address]
        i += 1

    if len(students_list) == 0:
        print("No student information available.")
        return

    print("\nList of Students:")
    i = 0
    while i < len(students_list):
        print(f"[{i+1}] {students_list[i][1]}")
        i += 1

    try:
        selection = int(input("\nSelect a student by number for more details: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if selection < 1 or selection > len(students_list):
        print("Invalid selection.")
        return

    selected_student = students_list[selection - 1]
    print("\nStudent Details:")
    print("Student ID: " + selected_student[0])
    print("Student Name: " + selected_student[1])
    print("Email: " + selected_student[2])
    print("Phone Number: " + selected_student[3])
    print("Address: " + selected_student[4] + "\n")


def read_students():
    students = []
    try:
        with open("student.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return students

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        parts = line.split(",")
        if len(parts) == 5:
            students.append(parts)
        i += 1

    return students


def read_courses():
    courses = []
    try:
        with open("course.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return courses

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        parts = line.split(",")
        if len(parts) == 3:
            courses.append(parts)
        i += 1

    return courses


def write_courses(courses):
    with open("course.txt", "w") as f:
        i = 0
        while i < len(courses):
            c = courses[i]
            f.write(c[0] + "," + c[1] + "," + c[2] + "\n")
            i += 1


def read_enrollments():
    enrollments = []
    try:
        with open("enrollment.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return enrollments

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        parts = line.split(",")
        if len(parts) == 2:
            enrollments.append(parts)
        i += 1

    return enrollments


def write_enrollments(enrollment_data):
    with open("enrollment.txt", "w") as f:
        i = 0
        while i < len(enrollment_data):
            e = enrollment_data[i]
            f.write(e[0] + "," + e[1] + "\n")
            i += 1


def enrol_course():
    students = read_students()
    if len(students) == 0:
        print("No students found. Please add a student first.")
        return

    print("\nSelect a student to enroll:")
    i = 0
    while i < len(students):
        print("[" + str(i + 1) + "] " + students[i][1] + " (ID: " + students[i][0] + ")")
        i += 1

    try:
        student_choice = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if student_choice < 1 or student_choice > len(students):
        print("Invalid selection.")
        return

    selected_student = students[student_choice - 1]
    sid = selected_student[0]

    courses = read_courses()
    if len(courses) == 0:
        print("No courses found. Please add a course first.")
        return

    print("\nSelect a course to enroll in:")
    i = 0
    while i < len(courses):
        print("[" + str(i + 1) + "] " + courses[i][1] + " (ID: " + courses[i][0] + ") | Seats: " + courses[i][2])
        i += 1

    try:
        course_choice = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if course_choice < 1 or course_choice > len(courses):
        print("Invalid selection.")
        return

    selected_course = courses[course_choice - 1]
    cid = selected_course[0]
    try:
        max_seats = int(selected_course[2])
    except ValueError:
        max_seats = 0

    if max_seats <= 0:
        print("Course " + selected_course[1] + " is full. Please try another course.")
        return

    enrollments = read_enrollments()
    i = 0
    while i < len(enrollments):
        if enrollments[i][0] == sid and enrollments[i][1] == cid:
            print("This student is already enrolled in the selected course.")
            return
        i += 1

    enrollments.append([sid, cid])
    write_enrollments(enrollments)

    i = 0
    while i < len(courses):
        if courses[i][0] == cid:
            seats_num = int(courses[i][2])
            seats_num -= 1
            courses[i][2] = str(seats_num)
            break
        i += 1

    write_courses(courses)
    print(
        "Student "
        + selected_student[1]
        + " (ID: "
        + sid
        + ") has been enrolled in "
        + selected_course[1]
        + " (ID: "
        + cid
        + ")."
    )


def drop_course():
    enrollments = read_enrollments()
    if len(enrollments) == 0:
        print("No enrollments found.")
        return

    students = read_students()
    if len(students) == 0:
        print("No students found.")
        return

    enrolled_student_ids = []
    i = 0
    while i < len(enrollments):
        sid = enrollments[i][0]
        if sid not in enrolled_student_ids:
            enrolled_student_ids.append(sid)
        i += 1

    enrolled_students = []
    i = 0
    while i < len(students):
        if students[i][0] in enrolled_student_ids:
            enrolled_students.append(students[i])
        i += 1

    if len(enrolled_students) == 0:
        print("No students are currently enrolled in any course.")
        return

    print("\nSelect a student to drop from a course:")
    i = 0
    while i < len(enrolled_students):
        print("[" + str(i + 1) + "] " + enrolled_students[i][1] + " (ID: " + enrolled_students[i][0] + ")")
        i += 1

    try:
        student_choice = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if student_choice < 1 or student_choice > len(enrolled_students):
        print("Invalid selection.")
        return

    selected_student = enrolled_students[student_choice - 1]
    sid = selected_student[0]

    student_enrolled_course_ids = []
    i = 0
    while i < len(enrollments):
        if enrollments[i][0] == sid:
            student_enrolled_course_ids.append(enrollments[i][1])
        i += 1

    courses = read_courses()
    student_courses = []
    i = 0
    while i < len(courses):
        if courses[i][0] in student_enrolled_course_ids:
            student_courses.append(courses[i])
        i += 1

    if len(student_courses) == 0:
        print("This student is not enrolled in any course.")
        return

    print("\nSelect a course to drop for " + selected_student[1] + ":")
    i = 0
    while i < len(student_courses):
        print(
            "["
            + str(i + 1)
            + "] "
            + student_courses[i][1]
            + " (ID: "
            + student_courses[i][0]
            + ") | Seats: "
            + student_courses[i][2]
        )
        i += 1

    try:
        drop_choice = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if drop_choice < 1 or drop_choice > len(student_courses):
        print("Invalid selection.")
        return

    drop_course_info = student_courses[drop_choice - 1]
    cid_to_drop = drop_course_info[0]

    new_enrollments = []
    i = 0
    while i < len(enrollments):
        if not (enrollments[i][0] == sid and enrollments[i][1] == cid_to_drop):
            new_enrollments.append(enrollments[i])
        i += 1

    write_enrollments(new_enrollments)

    i = 0
    while i < len(courses):
        if courses[i][0] == cid_to_drop:
            seats_num = int(courses[i][2])
            seats_num += 1
            courses[i][2] = str(seats_num)
            break
        i += 1

    write_courses(courses)
    print(
        "Student "
        + selected_student[1]
        + " (ID: "
        + sid
        + ") has been dropped from "
        + drop_course_info[1]
        + " (ID: "
        + cid_to_drop
        + ")."
    )


# Main Program using match/case for menu selection
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

    selection = input("Enter Your Selection Here: ").strip()

    match selection:
        case "1":
            add_student()
        case "2":
            add_course()
        case "3":
            enrol_course()
        case "4":
            drop_course()
        case "5":
            view_courses()
        case "6":
            view_students()
        case "7":
            print("Exiting The Program. SEE YOU AGAIN!")
            break
        case _:
            print("Invalid Selection, Please Choose Between 1 to 7")
