# 32555 - Assignment 1 - UniApp (CLI & GUI)

**Programming language**: pyhton 3.14
**Required labraries**: Standard python librabries only

1. Run the CLI Application ('CLIUniApp')
'''bash
python main.py

2. Run the GUI Application
python GUI.py

CLIUniApp
├── main.py           # Application entry point and menu router for CLIUniApp
├── subject.py        # Subject model (manages 3-digit IDs, random marks[0-100], and grade calculations)
├── student.py        # Student model (manages 6-digit IDs, credentials, and up to 4 enrolled subjects)
├── studentbase.py    # Persistence layer (handles binary read/write operations for students.data)
├── studentmanager.py # Controller (manages business logic, regex validation, and high-level system actions)
├── GUI.py            # GUIUniApp implementation for the graphical challenge task
└── students.data     # Local binary file for persistent student records (auto-generated)