import tkinter as tk
import sys
import os

from tkinter import ttk
from PIL import Image, ImageTk

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

from CLIUniApp.student import Student
from CLIUniApp.subject import Subject
from CLIUniApp.studentManager import StudentManager


class SubjectWindow(tk.Toplevel):
    def __init__(self, master: tk.Toplevel, manager: StudentManager, user: Student):
        super().__init__(master=master)
        # Hide the master (Login Window)
        master.withdraw()
        # Record the login student name and id
        self.user_name = user.getName()
        self.user_id = user.getStudentID()

        self.geometry("800x600")
        self.title("GUIUniApp - Course View")
        self.configure(bg="#27E4F5")
        self.resizable(False, False)

        # Greeting message set up
        greet_msg = tk.Label(
            self,
            text=f"Hello! {user.getName()} (ID: {user.getStudentID()})!\nPlease find below your enrolled courses.",
            fg="#D72411",
            bg="#27E4F5",
            font="TkHeadingFont 13 bold",
        )
        greet_msg.place(relx=0.03, rely=0.03, anchor="w")

        # Clickable text 'Go Back' set up
        def go_back():
            master.wm_deiconify()
            self.destroy()

        back_press = tk.Message(
            self,
            text="Go Back<--",
            fg="black",
            font="Helvetica 12 bold underline",
            bg="yellow",
        )
        back_press.place(relx=0.9, rely=0.03, anchor="e")
        back_press.bind("<Button-1>", lambda e: go_back())

        # Message label
        self.msg = tk.Label(
            self,
            text=f"Current Enrolment Table",
            fg="green3",
            bg="#FBFF0E",
            font="Helvetica 25 bold",
        )
        self.msg.place(relx=0.5, rely=0.2, anchor="center")

        # Column index set up for controling the properties of column name
        columns = ("id", "mark", "grade")
        # Create a table view (Treeview) for showing the subjects
        self.enrol_table = ttk.Treeview(self, columns=columns, show="headings")
        # Set up the column name that is actually shown in subject window
        self.enrol_table.heading("id", text="Subject ID")
        self.enrol_table.heading("mark", text="Mark")
        self.enrol_table.heading("grade", text="Grade")
        # Set up the properties for each column name
        self.enrol_table.column("id", width=100, anchor="center")
        self.enrol_table.column("mark", width=100, anchor="center")
        self.enrol_table.column("grade", width=100, anchor="center")
        # Insert current course enrolment data of current login student
        all_courses = manager.viewEnrolmentList(self.user_id)
        for c in all_courses:
            self.enrol_table.insert(
                "", tk.END, values=(c.getSubjectID(), c.getMark(), c.getGrade())
            )
        # Put enrol table into current window
        self.enrol_table.place(relx=0.5, rely=0.5, anchor="center")

        # Add an image
        view_1_img = Image.open("./GUIUniApp/Photos/view_1.jpg").resize((255, 150))
        self.tk_view1_img = ImageTk.PhotoImage(view_1_img)
        view1_imglbl = tk.Label(self, image=self.tk_view1_img, bg="#27E4F5")
        view1_imglbl.place(relx=0.5, rely=0.8, anchor="center")
