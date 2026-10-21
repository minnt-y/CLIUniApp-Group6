# 32555 - Assignment 1 Part 2 - UniApp (CLI & GUI)

**Programming language**: Python 3.14
**Required labraries**: Standard python librabries only

Project Structure
<pre>

├── UniSystem.py            # Application entry point and menu router for CLIUniApp
├── subject.py         # Subject model (manages 3-digit IDs, random marks [25-100], and grade calculations)
├── student.py         # Student model (manages 6-digit IDs, credentials, and up to 4 enrolled subjects)
├── studentBase.py     # Persistence layer (handles binary read/write operations for students.data)
├── StudentManager.py  # Controller (manages business logic, password validation, and high-level system actions)
├── AdminCLI.py        # Admin subsystem CLI interface
├── StudentCLI.py      # Student subsystem CLI interface
└── students.data      # Local binary file for persistent student records (auto-generated)
├── GUI
    ├── GUIEntry.py       # GUI entry point for CLIUniApp
    └── loginWindow.py    # Login window
