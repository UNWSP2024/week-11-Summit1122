# Info Shower
# 11/15/24
# Luis Amador

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.my_button = tkinter.Button(self.main_window, text = 'Show Info',
                                        command = self.do_something)

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit',
                                          command = self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()
        tkinter.mainloop()


    def do_something(self):
        tkinter.messagebox.showinfo('Info', 'Name: Luis Amador\n'
                                                          'Address: 23582 Eidelweiss, Saint Francis')


if __name__ == "__main__":
    my_gui = MyGUI()