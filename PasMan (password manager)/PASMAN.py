"""
COMP.CS.100
Creator: Lassi Cederlöf
Email: lassi.cederlof@tuni.fi
"""


from tkinter import *

class startpage:

    def __init__(self):


        self.__main_window = Tk()
        self.__main_window.title("PASMAN")
        self.__label_welcome = Label(self.__main_window, text="Welcome to PASMAN. "
                                    "The safest and user-friendliest password manager!",
                                     font=("Arial", 10))
        self.__label_welcome.pack()
        canvas = Canvas(self.__main_window, height=10, width=20)
        canvas.pack()



        self.__add_user_data = Button(self.__main_window, text="Add user data", font=("Arial", 10),
                               command=lambda: add_user_data(),
                                height=5, width=50)
        self.__add_user_data.pack()



        self.__remove_user_data = Button(self.__main_window, text="Remove user data", font=("Arial", 10),
                                      command=lambda: remove_user_data(),
                                      height=5, width=50)
        self.__remove_user_data.pack()



        self.__find_user_data = Button(self.__main_window, text="Find user data", font=("Arial", 10),
                                         command=lambda: find_user_data(),
                                         height=5, width=50)
        self.__find_user_data.pack()



        self.__quit = Button(self.__main_window, text="Quit", font=("Arial", 10),
                                       command=lambda: quit(),
                                       height=5, width=50)
        self.__quit.pack()



        self.__main_window.mainloop()


    def quit(self):
        self.__main_window.destroy()

class testi:

    def __init__(self):
        self.__main_window = Tk()
        self.__save_button = Button(self.__main_window, text="Save", height=2, width=10,
                                    command=lambda: self.save_input())
        self.__save_button.pack()

    def save_input(self):
        self.__main_window.destroy()

        # input1 = self.__input_text1.get("1.0", "end-1c")

        # input2 = self.__input_text2.get("1.0", "end-1c")

        # input3 = self.__input_text3.get("1.0", "end-1c")
        # encryption = row_encryption(input3, 0)

        # credentials = [input1, input2, encryption]

        # append_file("passwords.txt", credentials)

class add_user_data:



    def __init__(self):

        self.__main_window = Tk()
        self.__main_window.title("Add user data")

        self.__label1 = Label(self.__main_window, text="Here you can save and encrypt your login credentials",
                                                    font=("Arial", 10))
        self.__label1.pack()

        canvas1 = Canvas(self.__main_window, height=10, width=50)
        canvas1.pack()
        self.__label_service = Label(self.__main_window, text="Type in the service which"
                                                        " credentials you want to save.")
        self.__label_service.pack()
        canvas2 = Canvas(self.__main_window, height=5, width=50)
        canvas2.pack()


        self.__input_text1 = Text(self.__main_window, height=1, width=25)
        self.__input_text1.pack()

        canvas3 = Canvas(self.__main_window, height=10, width=50)
        canvas3.pack()
        self.__label_username = Label(self.__main_window, text="Type in your username/email")
        self.__label_username.pack()
        canvas4 = Canvas(self.__main_window, height=5, width=50)
        canvas4.pack()

        self.__input_text2 = Text(self.__main_window, height=1, width=25)
        self.__input_text2.pack()

        canvas5 = Canvas(self.__main_window, height=10, width=50)
        canvas5.pack()
        self.__label_password = Label(self.__main_window, text="Type in the password"
                                                              " you want to encrypt.")
        self.__label_password.pack()
        canvas6 = Canvas(self.__main_window, height=5, width=50)
        canvas6.pack()

        self.__input_text3 = Text(self.__main_window, height=1, width=25)
        self.__input_text3.pack()

        self.__save_button = Button(self.__main_window, text="Save", height=2, width=10,
                                    command=lambda: self.save_input())
        self.__save_button.pack()

        self.__main_window.mainloop()



    def save_input(self):
        self.__main_window.destroy()

        #input1 = self.__input_text1.get("1.0", "end-1c")

        #input2 = self.__input_text2.get("1.0", "end-1c")

        #input3 = self.__input_text3.get("1.0", "end-1c")
        #encryption = row_encryption(input3, 0)

        #credentials = [input1, input2, encryption]

        #append_file("passwords.txt", credentials)



class remove_user_data:

    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("Remove user data")
        canvas = Canvas(self.__main_window, height=800, width=500)
        canvas.pack()

        self.__main_window.mainloop()

class find_user_data:

    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("Find user data")
        canvas = Canvas(self.__main_window, height=800, width=500)
        canvas.pack()

        self.__main_window.mainloop()




def encrypt(text, index):

    """
    Encrypts its parameter using aencryption technology.

    :param text: str,  string to be encrypted
    :param index: int,  index that indicates what is needed
    to be done with the param <text>
    :return: str, <text> parameter encrypted
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z", "å", "ä", "ö", "0", "1", "2", "3",
                       "4", "5", "6", "7", "8", "9", "!", "?", "=", "%", "#"
                       "&"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "å", "ä", "ö", "0", "1", "2", "3", "4", "5",
                       "6", "7", "8", "9", "!", "?", "=", "%", "#", "&", "a",
                       "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m"]
    index = int(index)

    if index == 0:
        if text.lower() in regular_chars and text not in regular_chars:
            text = text.lower()
            luku = regular_chars.index(text) + 19
            if luku > len(encrypted_chars):
                luku = luku - len(encrypted_chars)
                salattu = encrypted_chars[luku]
                salattu = salattu.upper()
            else:
                salattu = encrypted_chars[luku]
                salattu = salattu.upper()
            return salattu
        if text in regular_chars:
            luku = regular_chars.index(text) + 19
            if luku > len(encrypted_chars):
                luku = luku - len(encrypted_chars)
                salattu = encrypted_chars[luku]
            else:
                salattu = encrypted_chars[luku]
            return salattu
        else:
            return text
    elif index == 1:
        if text.lower() in regular_chars and text not in regular_chars:
            text = text.lower()
            luku = regular_chars.index(text)
            salattu = encrypted_chars[luku]
            salattu = salattu.upper()
            return salattu
        if text in regular_chars:
            luku = regular_chars.index(text)
            salattu = encrypted_chars[luku]
            return salattu
        else:
            return text



def row_encryption(text, index):

    """
        Encrypts its parameter using a encryption technology.

        :param text: str,  string to be encrypted
        :param index: int,  index that indicates what is needed
        to be done with the param <text>
        :return: str, <text> parameter encrypted
        """
    index = int(index)
    lause = ""
    for luku in range(0, len(text)):
        merkki = text[luku]
        salattu = encrypt(merkki, index)
        lause += salattu

    return lause

def read_file(filename):


    passwords = {}

    try:
        file = open(filename, mode="r")

        for row in file:
            row = row.split(":")
            if row[0] in passwords:
                data = passwords[row[0]]
            else:
                data = {}

            if len(row) == 3:
                data[row[1]] = row[2]
                passwords[row[0]] = data


    except IOError:
        print("Error: the file could not be read.")
        return None

    return passwords

def append_file(filename, credentials):


    passwords = {}

    try:
        file = open(filename, mode="a")
        file.write('\n')
        file.write((f"{credentials[0]}:{credentials[1]}:{credentials[2]}"))

        file.close()


    except IOError:
        print("Error: the file could not be read.")
        return None

def main():

    gui = startpage()

if __name__ == "__main__":
    main()
