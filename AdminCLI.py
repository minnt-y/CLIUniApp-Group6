from studentManager import StudentManager


def admin_subsystem(manager: StudentManager):
    while True:
        choice = input("Admin System (c/g/p/r/s/x): ").strip().lower()

        if choice == "c":
            print("Clearing students database")
            confirm = (
                input("Are you sure you want to clear the database (Y)ES/(N)O: ")
                .strip()
                .upper()
            )
            if confirm == "Y" or confirm == "YES":
                manager.clearAllStudents()
                print("Students data cleared")

        elif choice == "g":
            print("Grade Grouping")
            grades_dict = manager.getStudentsByGrade()
            has_any = any(item_list for item_list in grades_dict.values())
            if not has_any:
                print("      < Nothing to Display >")
            else:
                for grade, item_list in grades_dict.items():
                    if item_list:
                        for student, avg_mark in item_list:
                            grade_str = f"{grade:>2}"
                            print(
                                f"{grade} --> [{student} --> GRADE:  {grade_str} - MARK: {avg_mark:.2f}]"
                            )
