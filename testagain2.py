def enrol_course():
    sid = input("Enter student ID to enrol: ")
    if not sid.isdigit():
        print("Please enter the valid number for student ID")
        return

    cid = input("Enter student course ID to enrol: ")
    if not cid:
        print("Please enter valid course ID")
        return

    try:
        with open("student.txt", "r") as student_file:
            for line in student_file:
                if sid == line.strip().split(",")[0]:
                    with open("course.txt", "r") as course_file:
                        for line in course_file:
                            if cid == line.strip().split(",")[0]:
                                with open("enrollments.txt", "a") as enrollment_file:
                                    enrollment_file.write(f"{sid},{cid}")
    except:
        print("This student is not registered")
        return

    print(f"Student ID: {sid} has succesfully enrolled in course ID: {cid}\n")
