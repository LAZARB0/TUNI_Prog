"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry()

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry()

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="Calculate",background="black", foreground="red",
                                         command= self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text="")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Stop", command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value.grid()
        self.__height_value.grid()
        self.__calculate_button.grid()
        self.__stop_button.grid()
        self.__result_text.grid()
        self.__explanation_text.grid()

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        try:
            height = float(self.__height_value.get()) * 0.01
            weight = float(self.__weight_value.get())

            if height > 0 and weight > 0:

                height_index = height * height

                bmi = weight / float(height_index)

                if bmi < 18.5:
                    self.__explanation_text.configure(text="You are underweight.")
                elif bmi > 25.0:
                    self.__explanation_text.configure(text="You are overweight.")
                else:
                    self.__explanation_text.configure(text="Your weight is normal.")

                bmi = f"{bmi:.2f}"


                self.__result_text.configure(text=f"{bmi}")


            else:
                self.__explanation_text.configure(text="Error: height and weight must be positive.")
                self.reset_fields()

        except ValueError:
            self.__explanation_text.configure(text=("Error: height and weight must be numbers."))
            self.reset_fields()
            pass

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__weight_value.delete(0, END)
        self.__height_value.delete(0, END)
        self.__result_text.configure(text="")

        pass

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
