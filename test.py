courses = []

def add_course():
    try:
        cid = input("Course ID: ")
        cname = input("Course name: ").strip()
        max_seats = int(input("Max seats: "))
    except TypeError:
        print("Please enter a valid number for Course ID and Max Seats.")
        return

    courses.append({"id": cid, "name": cname, "max": max_seats, "remaining": max_seats})
    print("Course added!")

def view_courses():
    if not courses:
        print("No courses available.")
        return

    for course in courses:
        print(f'{course["id"]} - {course["name"]}: {course["remaining"]} out of {course["max"]} seats left')

while True:
    print("Enter [1] To Add A New Student")
    print("Enter [2] To Add A New Course")
    print("Enter [3] To Enrol In A Course")
    print("Enter [4] To Drop A Course")
    print("Enter [5] to View Available Courses")
    print("Enter [6] To View Student Information")
    print("Enter [7] to Exit")
    selection = int(input("Enter Your Selection Here: "))

    match selection:
        case 2:
            add_course()
        case 5:
            view_courses()
        case 7:
            print("Exiting The Program. SEE YOU AGAIN!")
            break
        case _:
            print("Invalid Selection, Please Choose Between 1 to 7")
