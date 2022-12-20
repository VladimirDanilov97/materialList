import tkinter as tk

class mainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Нормы расхода материалов')
        

if __name__ == '__main__':
    main = mainWindow()
    main.mainloop()