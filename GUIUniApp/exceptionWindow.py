import tkinter as tk

from PIL import Image, ImageTk

class ExceptionWindow(tk.Toplevel):
    def __init__(self, master:tk.Toplevel, error_msg:str):
        super().__init__(master=master)
        self.geometry("350x200")
        self.title("GUIUniApp - Error Occured")
        self.configure(bg="white")
        self.resizable(False, False)
        # Record the reference to the master window
        self.master_win = master
        
        # Error box frame set up
        error_box = tk.LabelFrame(self, text="Oops! You Got an Error!!!", 
                                  fg="#F52727", bg="white", font="Helvetice 15 bold")
        error_box.place(rely=0.5, relx=0.5, anchor='center')
        # Error image set up
        error_img = Image.open("./GUIUniApp/Photos/error_sign.png").resize((100, 100))
        self.tk_student_img = ImageTk.PhotoImage(error_img)
        error_imglbl = tk.Label(error_box, image=self.tk_student_img, bg="white")
        error_imglbl.image = self.tk_student_img 
        error_imglbl.pack(side=tk.LEFT, padx=(0, 15))
        # Error message set up
        error_message = tk.Message(error_box, text=error_msg, 
                                   fg="black", font="Helvetica 12 bold", bg="white", justify='left')
        error_message.pack(pady=10, padx=10, side=tk.LEFT)
        
        # Bind the close event with the "X" button (close the window) on the top
        self.protocol("WM_DELETE_WINDOW", self.close)
        # Make sure this window will always appear 
        # in front of the main window.
        self.transient(master)
        # Make sure the main window cannot be used 
        # when this window is popped out
        self.grab_set()
        # Stay focus on this window when encontering error
        self.focus_force()
        # Not whole mainloop longer executing until the user 
        # close this window
        self.wait_window(self)
    
    def close(self): 
        """Make sure we can click the entry box after we have closed exception window."""
        # Release the grab for exception window
        try:
            self.grab_release()
        except tk.TclError:
            # If grab already released, then ignore it
            pass 
        
        # Put the focus back to the master window
        if self.master_win.winfo_exists():
            self.master_win.focus_force()
        
        # Destroy the current exception window
        self.destroy()    
        
           
        
        