from datetime import datetime


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

    # getting input from user for phone number and if user enter anything beside integer then will show error
    phone_num = input("Phone number: ").strip()
    if not phone_num.isdigit():
        print("Please enter a valid number for phone number")
        return

    email_info = input("Email Address: ").strip()
    if not email_info:
        print("Please enter a valid email address")
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
        students_file.write(f"{sid},{sname},{phone_num},{email_info}\n")
        print()
        print(f"Student ID: {sid} | Student Name: {sname} added successfully!\n")


def add_course():
    # Getting input from user for course id & course name
    cid = input("Course ID: ").strip().upper()
    if not cid:
        print("Please enter the valid Course ID")
        return

    cname = input("Course name: ").strip()
    if not cname:
        print("Please enter the valid course Name")
        return

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
        print(f"(Course ID: {cid}) (Course Name: {cname}) (Max Seats: {max_seats}) added successfully!\n")


def enrol_course():
    sid = input("Enter student ID to enrol: ").strip()
    if not sid.isdigit():
        print("Please enter a valid number for student ID")
        return

    cid = input("Enter student course ID to enrol: ").strip().upper()
    if not cid:
        print("Please enter a valid course ID")
        return

    student_found = False
    course_found = False
    course_id_seats_left = 0
    updated_courses = []
    already_enrolled = False  # New variable to track duplicate enrollment

    # Check if student exists
    try:
        with open("student.txt", "r") as student_file:
            for line in student_file:
                if sid == line.strip().split(",")[0]:
                    student_found = True
                    break
    except FileNotFoundError:
        pass

    if not student_found:
        print("Student is not registered")
        return

    # Read courses and check if course exists
    try:
        with open("course.txt", "r") as course_file:
            for line in course_file:
                course_id, cname, max_seats = line.strip().split(",")
                if cid == course_id:
                    course_found = True
                    course_id_seats_left = int(max_seats)
                updated_courses.append([course_id, cname, int(max_seats)])  # Store all course data
    except FileNotFoundError:
        pass

    if not course_found:
        print("Course is not available")
        return

    # Count students already enrolled in the course & check for duplicate enrollment
    enrolled_count = 0
    try:
        with open("enrollments.txt", "r") as enrollment_file:
            for line in enrollment_file:
                try:
                    enrolment_sid, enrolment_cid, _ = line.strip().split(",")
                    if enrolment_cid == cid:
                        enrolled_count += 1
                    if enrolment_sid == sid and enrolment_cid == cid:
                        already_enrolled = True  # Student is already in this course
                except ValueError:
                    continue  # Skip malformed lines
    except FileNotFoundError:
        pass

    # **Check if student is already enrolled in the course**
    if already_enrolled:
        print(f"Student ID: {sid} is already enrolled in Course ID: {cid}.")
        return

    # **Check if seats are available**
    available_seats = course_id_seats_left - enrolled_count
    if available_seats <= 0:
        print(f"Unable to enrol student in Course ID: {cid} as there are no seats left.")
        return

    # **Add student into enrollments**
    with open("enrollments.txt", "a") as enrollment_file:
        enrolment_date = datetime.today().strftime("%d-%m-%Y")
        enrollment_file.write(f"{sid},{cid},{enrolment_date}\n")

    # **Update course.txt to reflect new seat count**
    with open("course.txt", "w") as course_file:
        for course in updated_courses:
            if course[0] == cid:  # Update the seats for enrolled course
                course[2] -= 1
            course_file.write(f"{course[0]},{course[1]},{course[2]}\n")

    print(f"Student ID: {sid} has successfully enrolled in Course ID: {cid} on {enrolment_date}.")


def drop_course():

    sid = input("Enter student ID to drop a course: ").strip()
    if not sid.isdigit():
        print("Please enter a valid student ID")
        return

    cid = input("Enter course ID to drop: ").strip().upper()
    if not cid:
        print("Please enter a valid course ID")
        return

    student_found = False
    course_found = False
    enrollment_found = False
    saved_enrollments = []
    updated_courses = []

    # **Check if student exists**
    try:
        with open("student.txt", "r") as student_file:
            for line in student_file:
                if sid == line.strip().split(",")[0]:
                    student_found = True
                    break
    except FileNotFoundError:
        pass

    if not student_found:
        print(f"Student ID: {sid} not found. Please register first.")
        return

    # **Check if course exists**
    try:
        with open("course.txt", "r") as course_file:
            for line in course_file:
                course_id, cname, max_seats = line.strip().split(",")
                if cid == course_id:
                    course_found = True
                updated_courses.append([course_id, cname, int(max_seats)])  # Store all course data
    except FileNotFoundError:
        pass

    if not course_found:
        print(f"Course ID: {cid} not found. Please enter a valid course.")
        return

    # **Check if enrollment exists & remove it**
    try:
        with open("enrollments.txt", "r") as enrollment_file:
            for line in enrollment_file:
                try:
                    enrolment_sid, enrolment_cid, _ = line.strip().split(",")
                except ValueError:
                    continue  # Skip malformed lines

                if sid == enrolment_sid and cid == enrolment_cid:
                    enrollment_found = True
                else:
                    saved_enrollments.append(line)  # Keep valid enrollments

    except FileNotFoundError:
        pass

    if not enrollment_found:
        print(f"Student ID: {sid} is not enrolled in Course ID: {cid}. No course to drop.")
        return

    # **Write updated enrollments back to the file**
    with open("enrollments.txt", "w") as enrollment_file:
        enrollment_file.writelines(saved_enrollments)

    # **Increase seat count in `course.txt`**
    with open("course.txt", "w") as course_file:
        for course in updated_courses:
            if course[0] == cid:  # Increase seats for the dropped course
                course[2] += 1
            course_file.write(f"{course[0]},{course[1]},{course[2]}\n")

    print(f"Student ID: {sid} has successfully dropped Course ID: {cid}. Seat has been returned.")


def view_courses():
    try:
        # Read all course details
        with open("course.txt", "r") as courses:
            course_list = courses.readlines()

        # Loop through courses one by one
        for line in course_list:
            cid, cname, max_seats = line.strip().split(",")

            # Count seats taken for this specific course
            seats_taken = 0
            try:
                with open("enrollments.txt", "r") as enrollments:
                    for enroll_line in enrollments:
                        enrolment_cid = enroll_line.strip().split(",")[0]  # Extract enrolled course ID
                        if enrolment_cid == cid:  # Match with current course ID
                            seats_taken += 1  # Increase seat count
            except FileNotFoundError:
                pass  # No enrollments yet

            # Calculate remaining seats
            remaining_seats = int(max_seats) - seats_taken
            print(f"Course ID: {cid} | Course Name: {cname} | Remaining Seats: {remaining_seats}")

    except FileNotFoundError:
        print("No available course now.")


def view_students():
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


while True:
    print("=============================================")
    print("Sunway Course Registration System")
    print("Enter [1] To add a new student")
    print("Enter [2] To add a new course")
    print("Enter [3] To enrol in a course")
    print("Enter [4] To drop a course")
    print("Enter [5] to view available courses")
    print("Enter [6] To view student informations")
    print("Enter [7] to exit")

    try:
        selection = int(input("Enter your selection here: "))
    except ValueError:
        print("\nInvalid input! Please enter a number between 1 to 7.")
        input("Press Enter to continue...")  # Adds a small pause
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
            print("Invalid selection, please choose between 0 to 7")
