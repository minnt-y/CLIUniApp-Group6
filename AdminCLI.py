from studentManager import StudentManager


def admin_subsystem(manager: StudentManager):
    while True:
        print("\n=== ADMIN MENU ===")
        print(
            "1. View All Students\n2. View Students by Grade\n3. Categorize Students (PASS/FAIL)\n4. Remove Student\n5. Clear All Records\n6. Back"
        )
        choice = input("Enter (1-6): ").strip()

        if choice == "1":
            print("\n--- All Registered Students ---")
            students = manager.getAllStudents()
            if not students:
                print("No registered students found.")
            else:
                print(f"Total Registered Students: {len(students)}")
                for s in students:
                    print(f"{s}")

        elif choice == "2":
            print("\n--- Students by Grade ---")
            grades_dict = manager.getStudentsByGrade()
            for grade, item_list in grades_dict.items():
                print(f"Grade [{grade}]")
                if not item_list:
                    print("  (None)")
                for student, avg_mark in item_list:
                    print(
                        f"Name: {student.getName()} -- Student ID: {student.getStudentID()} -- Mark: {avg_mark:.1f}"
                    )

        elif choice == "3":
            print("\n--- Categorize Students (PASS/FAIL) ---")
            pf_dict = manager.categorizePassFail()
            print(f"PASS (Total: {len(pf_dict['PASS'])})")
            for s in pf_dict["PASS"]:
                print(f"{s}")

            print(f"FAIL (Total: {len(pf_dict['FAIL'])})")
            for s in pf_dict["FAIL"]:
                print(f"{s}")

        elif choice == "4":
            print("\n--- Remove a Student ---")
            students = manager.getStudents()
            if not students:
                print("No registered students found.")
                continue

            print("Current Students List:")
            for s in students:
                print(f"{student}")

            sid = input("\nEnter 6-digit Student ID to remove: ").strip()
            if manager.removeStudent(sid):
                print(f"Student ID {sid} successfully removed.")
            else:
                print(f"Error: Student ID {sid} not found.")

        elif choice == "5":
            confirm = input("Confirm clear?(y/n): ").strip()
            if confirm.lower() == "y":
                manager.clearAllStudents()
                print("All records and file data cleared.")
            else:
                print("Operation cancelled.")

        elif choice == "6":
            break
