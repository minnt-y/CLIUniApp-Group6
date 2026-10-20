import tkinter as tk
from PIL import Image, ImageTk


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x600")
        self.title("GUIUniApp")
        self.configure(bg="#27E4F5")
        self.resizable(False, False)
        
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
        emailField = tk.Entry(box_frame, textvariable=emailText)
        emailField.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
       
        # Password input field set up
        pwdText = tk.StringVar()
        pwdField = tk.Entry(box_frame, textvariable=pwdText)
        pwdField.grid(column=1, row=1, padx=5, pady=5, sticky=tk.N)
        
        # Quit button set up
        quitBtn = tk.Button(box_frame, text='Quit',command=lambda: self.quit())
        quitBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        
        # Login button set up
        loginBtn = tk.Button(box_frame, text='Login',command=self.login)
        loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
    
    def login():
        return