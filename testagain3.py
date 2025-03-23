from datetime import datetime


def add_student():  # This is to add students' information to the student file
    while True:
        length = 8
        # Getting input from users for student ID. If not a digit or length is less than 8, print error.
        sid = input("Student ID(e.g. 25xxxxxx) (type 'cancel' to return): ").strip()
        if sid.lower() == "cancel":
            return
        if not sid.isdigit() or len(sid) < length:
            print("\nPlease enter a valid 8-digit number for Student ID(e.g. 25xxxxxx).\n")
            continue

        # Getting input from users for student name; if empty, print error.
        sname = input("Student Name (type 'cancel' to return): ").strip()
        if sname.lower() == "cancel":
            return
        if not sname:
            print("\nStudent Name cannot be empty.\n")
            continue

        # Getting input from users for phone number; if not digit, print error.
        phone_num = input("Phone number(e.g. 0123456789) (type 'cancel' to return): ").strip()
        if phone_num.lower() == "cancel":
            return
        if not phone_num.isdigit():
            print("\nPlease enter a valid number for phone number(e.g. 0123456789)\n")
            continue

        # Getting input from users for email address; if empty, print error.
        email_info = input("Email Address(e.g. example@email.com) (type 'cancel' to return): ").strip()
        if email_info.lower() == "cancel":
            return
        if not email_info:
            print("\nPlease enter a valid email address (e.g. example@email.com)\n")
            continue

        # Checking if student already exists.
        duplicate = False
        try:
            with open("student.txt", "r") as students_file:
                for line in students_file:
                    if sid == line.strip().split(",")[0]:
                        print("\nStudent ID already exists.\n")
                        duplicate = True
                        break
        except FileNotFoundError:
            print("\nNo existing student file found. A new one will be created.\n")
        if duplicate:
            continue

        # Write new student details into student.txt.
        with open("student.txt", "a") as students_file:
            students_file.write(f"{sid},{sname},{phone_num},{email_info}\n")
            print(f"\nStudent ID: {sid} | Student Name: {sname} added successfully!\n")
        break  # Exit after successful entry.


def add_course():  # This is to add courses' information to the course file
    while True:
        # Getting input from user for course ID.
        cid = input("Course ID(e.g. CSC1024) (type 'cancel' to return): ").strip().upper()
        if cid.lower() == "cancel":
            return
        if not cid:
            print("\nPlease enter the valid Course ID(e.g. CSC1024)\n")
            continue

        # Getting input from user for course name.
        cname = input("Course name(e.g. Computer Science) (type 'cancel' to return): ").strip()
        if cname.lower() == "cancel":
            return
        if not cname:
            print("\nPlease enter the valid course Name(e.g. Computer Science)\n")
            continue

        # Getting input from user for maximum seats; if not digit, print error.
        max_seats = input("Maximum seats for the course (type 'cancel' to return): ").strip()
        if max_seats.lower() == "cancel":
            return
        if not max_seats.isdigit():
            print("\nPlease enter a valid number for maximum seats.\n")
            continue

        # Check if course exists.
        duplicate = False
        try:
            with open("course.txt", "r") as course_file:
                for line in course_file:
                    if cid == line.strip().split(",")[0]:
                        print("\nCourse already exists!\n")
                        duplicate = True
                        break
        except FileNotFoundError:
            print("\nNo existing course file found, a new one will be created.\n")
        if duplicate:
            continue

        # Append the course information to the file.
        with open("course.txt", "a") as course_file:
            course_file.write(f"{cid},{cname},{max_seats}\n")
            print(f"\n(Course ID: {cid}) (Course Name: {cname}) (Max Seats: {max_seats}) added successfully!\n")
        break


def enrol_course():  # This is to enrol students in a course.
    while True:
        # Get student ID for enrolment.
        sid = input("Enter student ID to enrol(e.g. 25xxxxxx) (type 'cancel' to return): ").strip()
        if sid.lower() == "cancel":
            return
        if not sid.isdigit():
            print("\nPlease enter a valid number for student ID(e.g. 25xxxxxx)\n")
            continue

        # Get course ID for enrolment.
        cid = input("Enter course ID to enrol(e.g. CSC1024) (type 'cancel' to return): ").strip().upper()
        if cid.lower() == "cancel":
            return
        if not cid:
            print("\nPlease enter a valid course ID(e.g. CSC1024)\n")
            continue

        student_found = False
        course_found = False
        course_id_seats_left = 0
        updated_courses = []
        already_enrolled = False

        # Check if student exists.
        try:
            with open("student.txt", "r") as student_file:
                for line in student_file:
                    if sid == line.strip().split(",")[0]:
                        student_found = True
                        break
        except FileNotFoundError:
            pass
        if not student_found:
            print("\nStudent is not registered\n")
            continue

        # Read courses and check if the specified course exists.
        try:
            with open("course.txt", "r") as course_file:
                for line in course_file:
                    course_id, cname_line, max_seats = line.strip().split(",")
                    if cid == course_id:
                        course_found = True
                        course_id_seats_left = int(max_seats)
                    updated_courses.append([course_id, cname_line, int(max_seats)])
        except FileNotFoundError:
            pass
        if not course_found:
            print("\nCourse is not available\n")
            continue

        # Count how many students are already enrolled in the course
        # and check if this student is already enrolled.
        enrolled_count = 0
        try:
            with open("enrollments.txt", "r") as enrollment_file:
                for line in enrollment_file:
                    try:
                        enrolment_sid, enrolment_cid, _ = line.strip().split(",")
                    except ValueError:
                        continue
                    if enrolment_cid == cid:
                        enrolled_count += 1
                    if enrolment_sid == sid and enrolment_cid == cid:
                        already_enrolled = True
        except FileNotFoundError:
            pass
        if already_enrolled:
            print(f"\nStudent ID: {sid} is already enrolled in Course ID: {cid}.\n")
            continue

        available_seats = course_id_seats_left - enrolled_count
        if available_seats <= 0:
            print(f"\nUnable to enrol student in Course ID: {cid} as there are no seats left.\n")
            continue

        # Add enrolment record.
        with open("enrollments.txt", "a") as enrollment_file:
            enrolment_date = datetime.today().strftime("%d-%m-%Y")
            enrollment_file.write(f"{sid},{cid},{enrolment_date}\n")

        # Update the course file to reflect new seat count.
        with open("course.txt", "w") as course_file:
            for course in updated_courses:
                if course[0] == cid:
                    course[2] -= 1
                course_file.write(f"{course[0]},{course[1]},{course[2]}\n")

        print(f"\nStudent ID: {sid} has successfully enrolled in Course ID: {cid} on {enrolment_date}.\n")
        break


