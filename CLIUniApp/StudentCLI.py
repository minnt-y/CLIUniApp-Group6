from studentManager import StudentManager


def student_subsystem(manager: StudentManager):
    while True:
        choice = input("Student System (l/r/x): ").strip().lower()

        if choice == "r":
            print("Student Sign Up")
            email = input("Email: ").strip()
            password = input("Password: ").strip()

            if not manager.validateEmail(email) or not manager.validatePassword(
                password
            ):
                print("Incorrect email or password format")
                continue
            else:
                print("Email and password formats acceptable")

            exists = any(s.getEmail() == email for s in manager.getAllStudents())
            if exists:
                matched_name = next(
                    (
                        s.getName()
                        for s in manager.getAllStudents()
                        if s.getEmail() == email
                    ),
                    "User",
                )
                print(f"Student {matched_name} already exists")
                continue

            name = input("Name: ").strip()
            student = manager.registerStudent(name, email, password)
            if student:
                print(f"Enrolling Student {name}")

        elif choice == "l":
            print("Student Sign In")
            email = input("Email: ").strip()
            password = input("Password: ").strip()

            if not manager.validateEmail(email) or not manager.validatePassword(
                password
            ):
                print("Incorrect email or password format")
                continue
            else:
                print("email and password formats acceptable")

            student = None
            for s in manager.getAllStudents():
                if s.getEmail() == email and s.getPassword() == password:
                    student = s
                    break

            if not student:
                print("Student does not exist")
                continue

            student_course_menu(manager, student)

        elif choice == "x":
            break


def student_course_menu(manager: StudentManager, student):
    while True:
        choice = input("Student Course Menu (c/e/r/s/x): ").strip().lower()

        if choice == "s":
            enrolled = student.viewEnrolmentList()
            count = len(enrolled)
            print(f"Showing {count} subjects")
            for sub in enrolled:
                print(sub)

        elif choice == "e":
            if len(student.viewEnrolmentList()) >= 4:
                print("Students are allowed to enrol in 4 subjects only")
                continue

            subject = manager.enrolSubject(student.getStudentID())
            if subject:
                print(f"Enrolling in Subject-{subject.getSubjectID()}")
                count = len(student.viewEnrolmentList())
                print(f"You are now enrolled in {count} out of 4 subjects")

        elif choice == "r":
            sub_id = input("Remove Subject by ID: ").strip()
            success = manager.removeSubject(student.getStudentID(), sub_id)
            if success:
                print(f"Droping Subject-{sub_id}")
                count = len(student.viewEnrolmentList())
                print(f"You are now enrolled in {count} out of 4 subjects")

        elif choice == "c":
            print("Updating Password")
            while True:
                new_pwd = input("New Password: ").strip()
                confirm_pwd = input("Confirm Password: ").strip()
                if new_pwd == confirm_pwd:
                    success = manager.changePassword(student.getStudentID(), new_pwd)
                    if success:
                        break
                    else:
                        print("Password format incorrect - try again")
                else:
                    print("Password does not match - try again")

        elif choice == "x":
            break
