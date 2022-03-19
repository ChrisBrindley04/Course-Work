import sqlite3
import Login2

def LoginDatabase():
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()

    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name = 'LOGIN' ''')

    if c.fetchone()[0] == 0: # Will have a value of 0 if there is no table, and 1 if there is a table
        exists = False
    else:
        exists = True

    # Creates the table LOGIN, if it doesn't exist
    conn.execute('''CREATE TABLE IF NOT EXISTS LOGIN
           (ID INT PRIMARY KEY NOT NULL,
            USERNAME TEXT NOT NULL,
            PASSWORD TEXT NOT NULL);''')

    if exists == False:
        LoginDefault() # Will set the default values for USERNAME and PASSWORD

    conn.close()

def LoginDefault():
    conn = sqlite3.connect("Database.db")

    cursor = conn.execute("SELECT ID, USERNAME, PASSWORD from LOGIN")

    for row in cursor:
        Username = row[1]
        Password = row[2]


    # Sets the values of USERNAME and PASSWORD to the default values
    conn.execute("INSERT INTO LOGIN (ID, USERNAME, PASSWORD) \
                VALUES (1, 'Username1', 'Password1')")

    conn.commit()
    conn.close()

def CheckLogin(InputedUsername, InputedPassword, window):
    conn = sqlite3.connect("Database.db")
    cursor = conn.execute("SELECT ID, USERNAME, PASSWORD from LOGIN")

    for row in cursor:
        Username = row[1]
        Password = row[2]

    if Username == InputedUsername and Password == InputedPassword:
        window.destroy()
        Login2.AllowAccess(True) # Opens the main window

    conn.close()

def CheckLoginUpdate(InputedUsername, InputedPassword, old_window):
    conn = sqlite3.connect("Database.db")
    cursor = conn.execute("SELECT ID, USERNAME, PASSWORD from LOGIN")

    for row in cursor:
        Username = row[1]
        Password = row[2]

    if Username == InputedUsername and Password == InputedPassword: # Checks the inputted info is the
        Login2.AllowUpdate(True, old_window)                        # same as the info stored in the database
    else:
        Login2.AllowUpdate(False, old_window)

    conn.close()

def UpdateUsername(InputedUsername):
    conn = sqlite3.connect("Database.db")

    # Updates the username in the table to the inputted name
    conn.execute("UPDATE LOGIN SET USERNAME = ? WHERE ID = ?", (InputedUsername, 1))

    conn.commit()
    conn.close()

def UpdatePassword(InputedPassword):
    conn = sqlite3.connect("Database.db")

    # Updates the password in the table to the inputted name
    conn.execute("UPDATE LOGIN SET PASSWORD = ? WHERE ID = ?", (InputedPassword, 1))

    conn.commit()
    conn.close()

def VerifyPassword(password):
    capital_letters = 0
    lower_case_letters = 0
    numbers = 0
    allow = True

    for i in range(len(password)):
        if ord(password[i]) > 64 and ord(password[i]) < 91: # Tests if the character is between A-Z
            capital_letters += 1
        elif ord(password[i]) > 96 and ord(password[i]) < 123: # Tests if the character is between a-z
            lower_case_letters += 1
        elif ord(password[i]) > 47 and ord(password[i]) < 58: # Tests if the character is a number
            numbers += 1
        elif ord(password[i]) == 32: # Tests if the character is a space
            allow = False

    if len(password) > 7 and len(password) < 31:
        if allow == True:
            if capital_letters > 0:
                if lower_case_letters > 0:
                    if numbers > 0:
                        return True

def CreateClass(name, entry_box):
    conn = sqlite3.connect("Database.db")

    if ClassNameVerify(name) == True: # Makes sure the name has no invalid characters
        if len(name) > 4 and len(name) < 31: # Makes sure the length is valid
            if name != "LOGIN": # Makes it so you can't create a table called LOGIN
                # Creates a table with the name that the user inputted
                conn.execute('''CREATE TABLE IF NOT EXISTS {}
                            (STUDENTNAME string NOT NULL)'''.format(name))
                if len(str(entry_box)) != 0:
                    entry_box.delete(0, len(str(name))) # Will remove all text from an entry box

    conn.commit()
    conn.close()

def ClassNameVerify(name): # Verifies that the name of a class trying to be added is valid
    allow = 0 # Sets the default value of allow to 0

    for i in range(len(str(name))):
        if ord(name[i]) > 64 and ord(name[i]) < 91: # Tests if the character is between A-Z
            allow += 1
        elif ord(name[i]) > 96 and ord(name[i]) < 123: # Tests if the character is between a-z
            allow += 1

    if allow == len(name): # Tests if every character is valid
        return True
    else:
        return False

def AllTables(): # Gets a list of all the classes
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

    ClassList = ["Please select the class"]
    TableList = cursor.fetchall()

    for i in range(len(TableList) - 1):
        ClassList.append(TableList[i + 1])

    return(ClassList)

    conn.commit()
    conn.close()

def AllWork(table): # Gets a list of all pieces of work in a given class
    table = table[2:len(table)-3]
    WorkList = ["Please select the work"]

    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM {}".format(table))

    for column in data.description:
        WorkList.append(column[0])

    WorkList.remove("STUDENTNAME")

    conn.commit()
    conn.close()

    return(WorkList)

def AllStudents(table): # Gets a list of all students in a given class
    table = table[2:len(table)-3]
    StudentList = ["Please select the student"]

    conn = sqlite3.connect("Database.db")
    cursor = conn.execute("SELECT STUDENTNAME FROM {}".format(table))

    for row in cursor:
        StudentList.append(row[0])

    return(StudentList)

    conn.commit()
    conn.close()

def AddStudent(name, table, entry_box): # Adds a student to a specific class
    if table != "Please select the class":
        if CheckStudent(table, name) == True:
            table = table[2:len(table) - 3]
            conn = sqlite3.connect("Database.db")

            if StudentNameVerify(name) == True:
                if len(name) > 1 and len(name) < 31:
                    conn.execute('''INSERT INTO {} (STUDENTNAME) VALUES (?)'''.format(table),(name,))

                if len(str(entry_box)) != 0:
                    entry_box.delete(0, len(str(name))) # Will remove all text from an entry box

            conn.commit()
            conn.close()

def StudentNameVerify(name):
    allow = 0 # Sets the default value of allow to 0

    for i in range(len(str(name))):
        if ord(name[i]) > 64 and ord(name[i]) < 91: # Tests if the character is between A-Z
            allow += 1
        elif ord(name[i]) > 96 and ord(name[i]) < 123: # Tests if the character is between a-z
            allow += 1
        elif ord(name[i]) == 32:
            allow += 1

    if allow == len(name): # Tests if every character is valid
        return True
    else:
        return False

def AddWork(name, table, entry_box): # Adds a piece of work to specific class
    if table != "Please select the class":
        if CheckWork(table, name) == True:
            table = table[2:len(table) - 3]

            conn = sqlite3.connect("Database.db")

            if WorkNameVerify(name) == True:
                if len(name) > 1 and len(name) < 31:
                        conn.execute('''ALTER TABLE {} ADD {} INT'''.format(table, name))

                        if len(str(entry_box)) != 0:
                            entry_box.delete(0, len(str(name))) # Will remove all text from an entry box

            conn.commit()
            conn.close()

def CheckWork(class_name, work):
    allow = 0
    for i in range(len(AllWork(class_name)) - 1):
        if AllWork(class_name)[i + 1] != work:
            allow += 1
    if allow == len(AllWork(class_name)) - 1:
        return True


def WorkNameVerify(name): # Verifies that the name of a piece of work being added is valid
    allow = 0 # Sets the default value of allow to 0

    for i in range(len(str(name))):
        if ord(name[i]) > 64 and ord(name[i]) < 91: # Tests if the character is between A-Z
            allow += 1
        elif ord(name[i]) > 96 and ord(name[i]) < 123: # Tests if the character is between a-z
            allow += 1
        elif ord(name[i]) < 58 and ord(name[i]) > 47: # Tests if the character is a number
            allow += 1

    if allow == len(name): # Tests if every character is valid
        return True
    else:
        return False

def AddGrade(table, student, work, score):
    table = table[2:len(table) - 3]

    conn = sqlite3.connect("Database.db")

    conn.execute('''UPDATE {tbl} SET {wrk} = ? WHERE STUDENTNAME = ?'''.format(tbl = table, wrk = work),(score, student))

    conn.commit()
    conn.close()

def GetGrades(table, student, ignore):
    if student == "Please select the student":
        return([])

    WorkList = AllWork(table)
    WorkList = WorkList[1:]

    if len(ignore) != 0:
        WorkList.remove(ignore)


    table = table[2:len(table) - 3]

    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()

    GradeList = []

    for i in range(len(WorkList)):
        cursor.execute('''SELECT {wrk} FROM {tbl} WHERE STUDENTNAME = ?'''.format(wrk = WorkList[i], tbl = table),(student,))
        GradeList.append(cursor.fetchall())
        if GradeList[i][0] == (None,):
            GradeList[i][0] = (0)

    for j in range(len(WorkList)):
        if GradeList[j][0] != 0:
            GradeList[j] = GradeList[j][0]

    Grades = []

    for k in range(len(WorkList)):
        Grades.append(GradeList[k][0])

    return(Grades)

    conn.commit()
    conn.close()

def GetWorkGrades(table, work):
    if work != "Please select the work":
        StudentList = AllStudents(table)
        StudentList = StudentList[1:]

        table = table[2:len(table) - 3]

        conn = sqlite3.connect("Database.db")
        cursor = conn.cursor()

        GradeList = []

        for i in range(len(StudentList)):
            cursor.execute('''SELECT {wrk} FROM {tbl} WHERE STUDENTNAME = ?'''.format(wrk=work, tbl=table), (StudentList[i],))
            GradeList.append(cursor.fetchall())
            if GradeList[i][0] == (None,):
                GradeList[i][0] = (0)

        for j in range(len(StudentList)):
            if GradeList[j][0] != 0:
                GradeList[j] = GradeList[j][0]

        Grades = []

        for k in range(len(StudentList)):
            Grades.append(GradeList[k][0])

        return(GradeList)

        conn.commit()
        conn.close()

def UpdateStudent(table, student, new_student): # Will edit or remove a student in database
    conn = sqlite3.connect("Database.db")

    if len(new_student) == 0:
        table = table[2:len(table) - 3]

        conn.execute('''DELETE FROM {} WHERE STUDENTNAME = ?'''.format(table), (student,))

        conn.commit()
        conn.close()

    elif CheckStudent(table, new_student) == True:
        table = table[2:len(table) - 3]
        conn.execute('''UPDATE {} SET STUDENTNAME = ? WHERE STUDENTNAME = ?'''.format(table),(new_student, student))

        conn.commit()
        conn.close()

        return True

def CheckStudent(class_name, student):
    allow = 0
    for i in range(len(AllStudents(class_name)) - 1):
        if AllStudents(class_name)[i + 1] != student:
            allow += 1
    if allow == len(AllStudents(class_name)) - 1:
        return True


def UpdateWork(table, work, new_name): # Will edit or remove a piece of work in database
    conn = sqlite3.connect("Database.db")

    if len(new_name) != 0:
        if CheckWork(table, new_name) == True:
            table = table[2:len(table) - 3]

            conn.execute("ALTER TABLE {} RENAME COLUMN {} TO {}".format(table, work, new_name))

            conn.commit()
            conn.close()
        else:
            return False

    elif len(new_name) == 0:
        FakeTable = "Fake" + table[2:len(table) - 3]

        CreateClass(FakeTable, "")

        WorkList = AllWork(table)
        WorkList = WorkList[1:]
        WorkList.remove(work)

        for i in range(len(WorkList)):
            AddWork(WorkList[i], "AA" + FakeTable + "AAA", "")

        StudentList = AllStudents(table)
        StudentList = StudentList[1:]

        for j in range(len(StudentList)):
            AddStudent(StudentList[j], "AA" + FakeTable + "AAA", "")

        for k in range(len(StudentList)):
            for l in range(len(WorkList)):
                GradeList = GetGrades(table, StudentList[k], work)
                AddGrade("AA" + FakeTable + "AAA", StudentList[k], WorkList[l], GradeList[l])

        conn.execute("DROP TABLE {}".format(table[2:len(table) - 3]))
        conn.execute("ALTER TABLE {oldtbl} RENAME TO {newtbl}".format(oldtbl = FakeTable, newtbl = table[2:len(table) - 3]))

        conn.commit()
        conn.close()

        return True

def UpdateClass(old_name, new_name): # Will edit or remove the name of a class
    if old_name != "Please select the class":
        old_name = old_name[2: len(old_name) - 3]

        if len(new_name) == 0:
            conn = sqlite3.connect("Database.db")
            conn.execute("DROP TABLE {}".format(old_name))
            conn.commit()
            conn.close()

            return True

        elif ClassNameVerify(new_name) == True:
            if len(new_name) > 4 and len(new_name) < 31:
                conn = sqlite3.connect("Database.db")
                conn.execute("ALTER TABLE {oldtbl} RENAME TO {newtbl}".format(oldtbl=old_name, newtbl=new_name))
                conn.commit()
                conn.close()

                return True

InfoCorrect = "False"
LoginDatabase()