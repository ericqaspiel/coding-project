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

    # getting input from user for contact information and if user enter anything beside integer then will show error
    contact_info = input("Phone number: ").strip()
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
        print(f"Student ID: {sid} | Student Name: {sname} added successfully!\n")


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
        print(f"(Course ID: {cid}) (Course Name: {cname}) (Max Seats: {max_seats}) added successfully!\n")


# def enrol_course():
#     student_exists = 1
#     course_exists = 1
#     enrollment_exists = 1

#     sid = input("Enter student ID to enrol: ")
#     if not sid.isdigit():
#         print("Please enter the valid number for student ID: ")
#         return

#     cid = input("Enter student course ID to enrol: ")
#     if not cid:
#         print("Please enter valid course ID: ")
#         return

#     with open("student.txt", "r") as student_file:
#         for line in student_file:
#             if sid == line.strip().split(",")[0]:
#                 student_exists = 2
#                 break
#             else:
#                 print("Student Does not exist.")

#     if student_exists == 2:
#         with open("course.txt", "r") as course_file:
#             for line in course_file:
#                 if cid == line.strip().split(",")[0]:
#                     course_exists = 2
#                     break
#                 else:
#                     print("Course doesnt exist.")

#     if course_exists == 2:
#         with open("enrollments.txt", "r") as enrollment_file:
#             for line in enrollment_file:
#                 if sid == line.strip().split(",")[0] and cid == line.strip().split(",")[1]:
#                     enrollment_exists = 2
#                     print("Student Already Enrolled")
#                     break

#     if student_exists == 2 and course_exists == 2 and enrollment_exists == 1:
#         with open("enrollments.txt", "a") as enrollment_file:
#             enrollment_file.write(f"{sid},{cid}\n")
#             print(f"(Student ID:{sid}) (Course Id:{cid}) Enrolled Successfully!\n")


# def enrol_course():
#     sid = input("Enter student ID to enrol: ").strip()
#     if not sid.isdigit():
#         print("Please enter the valid number for student ID")
#         return

#     cid = input("Enter student course ID to enrol: ").strip()
#     if not cid:
#         print("Please enter valid course ID")
#         return

#     student_found = False
#     course_found = False

#     with open("student.txt", "r") as student_file:
#         for line in student_file:
#             if sid == line.strip().split(",")[0]:
#                 student_found = sid
#             else:
#                 print("Student is not registered")

#     with open("course.txt", "r") as course_file:
#         for line in course_file:
#             if cid == line.strip().split(",")[0]:
#                 course_found = True
#             else:
#                 print("Course is not available")

#     if student_found == True and course_found == True:
#         with open("enrollments.txt", "a") as enrollment_file:
#             enrollment_file.write(f"{sid},{cid}\n")
#             print(f"Student ID: {sid} has succesfully enrolled in course ID: {cid}\n")


def enrol_course():
    sid = input("Enter student ID to enrol: ").strip()
    if not sid.isdigit():
        print("Please enter the valid number for student ID")
        return

    cid = input("Enter student course ID to enrol: ").strip()
    if not cid.isdigit():
        print("Please enter valid course ID")
        return

    student_not_found = True
    course_not_found = True
    try:
        with open("student.txt", "r") as student_file:
            for line in student_file:
                if sid == line.strip().split(",")[0]:
                    student_not_found = False
                    break
    except FileNotFoundError:
        pass
    finally:
        if student_not_found:
            print("Student is not registered")
            return

    course_id_seats_left = 0
    try:
        with open("course.txt", "r") as course_file:
            for line in course_file:
                course_id, _, max_seats = line.split(",")
                if cid == course_id:
                    course_not_found = True
                    course_id_seats_left = max_seats
                    break
    except FileNotFoundError:
        pass
    finally:
        if course_not_found:
            print("Course is not available")
            return

    with open("enrollments.txt", "r") as enrollment_file:
        for line in enrollment_file.readlines():
            enrolment_sid, enrolment_cid, enrolment_date = line.split(",")
            if sid == enrolment_sid and cid == enrolment_cid:
                print(f"Student ID: {sid} has already enrolled in course ID: {cid} on the {enrolment_date}")
                break
            if cid == enrolment_cid:
                course_id_seats_left -= 1

    # check if seats available
    if course_id_seats_left == 0:
        print(f"Unable to enrol student in course ID: {cid} as there is no seats left")
        return

    # add student into enrollments if all conditions is satisfied
    with open("enrollments.txt", "a") as enrollment_file:
        enrolment_date = datetime.today().strftime("%d-%m-%Y")
        enrollment_file.write(f"{sid},{cid},{enrolment_date}\n")
        print(f"Student ID: {sid} has succesfully enrolled in course ID: {cid} on the {enrolment_date}\n")


def drop_course():
    # TODO: input for student id

    # TODO: read enrollment file and find sid if exist
    saved_enrollments = []
    enrollment_not_found = True
    try:
        with open("enrollments.txt", "r") as enrollment_file:
            for line in enrollment_file.readlines():
                enrolment_sid = line.split(",")[0]
                if sid == enrolment_sid:
                    # exist case handle print
                    sid = enrolment_sid
                    enrollment_not_found = False
                else:
                    saved_enrollments.append(line)
    except FileNotFoundError:
        pass
    finally:
        if enrollment_not_found:
            # TODO: write proper message with sid
            print("No course to drop...")
            return

    # TODO: overwrite enrollment.txt if there is a drop course
    with open("enrollment.txt", "w") as enrollment_file:
        enrollment_file.writelines(saved_enrollments)

    print("Successful message???")


def view_courses():
    try:
        with open("course.txt", "r") as courses:
            course_list = courses.readlines()

        # TODO: read enrollment file and count seats taken
        seats_taken = 0
        ...
        seats_taken += 1
        for line in course_list:
            cid, cname, max_seats = line.strip().split(",")
            print(f"Course ID: {cid} | Course Name: {cname} | Remaining Seats: {max_seats - seats_taken}")
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
        case 4:
            drop_course()
        case 5:
            view_courses()
        case 6:
            view_students()
        case 7:
            print("Exiting The Program. SEE YOU AGAIN!")
            break
        case _:
            print("Invalid Selection, Please Choose Between 1 to 7")
