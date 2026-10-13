from StudentManager import StudentManager
from AdminCLI import admin_subsystem
from StudentCLI import student_subsystem


def main():
    manager = StudentManager()

    while True:
        print("\n--- UNIVERSITY SYSTEM: ADMIN & STUDENT ---")
        print("1. Admin Subsystem\n2. Student Subsystem\n3. Exit")

        choice = input("Enter(1-3): ").strip()

        if choice == "1":
            admin_subsystem(manager)
        elif choice == "2":
            student_subsystem(manager)
        elif choice == "3":
            print("\nExited.")
            break


if __name__ == "__main__":
    main()
