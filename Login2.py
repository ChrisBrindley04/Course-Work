import main
import Login

def AllowAccess(access):
    if access == True:
        main.MainWindow()

def AllowUpdate(access, old_window):
    if access == True:
        Login.UpdateMenu(old_window)
