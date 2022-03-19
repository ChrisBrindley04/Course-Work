import tkinter as tk
import MyDatabase
import BackToMain

def Create(old_window):
    old_window.destroy()

    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("410x387+750+350")
    window.title("Create Page")

    row_index = 0

    class_title = tk.Label(window, text="Create Features", font="Verdana 12 underline")
    class_title.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky = "W")

    row_index += 1

    class_label = tk.Label(window, text="Type the name of the class you want to create:", font="Verdana 9")
    class_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    class_entry = tk.Entry(window,width=37, font="Verdana 9")
    class_entry.grid(row=row_index, column=0, padx=14, pady=5, sticky="W")

    class_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: MyDatabase.CreateClass(class_entry.get(), class_entry))
    class_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

    row_index += 1

    student_label = tk.Label(window, text="Type the name of the student you want to add:", font="Verdana 9")
    student_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    ClassList = MyDatabase.AllTables()

    # Drop down option list \/ \/ \/
    variable = tk.StringVar(window)
    variable.set(ClassList[0])

    opt = tk.OptionMenu(window, variable, *ClassList)
    opt.config(width=32, font=('Verdana', 9))
    opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")
    # Drop down option list /\ /\ /\

    row_index += 1

    student_entry = tk.Entry(window, width = 37, font="Verdana 9")
    student_entry.grid(row=row_index, column=0, padx=14, pady=5, sticky="W")

    student_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: MyDatabase.AddStudent(student_entry.get(), variable.get(), student_entry))
    student_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

    row_index += 1

    work_label = tk.Label(window, text="Type the name of the work you want to add:", font="Verdana 9")
    work_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    Work_ClassList = MyDatabase.AllTables()

    work_variable = tk.StringVar(window)
    work_variable.set(ClassList[0])

    work_opt = tk.OptionMenu(window, work_variable, *Work_ClassList)
    work_opt.config(width=32, font=('Verdana', 9))
    work_opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")

    row_index += 1

    work_entry = tk.Entry(window, width = 37, font="Verdana 9")
    work_entry.grid(row=row_index, column=0, padx=14, pady=5, sticky="W")

    student_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: MyDatabase.AddWork(work_entry.get(), work_variable.get(), work_entry))
    student_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

    row_index += 1

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9",command=lambda: BackToMain.BackToStoreCreateUpdatePage(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=14, pady=10, sticky="W")

    refresh_button = tk.Button(window, text="Refresh", height=1, width=7, font="Verdana 9", command=lambda: Create(window))
    refresh_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="E")

    window.mainloop()

def Store():
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("410x154+750+350")
    window.title("Store Page")

    row_index = 0

    store_title = tk.Label(window, text="Store Menu", font="Verdana 12 underline")
    store_title.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    store_label = tk.Label(window, text="Please select the name of the student's class:", font="Verdana 9")
    store_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    ClassList = MyDatabase.AllTables()

    # Drop down option list \/ \/ \/
    variable = tk.StringVar(window)
    variable.set(ClassList[0])

    opt = tk.OptionMenu(window, variable, *ClassList)
    opt.config(width=32, font=('Verdana', 9))
    opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")
    # Drop down option list /\ /\ /\

    store_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: InsertValues(variable.get(), window))
    store_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

    row_index += 1

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: BackToMain.BackToStoreCreateUpdatePage(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=14, pady=10, sticky="W")

def InsertValues(class_name, old_window):
    if class_name != "Please select the class":
        old_window.destroy()
        window = tk.Tk()
        window.resizable(width=False, height=False)
        window.geometry("394x250+750+350")
        window.title("Store Page")

        row_index = 0

        store_title = tk.Label(window, text="Store Menu", font="Verdana 12 underline")
        store_title.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        row_index += 1

        student_label = tk.Label(window, text="Please select the name of the student:", font="Verdana 9")
        student_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        row_index += 1

        StudentList = MyDatabase.AllStudents(class_name)

        student_variable = tk.StringVar(window)
        student_variable.set(StudentList[0])

        student_opt = tk.OptionMenu(window, student_variable, *StudentList)
        student_opt.config(width=40, font=('Verdana', 9))
        student_opt.grid(row=row_index, column=0, columnspan=2, padx=14, pady=5, sticky="W")

        row_index += 1

        work_label = tk.Label(window, text="Please select the name of the work:", font="Verdana 9")
        work_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        row_index += 1

        WorkList = MyDatabase.AllWork(class_name)

        work_variable = tk.StringVar(window)
        work_variable.set(WorkList[0])

        work_opt = tk.OptionMenu(window, work_variable, *WorkList)
        work_opt.config(width=40, font=('Verdana', 9))
        work_opt.grid(row=row_index, column=0, columnspan=2, padx=14, pady=5, sticky="W")

        row_index += 1

        score_label = tk.Label(window, text="Please type the integer percentage (e.g. 72):", font="Verdana 9")
        score_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

        score_entry = tk.Entry(window, width=5, font="Verdana 9")
        score_entry.grid(row=row_index, column=1, padx=0, pady=5, sticky="W")

        percent_sign = tk.Label(window, text="%", font="Verdana 9")
        percent_sign.grid(row=row_index, column=1, columnspan=1, padx=10, pady=5, sticky="E")

        row_index += 1

        enter_button = tk.Button(window, text="Enter", height=1, width=6, font="Verdana 9", command=lambda: StoreVerify(class_name, student_variable.get(),work_variable.get(), score_entry.get(), score_entry))
        enter_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

        back_button = tk.Button(window, text="Back", height=1, width=6, font="Verdana 9", command=lambda: (Store(), window.destroy()))
        back_button.grid(row=row_index, column=0, columnspan=1, padx=14, pady=10, sticky="W")

def StoreVerify(class_name, student, work, score, entry_box):
    Valid = 0
    ValidScoreCharacters = 0
    if len(score) > 0:
        if score.isdigit() == True:
            if len(str(score)) > 0:
                for i in range(len(score)):
                    if ord(score[i]) < 58 and ord(score[i]) > 47:
                        ValidScoreCharacters += 1
                if ValidScoreCharacters == len(str(score)):
                    Valid += 1

            if int(score) >= 0 and int(score) <= 100:
                Valid += 1

            if work != "Please select the work":
                Valid += 1

            if student != "Please select the student":
                Valid += 1

            if Valid == 4:
                MyDatabase.AddGrade(class_name, student, work, score)
                entry_box.delete(0, len(str(score)))