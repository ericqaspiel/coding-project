def add_course():
    # Getting input from user for course ID & course name
    cid = input("Course ID: ").strip()
    cname = input("Course name: ").strip()

    # Getting input from user for max seats, ensuring input is an integer
    try:
        max_seats = int(input("Max seats: ").strip())
    except ValueError:
        print("Please enter a valid number for seats.")
        return

    # Checking if course exists in the file
    try:
        with open('course.txt', 'r') as courses:
            for line in courses:
                c_id, c_name, c_seats = line.strip().split(",")  # Split line by comma
                if c_id == cid:  # Compare input ID with stored ID
                    print("Course Is Already Existed!")
                    return
    except FileNotFoundError:
        print("New file for course created!")

    # Append the new course to the file
    with open('course.txt', 'a') as courses:
		courses.write("{cid},{cname},{max_seats}")
        print("Course added successfully!")

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
        case 5:
            view_courses()
        case 7:
            print("Exiting The Program. SEE YOU AGAIN!")
            break
        case _:
            print("Invalid Selection, Please Choose Between 1 to 7")
