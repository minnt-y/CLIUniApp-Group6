import tkinter as tk
import sys
import os

from PIL import Image, ImageTk

# 获取当前文件(loginWindow.py)所在目录(GUI)的上一级目录(即项目根目录)，并加入系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student
from studentManager import StudentManager

class SubjectWindow(tk.Toplevel):
    def __init__(self, master:tk.Toplevel, manager: StudentManager, user: Student):
        super().__init__(master=master)
        # Hide the master (Login Window)
        master.withdraw()
        # Record the login student name and id
        self.user_name = user.getName()
        self.user_id = user.getStudentID()
                
        self.geometry("800x600")
        self.title("GUIUniApp")
        self.configure(bg="#27E4F5")
        self.resizable(False, False)
                
        # Greeting message set up
        greet_msg = tk.Label(self, text=f"Hello! {user.getName()} (ID: {user.getStudentID()})!\nPlease find below your enrolled courses.", 
                                    fg="#D72411", bg="#27E4F5", font="TkHeadingFont 13 bold")
        greet_msg.place(relx=0.03, rely=0.03, anchor='w')
        # Clickable text 'Go Back' set up
        def go_back():
            master.wm_deiconify()
            self.destroy()
        back_press = tk.Message(self, text="Go Back<--", fg="black", font="Helvetica 12 bold underline", bg="yellow")
        back_press.place(relx=0.9, rely=0.03, anchor="e")
        back_press.bind("<Button-1>", lambda e:go_back())