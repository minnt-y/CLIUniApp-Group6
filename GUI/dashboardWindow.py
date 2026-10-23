import tkinter as tk
import sys
import os

from PIL import Image, ImageTk
from enrolWindow import EnrolWindow
from subjectWindow import SubjectWindow

# 获取当前文件(loginWindow.py)所在目录(GUI)的上一级目录(即项目根目录)，并加入系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student
from studentmanager import StudentManager


class Dashboard(tk.Toplevel):
    def __init__(self, master: tk.Tk, user: Student, manager: StudentManager):
        super().__init__(master=master)
        # Hide the master (Login Window)
        master.withdraw()
        # Record the login student name and id
        self.user_name = user.getName()
        self.user_id = user.getStudentID()

        self.geometry("800x600")
        self.title("GUIUniApp - Dashboard")
        self.configure(bg="#27E4F5")
        self.resizable(False, False)

        # Greeting message set up
        greet_msg = tk.Label(
            self,
            text=f"Hello! {user.getName()} (ID: {user.getStudentID()})!",
            fg="#D72411",
            bg="#27E4F5",
            font="TkHeadingFont 13 bold",
        )
        greet_msg.place(relx=0.03, rely=0.03, anchor="w")

        # Clickable text 'log out' set up
        def back_to_login():
            master.wm_deiconify()
            self.destroy()

        back_press = tk.Message(
            self,
            text="Log Out<--",
            fg="black",
            font="Helvetica 12 bold underline",
            bg="yellow",
        )
        back_press.place(relx=0.9, rely=0.03, anchor="e")
        back_press.bind("<Button-1>", lambda e: back_to_login())

        # Dashboard frame
        dashboard_frame = tk.LabelFrame(
            self,
            text="Dashboard",
            bg="#27E4F5",
            fg="green",
            padx=20,
            pady=20,
            font="Helvetice 20 bold",
        )
        dashboard_frame.columnconfigure(0, weight=1)
        dashboard_frame.columnconfigure(1, weight=1)
        dashboard_frame.place(relx=0.5, rely=0.3, anchor="center")

        # Dashboard Img
        dash_img = Image.open("./GUI/Photos/study_img.jpg").resize((400, 200))
        tk_dash_img = ImageTk.PhotoImage(dash_img)
        dash_imglbl = tk.Label(self, image=tk_dash_img, bg="#27E4F5")
        dash_imglbl.image = tk_dash_img
        dash_imglbl.place(relx=0.5, rely=0.6, anchor="n")

        # Clickable img to 'Course Enrolment'
        enrol_img = Image.open("./GUI/Photos/enrolment.jpg").resize((220, 150))
        self.tk_enrol_img = ImageTk.PhotoImage(enrol_img)
        enrol_imglbl = tk.Label(
            dashboard_frame, image=self.tk_enrol_img, bg="#27E4F5", cursor="hand2"
        )
        enrol_imglbl.grid(column=0, row=0, padx=10, pady=10)
        # Enrolment label
        enrol_lbl = tk.Label(
            dashboard_frame,
            text="Enrol a Course",
            fg="green3",
            bg="#FBFF0E",
            font="TkHeadingFont 13 bold",
        )
        enrol_lbl.grid(column=0, row=1, pady=(0, 10))

        # Click event setup for going to 'Course Enrolment Window'
        def go_to_enrolment():
            EnrolWindow(self, manager, user)

        enrol_imglbl.bind("<Button-1>", lambda e: go_to_enrolment())

        # Clickable img to 'View Courses'
        sub_img = Image.open("./GUI/Photos/subject.png").resize((220, 150))
        self.tk_sub_img = ImageTk.PhotoImage(sub_img)
        sub_imglbl = tk.Label(
            dashboard_frame, image=self.tk_sub_img, bg="#27E4F5", cursor="hand2"
        )
        sub_imglbl.grid(column=1, row=0, padx=10, pady=10)
        # Subject label
        sub_lbl = tk.Label(
            dashboard_frame,
            text="View Enrolled Courses",
            fg="green3",
            bg="#FBFF0E",
            font="TkHeadingFont 13 bold",
        )
        sub_lbl.grid(column=1, row=1, pady=(0, 10))

        # Click event setup for going to 'View Courses Window'
        def go_to_subject_view():
            SubjectWindow(self, manager, user)

        sub_imglbl.bind("<Button-1>", lambda e: go_to_subject_view())
