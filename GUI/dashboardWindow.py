import tkinter as tk
import sys
import os

from PIL import Image, ImageTk

# 获取当前文件(loginWindow.py)所在目录(GUI)的上一级目录(即项目根目录)，并加入系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student  # 现在这行就不会报错了
from studentManager import StudentManager

class Dashboard(tk.Toplevel):
    def __init__(self, master:tk.Tk, user: Student, manager: StudentManager):
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
        
        tk.mainloop()
        
        
        
        
        
        