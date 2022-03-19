import tkinter as tk
import MyDatabase
import Login
import Student
import Display

def MainWindow():
    # Window
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("406x223+750+350")
    window.title("Main Page")

    row_index = 0

    # Window title
    title_label = tk.Label(window, text="Main Page", font="Verdana 12 underline")
    title_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=10, sticky="W")

    row_index += 1

    students_label = tk.Label(window, text="Click here to open the menu of other features:", font="Verdana 9")
    students_label.grid(row=row_index, column=0, padx=10, pady=10, sticky="W")

    students_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command = lambda: StoreCreateUpdatePage(window))
    students_button.grid(row=row_index, column=1, columnspan=1, padx=1, pady=10, sticky="W")

    row_index += 1

    # Display
    display_label = tk.Label(window, text="Click here to open the menu of display features:", font="Verdana 9")
    display_label.grid(row=row_index, column=0, padx=10, pady=10, sticky="W")

    display_button = tk.Button(window, text="Display", height=1, width=7, font="Verdana 9", command = lambda: Display.DisplayMenuClass(window))
    display_button.grid(row=row_index, column=1, columnspan=1, padx=1, pady=10, sticky="W")

    row_index += 1

    # Update Login info
    update_label = tk.Label(window, text="Click here to update your login information:", font="Verdana 9")
    update_label.grid(row=row_index, column=0, padx=10, pady=10, sticky="W")

    update_button = tk.Button(window, text="Update", height=1, width=7, font="Verdana 9", command = lambda: Login.UpdateLogin(window))
    update_button.grid(row=row_index, column=1, columnspan=1, padx=1, pady=10, sticky="W")

    row_index += 1

    # Logout button
    logout_button = tk.Button(window, text="Logout", height=1, width=7, font="Verdana 9", command = lambda: Logout(window))
    logout_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=10, sticky="W")

    # Exit button
    exit_button = tk.Button(window, text="Quit", height=1, width=7, font="Verdana 9", command = lambda: (window.destroy(), Display.plt.close('all')))
    exit_button.grid(row=row_index, column=0, columnspan=1, padx=85, pady=10, sticky="W")

    tk.mainloop()

def Logout(old_window):
    Display.plt.close('all') # Closes all plots
    old_window.destroy()
    Login.login()

def StoreCreateUpdatePage(old_window):
    old_window.destroy()

    #Window
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("410x224+750+350")
    window.title("Store, Create, and Update")

    row_index = 0

    #Title
    title_label = tk.Label(window, text="Store, Create, and Update Data", font="Verdana 12 underline")
    title_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=10, sticky="W")

    row_index += 1

    create_label = tk.Label(window, text="Click here to open the menu of create features:", font="Verdana 9")
    create_label.grid(row=row_index, column=0, padx=10, pady=10, sticky="W")

    create_button = tk.Button(window, text="Create", height=1, width=7, font="Verdana 9", command = lambda: Student.Create(window))
    create_button.grid(row=row_index, column=1, columnspan=1, padx=1, pady=10, sticky="W")

    row_index += 1

    update_label = tk.Label(window, text="Click here to open the menu of update features:", font="Verdana 9")
    update_label.grid(row=row_index, column=0, padx=10, pady=10, sticky="W")

    update_button = tk.Button(window, text="Update", height=1, width=7, font="Verdana 9", command=lambda: UpdateMenu(window))
    update_button.grid(row=row_index, column=1, columnspan=1, padx=1, pady=10, sticky="W")

    row_index += 1
    store_label = tk.Label(window, text="Click here to open the menu of store features:", font="Verdana 9")
    store_label.grid(row=row_index, column=0, padx=10, pady=10, sticky="W")

    store_button = tk.Button(window, text="Store", height=1, width=7, font="Verdana 9", command = lambda: (Student.Store(), window.destroy()))
    store_button.grid(row=row_index, column=1, columnspan=1, padx=1, pady=10, sticky="W")

    row_index += 1

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command = lambda: (window.destroy(), MainWindow()))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=10, sticky="W")

    tk.mainloop()

