from tkinter import *
from tkinter import messagebox, Toplevel

def open_main_window():
    global login_window  # Declare login_window as global to access it inside the function
    login_window.destroy()  # Close the login window

    # Create the main window
    main_window = Tk()
    main_window.title("Py Flora App MV")
    main_window.geometry('700x700')

    # Add your desired widgets and functionality to the main window here

    # Start the main loop for the new window
    main_window.mainloop()
