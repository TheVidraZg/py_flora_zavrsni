import sqlite3
from tkinter import *
from tkinter import messagebox, Toplevel


# Database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT UNIQUE, password TEXT)''')

# Function to save user details to the database
def save_user(username, password):
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

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


# Function to handle login
def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    

    # Check if username and password are correct
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    if result:
        messagebox.showinfo(title = 'Uspjeh', message = 'Uspjesno ste se ulogirali ')
        open_main_window()
    else:
        messagebox.showinfo(title = 'Error', message = 'Unijeli ste krive podatke!')

# Function to handle account creation
def create_account():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Check if username already exists
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        messagebox.showinfo(title = 'Error', message = 'Korisnik je vec u bazi ')
    else:
        save_user(username, password)
        messagebox.showinfo(title = 'Uspjeh', message = 'Racun je kreiran ')

# Create the main window
login_window = Tk()
login_window.title("Login Form")
login_window.geometry('700x700')

# Load the background image
bg_image = PhotoImage(file='services\login_window\images\imagebg.png')

# Create a Label to display the background image
bg_label = Label(login_window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
app_name_label= Label(login_window, text='Algebra PY-Flora MVID',font= ('O_Helvetica-Bold', 25),bg="#48483D", highlightthickness=0 )
app_name_label.pack()


# Create login frame
login_frame = Frame(login_window, bg="#48483D", highlightthickness=0)
login_frame.place(relx=0.8, rely=0.6, anchor=NW)

# Username label and entry
usernameLabel = Label(login_frame, text="Username:", bg='#48483D')
usernameLabel.pack()
usernameEntry = Entry(login_frame, bg="#48483D", highlightthickness=0)
usernameEntry.pack()

# Password label and entry
passwordLabel = Label(login_frame, text="Password:", bg='#48483D')
passwordLabel.pack()
passwordEntry = Entry(login_frame, show="*", bg="#48483D", highlightthickness=0)
passwordEntry.pack()

# Login button
loginButton = Button(login_frame, text="Login", command=login, bg='#48483D')
loginButton.pack()

# Create account button
createAccountButton = Button(login_frame, text="Create Account", command=create_account, bg='#48483D')
createAccountButton.pack()

# Start the main loop
login_window.mainloop()

# Close the database connection
conn.close()