import main

def BackToMain(old_window):
    old_window.destroy()
    main.MainWindow()

def BackToStoreCreateUpdatePage(old_window):
    main.StoreCreateUpdatePage(old_window)