# 32555 - Assignment 1 Part 2 - UniApp (CLI & GUI)

## 1. Project Overview

**UniApp** is a University Management System developed in Python 3.14, featuring both a Command Line Interface and a Graphical User Interface. The project is built following OOP principles, implements data persistence and error-handling mechanisms.

## 2. System Requirements
* **Programming language**: Python 3.14
* **Required labraries**: Standard python librabries + **PIL (Pillow)** for GUI image processing
* **Operating System**: Windows, macOS, Linux

## 3. Setup & Installation
* Clone or download the repository to your local machine:
   ```bash
   git clone [https://github.com/minnt-y/CLIUniApp-Group6.git](https://github.com/minnt-y/CLIUniApp-Group6.git)


## 4. Project Structure
<pre>

├── UniSystem.py            # Application entry point and menu router for CLIUniApp
├── subject.py         # Subject model (manages 3-digit IDs, random marks [25-100], and grade calculations)
├── student.py         # Student model (manages 6-digit IDs, credentials, and up to 4 enrolled subjects)
├── studentBase.py     # Persistence layer (handles binary read/write operations for students.data)
├── StudentManager.py  # Controller (manages business logic, password validation, and high-level system actions)
├── AdminCLI.py        # Admin subsystem CLI interface
├── StudentCLI.py      # Student subsystem CLI interface
├── students.data      # Local binary file for persistent student records (auto-generated)
└── GUI
    ├── dashboardWindow.py # Dashboard
    ├── enrolWindow.py     # Window for course selection
    ├── exceptionWindow.py # Exception Window
    ├── GUIEntry.py        # GUI entry point for GUIUniApp
    ├── GUIExceptions.py   # GUI Exception Class
    ├── loginWindow.py     # Login window
    ├── subjectWindow.py   # Window for viewing enrolled subject information
    └── Photos             # Folders for image data
        ├── enrolment.jpg
        ├── error_sign.png 
        ├── students.jpg
        ├── study_img.jpeg
        └── subject.png 
</pre>

