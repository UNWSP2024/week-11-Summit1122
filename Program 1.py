# Favorite Saying
# Luis Amador
# 11/15/24


import tkinter


class MyGUI:
    def __init__(self):


        self.main_window = tkinter.Tk()

        self.main_window.title("My Favorite Saying")
        self.label1 = tkinter.Label(self.main_window, text="Ya like jazz?? - Bee",
                                    borderwidth= 1, relief="solid")
        self.label1.pack()
        
        tkinter.mainloop()


if __name__ == "__main__":
    my_gui = MyGUI()