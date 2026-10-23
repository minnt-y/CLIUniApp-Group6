import tkinter as tk
import tkinter.messagebox as mb
import sys
import os

from PIL import Image, ImageTk
from GUIExceptions import EnrolmentExceedLimitException, CourseDeletionException
from exceptionWindow import ExceptionWindow

# 获取当前文件(loginWindow.py)所在目录(GUI)的上一级目录(即项目根目录)，并加入系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student
from subject import Subject
from studentManager import StudentManager

class EnrolWindow(tk.Toplevel):
    def __init__(self, master:tk.Toplevel, manager: StudentManager, user: Student):
        super().__init__(master=master)
        self.manager = manager
        self.user = user
        # Hide the master (Dashboard Window)
        master.withdraw()
        # Record the login student name and id
        self.user_name = user.getName()
        self.user_id = user.getStudentID()
        # Record the current enrolled courses for the login student
        self.current_courses = manager.viewEnrolmentList(self.user_id)
                
        self.geometry("800x600")
        self.title("GUIUniApp - Course Enrolment")
        self.configure(bg="#27E4F5")
        self.resizable(False, False)
                
        # Greeting message set up
        greet_msg = tk.Label(self, text=f"Hello! {user.getName()} (ID: {user.getStudentID()})!\nPlease enrol your course.", 
                                    fg="#D72411", bg="#27E4F5", font="TkHeadingFont 13 bold")
        greet_msg.place(relx=0.03, rely=0.03, anchor='w')
        # Clickable text 'Go Back' set up
        def go_back():
            master.wm_deiconify()
            self.destroy()
        back_press = tk.Message(self, text="Go Back<--", fg="black", font="Helvetica 12 bold underline", bg="yellow")
        back_press.place(relx=0.9, rely=0.03, anchor="e")
        back_press.bind("<Button-1>", lambda e:go_back())
        # Label for showing the number of current enrolment
        self.enrol_status = tk.Label(self)
        self.enrol_status.place(relx=0.5, rely=0.2, anchor='center')
        
        # Button for selecting courses
        self.select_btn = tk.Button(self, text="Course Enrol", command=self.enrol)
        self.select_btn.place(relx=0.4, rely=0.3, anchor='center')
        
        # Button for deleting courses
        self.delete_btn = tk.Button(self, text="Course Delete", command=self.delete)
        self.delete_btn.place(relx=0.6, rely=0.3, anchor='center')
        
        # ListBox that contains all enrolled subjects' IDs
        self.course_box = tk.Listbox(self)
        # Place the ListBox into the frame
        self.course_box.place(relx=0.5, rely=0.5, anchor='center')
        
        # Add image
        enrol_1_img = Image.open("./GUI/Photos/enrol_1.jpeg").resize((150, 150))
        tk_enrol1_img = ImageTk.PhotoImage(enrol_1_img)
        enrol1_imglbl = tk.Label(self, image=tk_enrol1_img, bg="#27E4F5")
        enrol1_imglbl.image = tk_enrol1_img
        enrol1_imglbl.place(relx=0.8, rely=0.5, anchor="center")
        
        # Add another image
        enrol_2_img = Image.open("./GUI/Photos/enrol_2.jpeg").resize((150, 150))
        tk_enrol2_img = ImageTk.PhotoImage(enrol_2_img)
        enrol2_imglbl = tk.Label(self, image=tk_enrol2_img, bg="#27E4F5")
        enrol2_imglbl.image = tk_enrol2_img
        enrol2_imglbl.place(relx=0.2, rely=0.5, anchor="center")
        
        # Add another image
        enrol_3_img = Image.open("./GUI/Photos/enrol_3.png").resize((230, 150))
        tk_enrol3_img = ImageTk.PhotoImage(enrol_3_img)
        enrol3_imglbl = tk.Label(self, image=tk_enrol3_img, bg="#27E4F5")
        enrol3_imglbl.image = tk_enrol3_img
        enrol3_imglbl.place(relx=0.5, rely=0.85, anchor="center")
        
        # UI initialize
        self.refresh_ui()
    
    def refresh_ui(self):
        """Refresh the enrolled subject (not confirmed) Listbox and the enroll status label"""
        # Empty the Listbox
        self.course_box.delete(0, tk.END)
        
        # Case: when there is no enrolment, then simply set the enrol status message and return
        if len(self.current_courses) == 0:
            self.enrol_status.config(text=f"You have enrolled 0 out of 4 courses.",
                                     fg="green3", bg="#FBFF0E", font="Helvetica 25 bold")
            return
        # Add the ids of currently enrolled courses of the current login student into the Listbox
        for i, c in enumerate(self.current_courses):
            box_text = f"[{i+1}] Enrolled Course: {c.getSubjectID()}"
            self.course_box.insert(tk.END, box_text)
        
        # Update the enrol status label
        total_enrol = len(self.current_courses)
        if total_enrol <= 4:
            self.enrol_status.config(text=f"You have enrolled {total_enrol} out of 4 courses.",
                                     fg="green3", bg="#FBFF0E", font="Helvetica 25 bold")
    
    def enrol(self):
        """Handle the course enrol event."""
        try:
            new_course = self.try_enrol()
        except EnrolmentExceedLimitException as e:
            ExceptionWindow(self, str(e))
        else:
            self.current_courses = self.manager.viewEnrolmentList(self.user_id)
            # Reflect the enrol status change
            self.refresh_ui()
            # Successful enrolment message
            mb.showinfo("Success", f"Course {new_course.getSubjectID()} is enrolled!")
    
    def try_enrol(self):
        """Detect the enrolment limit exceed exception during the course enrolling process."""
        sub = self.manager.enrolSubject(self.user_id)
        if not sub:
            raise EnrolmentExceedLimitException()
        return sub
    
    def delete(self):
        """Handle the course delete event."""
        try:
            _, selected = self.try_delete()
        except CourseDeletionException as e:
            ExceptionWindow(self, str(e))
        else:
            self.current_courses = self.manager.viewEnrolmentList(self.user_id)
            self.refresh_ui()
            mb.showinfo("Success", f"Successfully deleted subject with ID: {selected.getSubjectID()}!")
    
    def try_delete(self):
        """Detect the course delete exception during the enrolled course deletion process."""
        # Get a currently selected course from enrolment Listbox
        enrol_size = self.course_box.size()
        # Case 1: enrolment Listbox is empty
        if enrol_size == 0:
            raise CourseDeletionException("Course Deletion Error: Empty enrolment list!")
        select_idx = self.course_box.curselection()
        # Case 2: course is not selected before deletion
        if not select_idx:
            raise CourseDeletionException("Course Deletion Error: No course is selected to delete! Please select a course in enrolment list!")
        selected = self.current_courses[select_idx[0]]
        deleted = self.manager.removeSubject(self.user_id, selected.getSubjectID())
        # Case 3: deleted course does not exists. 
        if not deleted:
            raise CourseDeletionException()
        return deleted, selected

        
        
        