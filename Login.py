import tkinter as tk  # Importing TKinter
import MyDatabase # Importing the file MyDatabase (the database file)
import BackToMain # Importing the BackToMain file

def login():
    # Window
    window = tk.Tk()
    window.resizable(width = False, height = False) # Making the Tkinter window not have the ability to be scaled
    window.geometry("280x170+750+350") # Changing the size of the window
    window.title("Login") # Making the title of the window Login

    row_index = 0

    # Window title
    title_label = tk.Label(window, text = "Please enter your details here:", font = "Verdana 12 underline")
    title_label.grid(row = row_index, column = 0, columnspan = 2, padx = 10, pady = 10)

    row_index += 1

    # Username section
    username_label = tk.Label(window, text = "Username:", font = "Verdana 9")
    username_label.grid(row = row_index, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "W")
    username_entry = tk.Entry(window, font = "Verdana 9")
    username_entry.grid(row = row_index, column = 1, padx = 10, pady = 10)

    row_index += 1

    # Password section
    password_label = tk.Label(window, text = "Password:", font = "Verdana 9")
    password_label.grid(row = row_index, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "W")
    password_entry = tk.Entry(window, show = "*", font = "Verdana 9")
    password_entry.grid(row = row_index, column = 1, padx = 10, pady = 10)

    row_index += 1

    # Enter button
    enter_button = tk.Button(window, text = "Enter", height = 1, width = 7, font = "Verdana 9", command = lambda: MyDatabase.CheckLogin(username_entry.get(), password_entry.get(), window))
    enter_button.grid(row = row_index, column = 1, columnspan = 1, padx = 10, pady = 10, sticky = "W")

    # Exit button
    exit_button = tk.Button(window, text = "Quit", height = 1, width = 7, font = "Verdana 9", command = lambda: window.destroy())
    exit_button.grid(row = row_index, column = 0, columnspan = 1, padx = 10, pady = 10, sticky = "W")

    tk.mainloop()

def UpdateLogin(old_window):
    old_window.destroy()

    # Window
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("340x170+750+350")
    window.title("Validation")

    row_index = 0

    # Window title
    title_label = tk.Label(window, text="Please enter your current details here:", font="Verdana 12 underline")
    title_label.grid(row=row_index, column=0, columnspan=4, padx=10, pady=10)

    row_index += 1

    # Username section
    username_label = tk.Label(window, text="Username:", font="Verdana 9")
    username_label.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    username_entry = tk.Entry(window, font="Verdana 9")
    username_entry.place(x=90, y=56, width=240)

    row_index += 1

    # Password section
    password_label = tk.Label(window, text="Password:", font="Verdana 9")
    password_label.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    password_entry = tk.Entry(window, show="*", font="Verdana 9")
    password_entry.place(x = 90, y = 96, width=240)

    row_index += 1

    # Enter button
    enter_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: MyDatabase.CheckLoginUpdate(username_entry.get(), password_entry.get(), window))
    enter_button.grid(row=row_index, column=3, columnspan=1, padx=15, pady=10, sticky="E")

    # Back button
    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: BackToMain.BackToMain(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=10, sticky="W")

    tk.mainloop()

def UpdateMenu(old_window):
    old_window.destroy()


    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("250x180+750+350")
    window.title("Update")

    row_index = 0

    title_label = tk.Label(window, text="Please select:", font="Verdana 12 underline")
    title_label.grid(row=row_index, column=0, columnspan=4, padx=10, pady=10, sticky="W")

    row_index += 1

    # Username section
    username_label = tk.Label(window, text="Username:", font="Verdana 9")
    username_label.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    username_button = tk.Button(window, text = "Update Username", height = 1, width = 15, font = "Verdana 9", command = lambda: UpdateUsername(window))
    username_button.grid(row=row_index, column=2, columnspan=1, padx=10, pady=10, sticky="E")

    row_index += 1

    # Password section
    password_label = tk.Label(window, text="Password:", font="Verdana 9")
    password_label.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    password_button = tk.Button(window, text="Update Password", height=1, width=15, font="Verdana 9", command=lambda: UpdatePassword(window))
    password_button.grid(row=row_index, column=2, columnspan=1, padx=10, pady=10, sticky="E")

    row_index += 1

    back_button = tk.Button(window, text = "Back", height = 1, width = 7, font = "Verdana 9", command = lambda: BackToMain.BackToMain(window))
    back_button.grid(row=row_index, column = 0, columnspan = 1, padx=10, pady=10)

def UpdatePassword(old_window):
    old_window.destroy()
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("300x167+750+350")
    window.title("Update Password")

    row_index = 0

    title_label = tk.Label(window, text="Please input required information:", font="Verdana 12 underline")
    title_label.grid(row=row_index, column=0, columnspan=4, padx=10, pady=10)

    row_index += 1

    password_label1 = tk.Label(window, text="New Password:", font="Verdana 9")
    password_label1.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    password_entry1 = tk.Entry(window, show="*", font="Verdana 9")
    password_entry1.place(x=115, y=56, width=175)

    row_index += 1

    password_label2 = tk.Label(window, text="New Password:", font="Verdana 9")
    password_label2.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    password_entry2 = tk.Entry(window, show="*", font="Verdana 9")
    password_entry2.place(x=115, y=97, width=175)

    row_index += 1

    enter_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: ActualUpdatePassword(password_entry1.get(), password_entry2.get(), window))
    enter_button.grid(row=row_index, column=3, columnspan=1, padx=15, pady=10, sticky="E")

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: UpdateMenu(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=10, sticky="W")

    def ActualUpdatePassword(Password1, Password2, old_window):
        if Password1 == Password2:
            if MyDatabase.VerifyPassword(Password1) == True:
                MyDatabase.UpdatePassword(Password1)
                UpdateMenu(old_window)

    tk.mainloop()



def UpdateUsername(old_window):
    old_window.destroy()

    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("300x170+750+350")
    window.title("Update Username")

    row_index = 0

    title_label = tk.Label(window, text="Please input required information:", font="Verdana 12 underline")
    title_label.grid(row=row_index, column=0, columnspan=4, padx=10, pady=10)

    row_index += 1

    username_label1 = tk.Label(window, text="New Username:", font="Verdana 9")
    username_label1.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    username_entry1 = tk.Entry(window, font="Verdana 9")
    username_entry1.place(x=115, y=56, width=175)

    row_index += 1

    username_label2 = tk.Label(window, text="Confirm Name:", font="Verdana 9")
    username_label2.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="W")
    username_entry2 = tk.Entry(window, font="Verdana 9")
    username_entry2.place(x=115, y=97, width=175)

    row_index += 1

    enter_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: ActualUpdateUsername(username_entry1.get(), username_entry2.get(), window))
    enter_button.grid(row=row_index, column=3, columnspan=1, padx=15, pady=10, sticky="E")

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: UpdateMenu(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=10, sticky="W")

    def ActualUpdateUsername(Username1, Username2, old_window):
        if Username1 == Username2:
            MyDatabase.UpdateUsername(Username1)
            UpdateMenu(old_window)

    tk.mainloop()