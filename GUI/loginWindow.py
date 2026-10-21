import tkinter as tk
import sys
import os

from GUIExceptions import EmptyFieldException, InvalidEmailFormatException
from exceptionWindow import ExceptionWindow
from PIL import Image, ImageTk

# 获取当前文件(loginWindow.py)所在目录(GUI)的上一级目录(即项目根目录)，并加入系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from student import Student
from studentManager import StudentManager


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x600")
        self.title("GUIUniApp")
        self.configure(bg="#27E4F5")
        self.resizable(False, False)
        
        self.manager = StudentManager()
        
        # Set window top title
        top_title = tk.Label(self, text="Welcome to University Student Interactive System", 
                               font="Georgia 30 bold", bg="#27E4F5", fg="#D72411")
        top_title.pack(pady=(20,10))
        
        # Image set up
        students_img = Image.open("./GUI/Photos/students.jpg").resize((300, 200))
        tk_student_img = ImageTk.PhotoImage(students_img)
        students_imglbl = tk.Label(self, image=tk_student_img, bg="#27E4F5")
        students_imglbl.image = tk_student_img
        students_imglbl.pack(pady=10)
        
        # Box frame set up for containing all widgets in login window
        box_frame = tk.LabelFrame(self, text="Student Login", bg="#27E4F5", 
                              fg='green', padx=80, pady=50, font='Helvetice 20 bold')
        box_frame.columnconfigure(0, weight=1)
        box_frame.columnconfigure(1, weight=3)
        box_frame.place(relx=0.5, rely=0.7, anchor='center')
        
        # Email label set up 
        emailLbl = tk.Label(box_frame, text="Email:",justify='left',fg='#B427F5',
                    font="Helvetica 20 bold", bg='#27E4F5', )
        emailLbl.grid(column=0,row=0,padx=5,pady=5,sticky=tk.W)
        
        # Password label set up
        passwordLbl = tk.Label(box_frame, text="Password:",justify='left',fg='#B427F5',
                    font="Helvetica 20 bold", bg='#27E4F5')
        passwordLbl.grid(column=0,row=1,padx=5,pady=5,sticky=tk.W)
        
        # Email input field set up
        emailText = tk.StringVar()
        self.emailField = tk.Entry(box_frame, textvariable=emailText)
        self.emailField.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
       
        # Password input field set up
        pwdText = tk.StringVar()
        self.pwdField = tk.Entry(box_frame, textvariable=pwdText, show="*")
        self.pwdField.grid(column=1, row=1, padx=5, pady=5, sticky=tk.N)
        
        # Quit button set up
        quitBtn = tk.Button(box_frame, text='Quit',command=lambda: self.quit())
        quitBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        
        # Login button set up
        loginBtn = tk.Button(box_frame, text='Login',command=self.handle_login)
        loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
        # Show the current window
        tk.mainloop()
    
    def handle_login(self):
        try:
            self.email_check(self.emailField.get())
        except InvalidEmailFormatException as e:
            self.clear_email()
            ExceptionWindow(self, str(e))
    
    def email_check(self, email:str):
        if not self.manager.validateEmail(email):
            raise InvalidEmailFormatException()
        return True
    
    def clear_email(self):
        self.emailField.delete(0, tk.END)
    
    def clear_pwd(self):
        self.pwdField.delete(0, tk.END)