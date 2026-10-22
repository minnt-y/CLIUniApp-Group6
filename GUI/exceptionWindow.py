import tkinter as tk
import sys
import os

from PIL import Image, ImageTk

# # 获取当前文件(loginWindow.py)所在目录(GUI)的上一级目录(即项目根目录)，并加入系统路径
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from student import Student
# from studentManager import StudentManager

class ExceptionWindow(tk.Toplevel):
    def __init__(self, master:tk.Toplevel, error_msg:str):
        super().__init__(master=master)
        self.geometry("350x200")
        self.title("GUIUniApp")
        self.configure(bg="white")
        self.resizable(False, False)
        
        # Make sure this window will always appear 
        # in front of the main window.
        self.transient(master)
        # Make sure the main window cannot be used 
        # when this window is popped out
        self.grab_set()
        # Stay focus on this window when encontering error
        self.focus_force()
        
        # Error box frame set up
        error_box = tk.LabelFrame(self, text="Oops! You Got an Error!!!", 
                                  fg="#F52727", bg="white", font="Helvetice 15 bold")
        error_box.place(rely=0.5, relx=0.5, anchor='center')
        # Error image set up
        error_img = Image.open("./GUI/Photos/error_sign.png").resize((100, 100))
        self.tk_student_img = ImageTk.PhotoImage(error_img)
        error_imglbl = tk.Label(error_box, image=self.tk_student_img, bg="white")
        error_imglbl.image = self.tk_student_img 
        error_imglbl.pack(side=tk.LEFT, padx=(0, 15))
        # Error message set up
        error_message = tk.Message(error_box, text=error_msg, 
                                   fg="black", font="Helvetica 12 bold", bg="white", justify='left')
        error_message.pack(pady=10, padx=10, side=tk.LEFT)
        
        # Not whole mainloop longer executing until the user 
        # close this window
        self.wait_window(self)
        
        
        