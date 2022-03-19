import tkinter as tk
import matplotlib.pyplot as plt
import MyDatabase
import BackToMain

def DisplayMenuClass(old_window):
    old_window.destroy()

    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("406x157+750+350")
    window.title("Display Menu")

    row_index = 0

    class_title = tk.Label(window, text="Display Menu", font="Verdana 12 underline")
    class_title.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    class_label = tk.Label(window, text="Please select the class:", font="Verdana 9")
    class_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    ClassList = MyDatabase.AllTables()

    variable = tk.StringVar(window)
    variable.set(ClassList[0])

    opt = tk.OptionMenu(window, variable, *ClassList)
    opt.config(width=32, font=('Verdana', 9))
    opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")

    enter_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: (DisplayMenu(variable.get()), window.destroy()))
    enter_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

    row_index += 1

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: BackToMain.BackToMain(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=14, pady=10, sticky="W")

def DisplayMenu(class_name):
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.geometry("472x261+750+350")
    window.title("Display Menu")

    row_index = 0

    title = tk.Label(window, text="Display Menu", font="Verdana 12 underline")
    title.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    label = tk.Label(window, text="To compare grades, select a different option, and enter", font="Verdana 9")
    label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    student_label = tk.Label(window, text="Please select the student to display their grades:", font="Verdana 9")
    student_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    StudentList = MyDatabase.AllStudents(class_name)
    WorkList = MyDatabase.AllWork(class_name)

    student_variable = tk.StringVar(window)
    student_variable.set(StudentList[0])

    student_opt = tk.OptionMenu(window, student_variable, *StudentList)
    student_opt.config(width=40, font=('Verdana', 9))
    student_opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")

    student_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: DisplayStudentGrades(class_name, student_variable.get(), WorkList, MyDatabase.GetGrades(class_name, student_variable.get(), "")))
    student_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

    row_index += 1

    work_label = tk.Label(window, text="Please select the work to display all students grades:", font="Verdana 9")
    work_label.grid(row=row_index, column=0, columnspan=1, padx=10, pady=5, sticky="W")

    row_index += 1

    work_variable = tk.StringVar(window)
    work_variable.set(WorkList[0])

    work_opt = tk.OptionMenu(window, work_variable, *WorkList)
    work_opt.config(width=40, font=('Verdana', 9))
    work_opt.grid(row=row_index, column=0, columnspan=1, padx=14, pady=5, sticky="W")

    work_button = tk.Button(window, text="Enter", height=1, width=7, font="Verdana 9", command=lambda: DisplayWorkGrades(class_name, work_variable.get(), StudentList, MyDatabase.GetWorkGrades(class_name, work_variable.get())))
    work_button.grid(row=row_index, column=1, columnspan=1, padx=0, pady=10, sticky="W")

    row_index += 1

    back_button = tk.Button(window, text="Back", height=1, width=7, font="Verdana 9", command=lambda: DisplayMenuClass(window))
    back_button.grid(row=row_index, column=0, columnspan=1, padx=14, pady=10, sticky="W")

def DisplayStudentGrades(class_name, student, work, grades):
    if student != "Please select the student":
        class_name = class_name[2:len(class_name) - 3]
        work = work[1:]

        plt.figure(class_name + " Students")
        plt.plot(work, grades, label=student) # Makes a graph plot, with x axis of being added as a list called work, and y being a list called grades

        plt.xlabel("Name of Work")
        plt.ylabel('Score (%)')
        plt.title("Student Grades for " + class_name)

        plt.legend()
        plt.show()

def DisplayWorkGrades(class_name, work, students, grades):
    if work != "Please select the work":
        class_name = class_name[2:len(class_name) - 3]
        students = students[1:]

        plt.figure(class_name + " Work")
        plt.plot(students, grades, label=work)

        plt.xlabel("Name of Students")
        plt.ylabel('Score (%)')
        plt.title("Work Grades for " + class_name)

        plt.legend()
        plt.show()