import tkinter as tk
import loginWindow

def displayGUI() -> None:
    loginWindow.LoginWindow()
    tk.mainloop()
    
if __name__ == "__main__":
    displayGUI()