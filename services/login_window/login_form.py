import sqlite3
from tkinter import *
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk

# Konekcija na bazu podataka
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Kreiranje tablice
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT UNIQUE, password TEXT)''')

# Spremanje korisnika
def save_user(username, password):
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

def open_main_window(username):
    global login_window, main_frame
    login_window.destroy()  # Zatvaranje login prozora

    # Kreiranje glavnog prozora
    main_window = Tk()
    main_window.title("Py Flora App MV")
    main_window.geometry('700x700')
    main_window.config(bg="#48483D")  # Postavljanje boje pozadine na plavu

    # Dodavanje widgeta u novi prozor
    main_frame = Frame(main_window, bg="#48483D", highlightthickness=0)
    main_frame.place(relx=0.5, rely=0.1, anchor=N)

    # Prikazivanje imena korisnika u glavnom labelu
    main_label = Label(main_frame, text=f'Dobrodošli {username}', font=('Vedrana', 20))
    main_label.pack()
    
    # Kreiraj Label widget za prikaz slike
    image_label = Label(main_frame, bg="#48483D")
    image_label.pack()

    # Padajući izbornici
    option_label1 = Label(main_frame, text='Tegla 1:', bg='#48483D')
    option_label1.pack()
    option_menu1 = OptionMenu(main_frame, StringVar(), 'Ruza', 'Tulipan', 'Orhideja', 'Bosiljak', 'Ruzmarin', 'Persin', command=lambda cvijet: prikazi_sliku(cvijet, image_label))
    option_menu1.pack()

    option_label2 = Label(main_frame, text='Tegla 2:', bg='#48483D')
    option_label2.pack()
    option_menu2 = OptionMenu(main_frame, StringVar(), 'Ruza', 'Tulipan', 'Orhideja', 'Bosiljak', 'Ruzmarin', 'Persin', command=lambda cvijet: prikazi_sliku(cvijet, image_label))
    option_menu2.pack()

    option_label3 = Label(main_frame, text='Tegla 3:', bg='#48483D')
    option_label3.pack()
    option_menu3 = OptionMenu(main_frame, StringVar(), 'Ruza', 'Tulipan', 'Orhideja', 'Bosiljak', 'Ruzmarin', 'Persin', command=lambda cvijet: prikazi_sliku(cvijet, image_label))
    option_menu3.pack()

    option_label4 = Label(main_frame, text='Tegla 4:', bg='#48483D')
    option_label4.pack()
    option_menu4 = OptionMenu(main_frame, StringVar(), 'Ruza', 'Tulipan', 'Orhideja', 'Bosiljak', 'Ruzmarin', 'Persin', command=lambda cvijet: prikazi_sliku(cvijet, image_label))
    option_menu4.pack()

    # Pokretanje glavnog prozora
    main_window.mainloop()

# Funkcija za prikaz slike cvijeta
def prikazi_sliku(cvijet, image_label):
    # Provjeri koja opcija je odabrana
    if cvijet == "Ruza":
        # Učitaj sliku ruže
        image = Image.open("C:/py_code-learning/PY_Flora_zavrsni ispit/py_flora_zavrsni/services/login_window/images/ruza_app.png")
        # Prilagodi veličinu slike prema potrebi
        resized_image = image.resize((100, 100))  # Postavite željenu veličinu slike
        # Pretvori sliku u format pogodan za prikazivanje u Tkinteru
        photo = ImageTk.PhotoImage(resized_image)
        # Prikazi sliku u Label widgetu
        image_label.config(image=photo)
        image_label.image = photo  # Sačuvaj referencu na sliku kako se ne bi obrisala


def login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Provjera usernamea i passworda
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    if result:
        messagebox.showinfo(title='Uspjeh', message='Uspješno ste se ulogirali')
        open_main_window(username)  # Prijenos imena korisnika u funkciju otvaranja glavnog prozora
    else:
        messagebox.showinfo(title='Error', message='Unijeli ste krive podatke!')

# Kreiranje računa
def create_account():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Provjera postojanja korisnika
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        messagebox.showinfo(title='Error', message='Korisnik je već u bazi')
    else:
        save_user(username, password)
        messagebox.showinfo(title='Uspjeh', message='Račun je kreiran')

# Login prozor
login_window = Tk()
login_window.title("Login Form")
login_window.geometry('700x700')

bg_image = PhotoImage(file='services\login_window\images\imagebg.png')

bg_label = Label(login_window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
app_name_label = Label(login_window, text='Algebra PY-Flora MVID', font=('O_Helvetica-Bold', 25), bg="#48483D", highlightthickness=0)
app_name_label.pack()

# Login frame
login_frame = Frame(login_window, bg="#48483D", highlightthickness=0)
login_frame.place(relx=0.8, rely=0.6, anchor=NW)

# Username label
usernameLabel = Label(login_frame, text="Username:", bg='#48483D')
usernameLabel.pack()
usernameEntry = Entry(login_frame, bg="#48483D", highlightthickness=0)
usernameEntry.pack()

# Password label
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

# Kreiraj Frame widget za glavni prozor
main_frame = Frame(login_window, bg="#48483D", highlightthickness=0)


# Start the main loop
login_window.mainloop()

# Zatvaranje konekcije na bazu podataka
conn.close()