def UpdateMenu(old_window):
    old_window.destroy()

    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("331x309+750+350")
    window.title("Update Menu")

    row_index = 0

    title_label = tk.Label(window, text="Update and Delete Menu", font="Verdana 12 underline")
    title_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    score_label = tk.Label(window, text="To update a score, please go to the store menu", font="Verdana 9")
    score_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

    row_index += 1

    delete_label = tk.Label(window, text="To delete, leave input boxes blank", font="Verdana 9")
    delete_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

    row_index += 1

    ClassList = MyDatabase.AllTables()

    variable = tk.StringVar(window)
    variable.set(ClassList[0])

    opt = tk.OptionMenu(window, variable, *ClassList)
    opt.config(width=33, font=('Verdana', 9))
    opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")

    row_index += 1

    class_label = tk.Label(window, text="Update the name of a class:", font="Verdana 9")
    class_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

    row_index += 1

    class_entry = tk.Entry(window, width=28, font="Verdana 9")
    class_entry.grid(row=row_index, column=0, padx=14, pady=5, sticky="W")

    class_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: ClassRefresh(variable.get(), class_entry.get(), window))
    class_button.grid(row=row_index, column=0, columnspan=1, padx=15, pady=5, sticky="E")

    row_index += 1

    student_label = tk.Label(window, text="Update the name of a student:", font="Verdana 9")
    student_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

    student_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: UpdateStudent(variable.get(), window))
    student_button.grid(row=row_index, column=0, columnspan=1, padx=15, pady=5, sticky="E")

    row_index += 1

    work_label = tk.Label(window, text="Update or delete a piece of work:", font="Verdana 9")
    work_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

    work_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: UpdateWork(variable.get(), window))
    work_button.grid(row=row_index, column=0, columnspan=1, padx=15, pady=5, sticky="E")

    row_index += 1

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: StoreCreateUpdatePage(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

def ClassRefresh(old_name, new_name, old_window):
    if old_name[2: len(old_name) - 3] != new_name:
        allow = 0
        for i in range(len(MyDatabase.AllTables())-1):
            if list(MyDatabase.AllTables()[i + 1])[0] != new_name:
                allow += 1
        if allow == len(MyDatabase.AllTables()) - 1:
            if MyDatabase.UpdateClass(old_name, new_name) == True:
                UpdateMenu(old_window)

def UpdateStudent(class_name, old_window):
    if class_name != "Please select the class":
        old_window.destroy()

        window = tk.Tk()
        window.resizable(width=False, height=False)
        window.geometry("254x202+750+350")
        window.title("Update Student")

        row_index = 0

        title_label = tk.Label(window, text="Update Student", font="Verdana 12 underline")
        title_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        row_index += 1

        delete_label = tk.Label(window, text="To delete, leave the input box blank", font="Verdana 9")
        delete_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

        row_index += 1

        student_label = tk.Label(window, text="Update the name of a student:", font="Verdana 9")
        student_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

        row_index += 1

        StudentList = MyDatabase.AllStudents(class_name)

        variable = tk.StringVar(window)
        variable.set(StudentList[0])

        opt = tk.OptionMenu(window, variable, *StudentList)
        opt.config(width=23, font=('Verdana', 9))
        opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")

        row_index += 1

        student_entry = tk.Entry(window, width=28, font="Verdana 9")
        student_entry.grid(row=row_index, column=0, padx=14, pady=5, sticky="W")

        row_index += 1

        back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: UpdateMenu(window))
        back_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        entry_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: StudentRefresh(class_name, variable.get(), student_entry.get(), window))
        entry_button.grid(row=row_index, column=0, columnspan=1, padx=12, pady=5, sticky="E")

def StudentRefresh(class_name, student, new_student, old_window):
    if student != "Please select the student":
        if len(new_student) == 0:
            MyDatabase.UpdateStudent(class_name, student, new_student)
            UpdateStudent(class_name, old_window)
        elif MyDatabase.StudentNameVerify(new_student) == True:
            if len(student) > 1 and len(student) < 31:
                if MyDatabase.UpdateStudent(class_name, student, new_student) == True:
                    UpdateStudent(class_name, old_window)

def UpdateWork(class_name, old_window):
    if class_name != "Please select the class":
        old_window.destroy()

        window = tk.Tk()
        window.resizable(width=False, height=False)
        window.geometry("254x202+750+350")
        window.title("Update Work")

        row_index = 0

        title_label = tk.Label(window, text="Update Work", font="Verdana 12 underline")
        title_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        row_index += 1

        delete_label = tk.Label(window, text="To delete, leave the input box blank", font="Verdana 9")
        delete_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

        row_index += 1

        work_label = tk.Label(window, text="Update a piece of work:", font="Verdana 9")
        work_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="W")

        row_index += 1

        WorkList = MyDatabase.AllWork(class_name)

        variable = tk.StringVar(window)
        variable.set(WorkList[0])

        opt = tk.OptionMenu(window, variable, *WorkList)
        opt.config(width=23, font=('Verdana', 9))
        opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")

        row_index += 1

        work_entry = tk.Entry(window, width=28, font="Verdana 9")
        work_entry.grid(row=row_index, column=0, padx=14, pady=5, sticky="W")

        row_index += 1

        back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: UpdateMenu(window))
        back_button.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        entry_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: WorkRefresh(class_name, variable.get(), work_entry.get(), window))
        entry_button.grid(row=row_index, column=0, columnspan=1, padx=12, pady=5, sticky="E")

def WorkRefresh(class_name, work, new_name, old_window):
    if work != "Please select the work":
        if len(new_name) != 0:
            if len(new_name) > 1 and len(new_name) < 31:
                if MyDatabase.WorkNameVerify(new_name) == True:
                    if MyDatabase.UpdateWork(class_name, work, new_name) != False:
                        MyDatabase.UpdateWork(class_name, work, new_name)

                        UpdateWork(class_name, old_window)
        elif MyDatabase.WorkNameVerify(new_name) == True:
            if MyDatabase.UpdateWork(class_name, work, "") == True:
                UpdateWork(class_name, old_window)

if __name__ == "__main__":
    Login.login()