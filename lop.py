main_menu = True


while main_menu:
        print("Enter [1] To Add A New Student")
        print("Enter [2] To Add A New Course")
        print("Enter [3] To Enrol In A Course")
        print("Enter [4] To Drop A Course")
        print("Enter [5] to View Available Courses")
        print("Enter [6] To View Student Information")
        print("Enter [7] to Exit")
        selection  = int(input("Enter Your Number Here: "))

        match selection:
                        case 1:
                                with open("students.txt","a") as students:
                                        add_id = input("Please Enter Student ID: ").strip()
                                        add_name = input("Please Enter Student Name: ").strip()
                                        add_contact = int(input("Please Enter Student Contact: ")).strip()
                                        students.write(f"Student ID: {add_id}\nStudent Name: {add_name}\nStudent Contact: {add_contact}\n")
                                        print("Student Added Successfully!")
                                        print("===========================")

                        case 2:
                                with open("courses.txt", "a") as courses:
                                        add_id = input("Please Enter Course ID: ").strip()
                                        add_name = input("Please Enter Course Name: ").strip()
                                        max_seat = int(input("Please Enter Maximum Seats For The Course: ")).strip()
                                        courses.write(f"Course ID: {add_id}\nCourse Name: {add_name}\nMaximum Seats: {max_seat}\n")
                                        print("Course Added Successfully!")
                                        print("==========================")

                        case 7:
                                print("Exiting The Program. SEE YOU AGAIN!")
                                break


                        case _:
                                print("Invalid Selection, Please Choose Between 1 to 7")

