from StudentManager import StudentManager


def student_subsystem(manager: StudentManager):
    while True:
        print("\n=== STUDENT MENU ===")
        print("1. Register\n2. Login\n3. Back")
        choice = input("Enter (1-3): ").strip()

        if choice == "1":
            print("\n--- Student Registration ---")
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            password = input("Password: ").strip()

            result = manager.registerStudent(name, email, password)

            if result:
                print(f"\nRegistration successful! Student ID: {result.getStudentID()}")
            else:
                print(
                    "\nRegistration failed. Please check email format, password criteria, or if the email is already registered."
                )

        elif choice == "2":
            print("\n--- Student Login ---")
            student_id = input("Student ID: ").strip()
            password = input("Password: ").strip()

            student = manager.loginStudent(student_id, password)
            if student:
                print(f"\nWelcome back, {student.getStudentID()}!")
                student_logged_in_menu(manager, student)
            else:
                print("\nInvalid Student ID or Password.")

        elif choice == "3":
            break


def student_logged_in_menu(manager: StudentManager, student):
    while True:
        print(f"\n--- STUDENT ID: {student.getStudentID()} ---")
        print(
            "1. Enrol\n2. Remove Subject\n3. View Enrolments\n4. Change Password\n5. Logout"
        )

        choice = input("Enter (1-5): ").strip()

        if choice == "1":
            print("\n--- Enrol in a Subject ---")
            subject = manager.enrolSubject(student.getStudentID())
            if subject:
                print(f"Enrolled: {subject}")
            else:
                print(f"Error: Max 4 subjects reached.")

        elif choice == "2":
            print("\n--- Remove a Subject ---")
            enrolled = student.viewEnrolmentList()
            if not enrolled:
                print("[Info] Not enrolled in any subjects.")
                continue

            print("Current subjects:")
            for sub in enrolled:
                print(
                    f"Subject ID: {sub.getSubjectID()} -- Mark: {sub.getMark()} -- Grade: {sub.getGrade()}"
                )

            sub_id = input("Subject ID to remove: ").strip()
            success = manager.removeSubject(student.getStudentID(), sub_id)
            if success:
                print(f"Subject {sub_id} has been removed.")
            else:
                print(f"Subject ID {sub_id} not found in enrolment list.")

        elif choice == "3":
            print("\n--- Current Enrolment List ---")
            enrolled = student.viewEnrolmentList()
            if not enrolled:
                print("Enrolment list is empty.")
            else:
                for subject in enrolled:
                    print(f"{subject}")

        elif choice == "4":
            print("\n--- Change Password ---")
            new_pwd = input("New password: ").strip()
            success = manager.changePassword(student.getStudentID(), new_pwd)
            if success:
                print("Password changed.")
            else:
                print(f"Error: Invalid format.")

        elif choice == "5":
            break