def drop_course():  # This is to drop a student's course.
    while True:
        # Get student ID to drop.
        sid = input("Enter student ID to drop a course (type 'cancel' to return): ").strip()
        if sid.lower() == "cancel":
            return
        if not sid.isdigit():
            print("\nPlease enter a valid student ID\n")
            continue
        # Get course ID to drop.
        cid = input("Enter course ID to drop (type 'cancel' to return): ").strip().upper()
        if cid.lower() == "cancel":
            return
        if not cid:
            print("\nPlease enter a valid course ID\n")
            continue

        student_found = False
        course_found = False
        enrollment_found = False
        saved_enrollments = []
        updated_courses = []

        # Check if student exists.
        try:
            with open("student.txt", "r") as student_file:
                for line in student_file:
                    if sid == line.strip().split(",")[0]:
                        student_found = True
                        break
        except FileNotFoundError:
            pass
        if not student_found:
            print(f"\nStudent ID: {sid} not found. Please register first.\n")
            continue

        # Check if course exists.
        try:
            with open("course.txt", "r") as course_file:
                for line in course_file:
                    course_id, cname_line, max_seats = line.strip().split(",")
                    if cid == course_id:
                        course_found = True
                    updated_courses.append([course_id, cname_line, int(max_seats)])
        except FileNotFoundError:
            pass
        if not course_found:
            print(f"\nCourse ID: {cid} not found. Please enter a valid course.\n")
            continue

        # Check if enrollment exists and remove it.
        try:
            with open("enrollments.txt", "r") as enrollment_file:
                for line in enrollment_file:
                    try:
                        enrolment_sid, enrolment_cid, _ = line.strip().split(",")
                    except ValueError:
                        continue
                    if sid == enrolment_sid and cid == enrolment_cid:
                        enrollment_found = True
                    else:
                        saved_enrollments.append(line)
        except FileNotFoundError:
            pass
        if not enrollment_found:
            print(f"\nStudent ID: {sid} is not enrolled in Course ID: {cid}. No course to drop.\n")
            continue

        # Write updated enrollments.
        with open("enrollments.txt", "w") as enrollment_file:
            enrollment_file.writelines(saved_enrollments)

        # Increase seat count for the dropped course.
        with open("course.txt", "w") as course_file:
            for course in updated_courses:
                if course[0] == cid:
                    course[2] += 1
                course_file.write(f"{course[0]},{course[1]},{course[2]}\n")

        print(f"\nStudent ID: {sid} has successfully dropped Course ID: {cid}. Seat has been returned.\n")
        break


def view_courses():  # This is to view available courses.
    try:
        with open("course.txt", "r") as courses:
            course_list = courses.readlines()
        for line in course_list:
            cid, cname, max_seats = line.strip().split(",")
            seats_taken = 0
            try:
                with open("enrollments.txt", "r") as enrollments:
                    for enroll_line in enrollments:
                        enrolment_cid = enroll_line.strip().split(",")[0]  # Extract enrolled course ID.
                        if enrolment_cid == cid:
                            seats_taken += 1
            except FileNotFoundError:
                pass
            remaining_seats = int(max_seats) - seats_taken
            print(f"Course ID: {cid} | Course Name: {cname} | Remaining Seats: {remaining_seats}")
    except FileNotFoundError:
        print("\nNo available course now.\n")


def view_students():  # This is to view student details.
    try:
        with open("student.txt", "r") as students:
            students_list = students.readlines()
        for line in students_list:
            sid, sname, phone_num, email_info = line.strip().split(",")
            print(
                f"Student ID: {sid} | Student Name: {sname} | Phone Number: {phone_num} | Email Address: {email_info}"
            )
    except FileNotFoundError:
        print("No existing student now.")


def main_program():  # This shows the main menu and handles user selection.
    while True:
        print("=============================================")
        print("Sunway Course Registration System")
        print("Enter [1] To add a new student")
        print("Enter [2] To add a new course")
        print("Enter [3] To enrol in a course")
        print("Enter [4] To drop a course")
        print("Enter [5] To view available courses")
        print("Enter [6] To view student informations")
        print("Enter [7] To exit")

        try:
            selection = int(input("Enter your selection here: "))
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 to 7.")
            input("Press Enter to continue...")
            continue

        match selection:
            case 1:
                add_student()
            case 2:
                add_course()
            case 3:
                enrol_course()
            case 4:
                drop_course()
            case 5:
                view_courses()
            case 6:
                view_students()
            case 7:
                print("Exiting the program. SEE YOU AGAIN!")
                break
            case _:
                print("Invalid selection, please choose between 1 to 7")


main_program()
