from studentManager import StudentManager
from AdminCLI import admin_subsystem
from StudentCLI import student_subsystem


def UniSystem():
    manager = StudentManager()

    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").strip().upper()

        if choice == "A":
            admin_subsystem(manager)
        elif choice == "S":
            student_subsystem(manager)
        elif choice == "X":
            print("Thank You")
            break


if __name__ == "__main__":
    UniSystem()
