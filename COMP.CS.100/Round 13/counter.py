"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *



class Counter:
    def __init__(self):

        self.__current_count = 0

        self.__main_window = Tk()
        self.__current_value_label = Label(self.__main_window, text=self.__current_count)
        self.__current_value_label.grid(sticky=N)

        self.__reset_button = Button(self.__main_window, text="Reset", command=self.reset)
        self.__reset_button.grid(row=1, column=0)

        self.__increase_button = Button(self.__main_window, text="Increase", command=self.increase)
        self.__increase_button.grid(row=1, column=1)

        self.__decrease_button = Button(self.__main_window, text="Decrease", command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.lopeta)
        self.__quit_button.grid(row=1, column=3)




        self.__main_window.mainloop()

    def lopeta(self):
        self.__main_window.destroy()

    def reset(self):

        self.__current_count = 0

        self.__current_value_label.configure(text=self.__current_count)

    def increase(self):

        self.__current_count = self.__current_count + 1

        self.__current_value_label.configure(text=self.__current_count)

    def decrease(self):

        self.__current_count = self.__current_count - 1

        self.__current_value_label.configure(text=self.__current_count)

def main():

    Counter()


if __name__ == "__main__":
    main()


