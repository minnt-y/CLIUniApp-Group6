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
                                f"{grade} --> [{student.getName()} :: {student.getStudentID()} --> GRADE:  {grade_str} - MARK: {avg_mark:.2f}]"
                            )

        elif choice == "p":
            print("PASS/FAIL Partition")
            pf_dict = manager.categorizePassFail()

            def format_pf_student(student):
                avg = student.getAverageMark()
                if avg >= 85:
                    g = "HD"
                elif avg >= 75:
                    g = "D"
                elif avg >= 65:
                    g = "C"
                elif avg >= 50:
                    g = "P"
                else:
                    g = "Z"
                return f"{student} --> GRADE:  {g:>2} - MARK: {avg:.2f}"

            fail_list = [format_pf_student(s) for s in pf_dict["FAIL"]]
            pass_list = [format_pf_student(s) for s in pf_dict["PASS"]]

            print(f"FAIL --> [{', '.join(fail_list)}]")
            print(f"PASS --> [{', '.join(pass_list)}]")

        elif choice == "r":
            sid = input("Remove by ID: ").strip()
            exists = any(s.getStudentID() == sid for s in manager.getAllStudents())
            if exists:
                print(f"Removing Student {sid} Account")
                manager.removeStudent(sid)
            else:
                print(f"Student {sid} does not exist")

        elif choice == "s":
            print("Student List")
            students = manager.getAllStudents()
            if not students:
                print("      < Nothing to Display >")
            else:
                for s in students:
                    print(s)

        elif choice == "x":
            break
