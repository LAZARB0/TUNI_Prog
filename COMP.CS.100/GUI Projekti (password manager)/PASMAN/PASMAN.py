"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi

Salasanojen turvallinen säilytys, ylläpito sekä
hallinnointi ohjelma. Ohjelma käyttää graafista
käyttöliittymää perustuen tkinter kirjastoon.
Ohjelmassa käyttäjä lisää <add user data> ikkunaa
käyttäen tietonsa <passwords.txt> tidostoon.
Käyttäjä pystyy hallitsemaan tietojaan sekä
näyttämään niitä ohjelman muiden toimintojen avulla.

Ohjelma on tehty tähdäten kehittyneeseen versioon projektista
"""


from tkinter import *


class startpage:


    """
    This class defines the startpage window,
    that is ran when the program is ran.
    Starpage window works as the main manu of the
    program.
    """


    def __init__(self):


        self.__main_window = Tk()
        self.__main_window.title("PASMAN")
        self.__label_welcome = Label(self.__main_window, text="Welcome to PASMAN. "
                                    "The safest and user-friendliest password manager!",
                                     font=("Arial", 10))
        self.__label_welcome.pack()
        canvas = Canvas(self.__main_window, height=10, width=20)  # Canvasta käytetään tässä, sekä muissa ikkunoissa
        canvas.pack()                                             # muodostamaan välejä labeleiden yms välille.


        self.__add_user_data = Button(self.__main_window,
                                      text="Add user data", font=("Arial", 10),
                                      command= add_user_data,
                                      height=5, width=50)
        self.__add_user_data.pack()


        self.__remove_user_data = Button(self.__main_window,
                                      text="Remove user data", font=("Arial", 10),
                                      command= remove_user_data,
                                      height=5, width=50)
        self.__remove_user_data.pack()


        self.__config_user_data = Button(self.__main_window,
                                         text="Config user data", font=("Arial", 10),
                                         command=config_user_data,
                                         height=5, width=50)
        self.__config_user_data.pack()


        self.__find_user_data = Button(self.__main_window,
                                         text="Find user data", font=("Arial", 10),
                                         command= find_user_data,
                                         height=5, width=50)
        self.__find_user_data.pack()


        self.__quit = Button(self.__main_window,
                                       text="Quit", font=("Arial", 10),
                                       command=self.quit,
                                       height=5, width=50)
        self.__quit.pack()


        self.__main_window.mainloop()


    def quit(self):

        """
        Command attached to the quit button.
        destroys the startpage window when pressed.

        :return: None
        """

        self.__main_window.destroy()


class add_user_data:


    """
    This class defines the pop-up window for adding
    new login credentials to the save file. Window
    pop-ups when the <self.__add_user_data> button
    is pressed on the startpage.
    """


    def __init__(self):

        self.__main_window = Tk()
        self.__main_window.title("Add user data")

        self.__label1 = Label(self.__main_window, text="Here you can save and encrypt"
                                                       " your login credentials",
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

        canvas5 = Canvas(self.__main_window, height=5, width=50)
        canvas5.pack()

        self.__save_button = Button(self.__main_window, text="Save", font=("Arial", 10),
                                    command=self.save_input,
                                    height=2, width=5)
        self.__save_button.pack()

        canvas5 = Canvas(self.__main_window, height=10, width=50)
        canvas5.pack()
        self.__status = Label(self.__main_window, text=" ")
        self.__status.pack()
        canvas6 = Canvas(self.__main_window, height=10, width=50)
        canvas6.pack()

        self.__main_window.mainloop()

    def save_input(self):


        """
        Function made to save data given by the user
        on the different text input boxes. Function
        encrypts and saves the data to the <passwords.txt>
        file using the global <append_file> and <row_encryption>
        funtions.

        :return: None
        """


        try:
            input1 = self.__input_text1.get("1.0", "end-1c")

            input2 = self.__input_text2.get("1.0", "end-1c")

            input3 = self.__input_text3.get("1.0", "end-1c")

            for char in input1:
                if char == ":":
                    self.__input_text1.delete("1.0", "end-1c")
                    raise NameError
            for char in input2:
                if char == ":":
                    self.__input_text2.delete("1.0", "end-1c")
                    raise NameError
            for char in input3:
                if char == ":":
                    self.__input_text3.delete("1.0", "end-1c")
                    raise NameError

            encryption = row_encryption(input3, 0)      # Encryptataan salasana <row_encryption> funktiolla

            credentials = [input1, input2, encryption]


            if input1 != "" and input2 != "" and input3 != "":

                append_file("passwords.txt", credentials)

                self.__status.configure(text=f"Username: {input2} saved succesfully!")
                self.__input_text1.delete("1.0", "end-1c")
                self.__input_text2.delete("1.0", "end-1c")          # Tässä sekä muissa ikkunoissa, kun toiminto
                self.__input_text3.delete("1.0", "end-1c")          # suoritettu ilmoitetaan siitä käyttäjälle
                                                                    # ja tyhjennetään syötelaatikot
            else:
                self.__status.configure(text=f"You must fill in all the boxes!")
                return
        except NameError:
            self.__status.configure(text=f"Credentials can not include ':'")

class remove_user_data:


    """
    Class defined for the remove user data pop-up window
    window pop-ups when the <self.__remove_user_data> button
    is pressed on the startpage.
    """


    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("Add user data")


        self.__label1 = Label(self.__main_window, text="Here you can remove your"
                                                       " login credentials from the program",
                              font=("Arial", 10))
        self.__label1.pack()


        canvas1 = Canvas(self.__main_window, height=10, width=50)
        canvas1.pack()
        self.__label_service = Label(self.__main_window, text="Type in which service's "
         
                                                             " credentials you want to remove.")
        self.__label_service.pack()
        canvas2 = Canvas(self.__main_window, height=5, width=50)
        canvas2.pack()


        self.__input_text1 = Text(self.__main_window, height=1, width=25)
        self.__input_text1.pack()


        canvas3 = Canvas(self.__main_window, height=10, width=50)
        canvas3.pack()
        self.__label_username = Label(self.__main_window, text="Type in the username/email"
                     
                                                               " you want to remove.")
        self.__label_username.pack()
        canvas4 = Canvas(self.__main_window, height=5, width=50)
        canvas4.pack()


        self.__input_text2 = Text(self.__main_window, height=1, width=25)
        self.__input_text2.pack()
        canvas5 = Canvas(self.__main_window, height=5, width=50)
        canvas5.pack()


        self.__remove_button = Button(self.__main_window, text="Remove", font=("Arial", 10),
                                    command=self.remove_input,
                                    height=2, width=5)
        self.__remove_button.pack()


        canvas5 = Canvas(self.__main_window, height=10, width=50)
        canvas5.pack()
        self.__status = Label(self.__main_window, text=" ")
        self.__status.pack()
        canvas6 = Canvas(self.__main_window, height=10, width=50)
        canvas6.pack()


        self.__main_window.mainloop()

    def remove_input(self):


        """
        This function reads the <passwords.txt> file
        with <read_file> function, saves it to a variable,
        removes the data corresponding the user inputs from
        the variable, and then writes the file from a
        scratch with <write_file> function with the defined
        data variable.

        :return: None
        """


        input1 = self.__input_text1.get("1.0", "end-1c")

        input2 = self.__input_text2.get("1.0", "end-1c")

        file = read_file("passwords.txt")               # tietojen poistamista varten luetaan tiedostosta tiedot
                                                        # tallennetaan ne tietorakanteeseen ja muokataan tietorakennetta,
                                                        # jonka jälkeen taas kirjoitetaan tiedosto päivitetyillä tiedoilla.

        if input1 != "" and input2 != "" and input1 in file and input2 in file[input1]:

            if len(file[input1].keys()) == 1:
                file.pop(input1)
                write_file("passwords.txt", file)
                self.__status.configure(text=f"Username: {input2} removed succesfully!")
                self.__input_text1.delete("1.0", "end-1c")
                self.__input_text2.delete("1.0", "end-1c")

            else:
                user = file[input1]
                user.pop(input2)
                file[input1] = user

                write_file("passwords.txt", file)
                self.__status.configure(text=f"Username: {input2} removed succesfully!")
                self.__input_text1.delete("1.0", "end-1c")
                self.__input_text2.delete("1.0", "end-1c")

        else:
            self.__status.configure(text="Service or username/email not found!")

class config_user_data:


    """
    This class defines the pop-up window for updating
    login credentials in the save file. Window
    pop-ups when the <self.__config_user_data> button
    is pressed on the startpage.
    """


    def __init__(self):


        self.__main_window = Tk()
        self.__main_window.title("Config user data")


        self.__label1 = Label(self.__main_window, text="Here you can update your login credentials",
                              font=("Arial", 10))
        self.__label1.pack()


        canvas1 = Canvas(self.__main_window, height=10, width=50)
        canvas1.pack()
        self.__label_service = Label(self.__main_window, text="Type in which service's "
              
                                                              " credentials you want to update.")
        self.__label_service.pack()
        canvas2 = Canvas(self.__main_window, height=5, width=50)
        canvas2.pack()


        self.__input_text1 = Text(self.__main_window, height=1, width=25)
        self.__input_text1.pack()


        canvas3 = Canvas(self.__main_window, height=10, width=50)
        canvas3.pack()
        self.__label_username = Label(self.__main_window, text="Type in the username/email"
                                                               " you want to update.")
        self.__label_username.pack()


        canvas4 = Canvas(self.__main_window, height=5, width=50)
        canvas4.pack()
        self.__input_text2 = Text(self.__main_window, height=1, width=25)
        self.__input_text2.pack()


        canvas3 = Canvas(self.__main_window, height=10, width=50)
        canvas3.pack()
        self.__label_password = Label(self.__main_window, text="Type in the new password.")
        self.__label_password.pack()
        canvas4 = Canvas(self.__main_window, height=5, width=50)
        canvas4.pack()


        self.__input_text3 = Text(self.__main_window, height=1, width=25)
        self.__input_text3.pack()
        canvas5 = Canvas(self.__main_window, height=5, width=50)
        canvas5.pack()


        self.__display_button = Button(self.__main_window, text="Update", font=("Arial", 10),
                                       command=self.config_input,
                                       height=2, width=5)
        self.__display_button.pack()


        canvas5 = Canvas(self.__main_window, height=10, width=50)
        canvas5.pack()
        self.__credentials = Label(self.__main_window, text=" ")
        self.__credentials.pack()
        canvas6 = Canvas(self.__main_window, height=10, width=50)
        canvas6.pack()

    def config_input(self):


        """
        This function reads the <passwords.txt> file
        with <read_file> function, saves it to a variable,
        updates the data corresponding the user inputs in the
        variable data, and then writes the file <passwords.txt>
        again with <write_file> function with the defined
        data variable.

        :return: None
        """


        try:
            input1 = self.__input_text1.get("1.0", "end-1c")

            input2 = self.__input_text2.get("1.0", "end-1c")

            input3 = self.__input_text3.get("1.0", "end-1c")


            for char in input3:
                if char == ":":
                    self.__input_text3.delete("1.0", "end-1c")
                    raise NameError
                    break

            file = read_file("passwords.txt")


            if input1 in file and input2 in file[input1]:
                user_data = file[input1]
                user_data[input2] = row_encryption(input3, 0)
                file[input1] = user_data
                write_file("passwords.txt", file)
                self.__credentials.configure(text=f"Login credentials updated succesfully!")
                self.__input_text1.delete("1.0", "end-1c")
                self.__input_text2.delete("1.0", "end-1c")
                self.__input_text3.delete("1.0", "end-1c")
            else:
                self.__credentials.configure(text=f"Service or username/email not found")
        except NameError:
            self.__credentials.configure(text=f"Credentials can not include ':'")

class find_user_data:


    """
    This class defines the pop-up window for displaying
    login credentials from the save file. Window
    pop-ups when the <self.__find_user_data> button
    is pressed on the startpage.
    """


    def __init__(self):


        self.__main_window = Tk()
        self.__main_window.title("Find user data")


        self.__label1 = Label(self.__main_window, text="Here you can find and"
                                                       " display your login credentials",
                              font=("Arial", 10))
        self.__label1.pack()


        canvas1 = Canvas(self.__main_window, height=10, width=50)
        canvas1.pack()
        self.__label_service = Label(self.__main_window, text="Type in which service's "
                                                              " credentials you want to display.")
        self.__label_service.pack()
        canvas2 = Canvas(self.__main_window, height=5, width=50)
        canvas2.pack()


        self.__input_text1 = Text(self.__main_window, height=1, width=25)
        self.__input_text1.pack()
        canvas3 = Canvas(self.__main_window, height=10, width=50)
        canvas3.pack()


        self.__label_username = Label(self.__main_window, text="Type in the username/email"
                                                               " you want to display.")
        self.__label_username.pack()


        canvas4 = Canvas(self.__main_window, height=5, width=50)
        canvas4.pack()
        self.__input_text2 = Text(self.__main_window, height=1, width=25)
        self.__input_text2.pack()


        canvas7 = Canvas(self.__main_window, height=5, width=50)
        canvas7.pack()
        self.__display_button = Button(self.__main_window, text="Display", font=("Arial", 10),
                                      command=self.display_credentials,
                                      height=2, width=5)
        self.__display_button.pack()


        canvas4 = Canvas(self.__main_window, height=5, width=50)
        canvas4.pack()
        self.__display_all_button = Button(self.__main_window, text="Display all",
                                           font=("Arial", 10),
                                           command=display_all_credentials,
                                           height=2, width=10)
        self.__display_all_button.pack()


        canvas5 = Canvas(self.__main_window, height=10, width=50)
        canvas5.pack()
        self.__credentials = Label(self.__main_window, text="Your login credentials: ")
        self.__credentials.pack()
        canvas6 = Canvas(self.__main_window, height=10, width=50)
        canvas6.pack()


        self.__main_window.mainloop()


    def display_credentials(self):


        """
        When the <self.__display_button> button is pressed
        this funtion reads the <passwords.txt> file with
        <read_file> function and finds the user data
        corresponding the user inputs. Then the label
        <self.__credentials> is updated with the found
        user data.

        :return: None
        """


        input1 = self.__input_text1.get("1.0", "end-1c")

        input2 = self.__input_text2.get("1.0", "end-1c")

        file = read_file("passwords.txt")


        if input1 != "" and input2 != "":

            if input1 in file and input2 in file[input1]:
                user_data = file[input1]
                password = user_data[input2]
                encrypted_password = row_encryption(password, 1)

                self.__credentials.configure(text=f"Your login credentials:"
                                                  f" {input1}/{input2}: {encrypted_password}")
                self.__input_text1.delete("1.0", "end-1c")
                self.__input_text2.delete("1.0", "end-1c")
            else:
                self.__credentials.configure(text=f"Service or username/email not found")
        else:
            self.__credentials.configure(text=f"You must fill in both boxes!")

class display_all_credentials:


    """
    When the <self.__display_all_button> button is pressed
    this class reads the <passwords.txt> file with
    <read_file> function and finds all user data
    Then a pop-up window is shown with the found
    user data.
    """


    def __init__(self):


        file = read_file("passwords.txt")           # Kaikkien tietojen tulostus halutaan uuteen ikkunaan,
                                                    # joten luodaan tälle toiminnolle oma luokka.
        self.__main_window = Tk()
        self.__main_window.title("All data")

        canvas = Canvas(self.__main_window, height=10, width=50)
        canvas.pack()

        self.__label1 = Label(self.__main_window, text="Your all credentials in form:"
                                                       " service/username or email: password",
                              font=("Arial", 10))
        self.__label1.pack()


        canvas1 = Canvas(self.__main_window, height=10, width=50)
        canvas1.pack()


        for key in file.keys():
            user_data = file[key]
            for username in user_data:
                password = row_encryption(user_data[username], 1)
                self.__label_credentials = Label(self.__main_window,
                                                 text=f"{key}/{username}: {password}")
                self.__label_credentials.pack()
                canvas2 = Canvas(self.__main_window, height=10, width=50)
                canvas2.pack()

        self.__main_window.mainloop()



def encrypt(text, index):


    """
    Encrypts its parameter using aencryption technology.

    :param text: str,  string to be encrypted
    :param index: int,  index that indicates what is needed
    to be done with the parameter <text>
    :return: str, <text> parameter encrypted
    """


    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z", "å", "ä", "ö", "0", "1", "2", "3",
                       "4", "5", "6", "7", "8", "9", "!", "?", "=", "%", "#",
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
    Encrypts its parameter using an encryption technology.

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


    """
    Function used to read data from text files.
    Data is read from files with a structure of
    <service>:<username>:<password>. The data is
    saved to the data structure file and then the
    data structure is returned.

    :param filename: str, indicates  the name of the
    file that needs to be read.
    :return: nested dict, the data structure
    consisting dictionaries in dictionaries.
    """


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
        file = open(filename, mode="w")
        file.close()

    return passwords

def write_file(filename, file):


    """
    Function is used to write text file of the
    given filename and the given data structure.
    Writes the file with a stucture of
    <service>:<username>:<password>

    :param filename: str, indicates  the name of the
    file that needs to be read.
    :param file: nested dict, the data structure
    consisting dictionaries in dictionaries.
    :return:
    """


    file_new = open(filename, mode="w")

    for service in file.keys():
        for username in file[service].keys():
            user = file[service]
            password = user[username]
            credentials = [service, username, password]
            file_new.write((f"{credentials[0]}:{credentials[1]}:{credentials[2]}"))


def append_file(filename, credentials):


    """
    Function is used to append text file of the
    given filename and the given data structure.
    Appends the file with a stucture of
    <service>:<username>:<password>

    :param filename: str, indicates  the name of the
    file that needs to be read.
    :param credentials: list/ the data structre
    consisting login credentials for one account.
    :return: None
    """


    try:
        file = open(filename, mode="a")
        file.write('\n')
        file.write((f"{credentials[0]}:{credentials[1]}:{credentials[2]}"))

    except IOError:

        file = open(filename, mode="w")
        file.write((f"{credentials[0]}:{credentials[1]}:{credentials[2]}"))

def main():

    gui = startpage()

if __name__ == "__main__":
    main()