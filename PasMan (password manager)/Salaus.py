"""
Creator: Lassi Cederlöf
Email: lassi.cederlof@tuni.fi
"""


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

def read_message():

    rivi = "s"
    viesti = []
    while rivi != "":
        rivi = input("")
        viesti.append(rivi)
    del viesti[-1]
    return viesti

def main():


    print("Enter text rows to the message. Quit by entering an empty row.")

    msg = read_message()
    index = int(input("Index: "))
    print("ROT13:")
    for rivi in msg:
        salattu = row_encryption(rivi, index)
        print(salattu)


if __name__ == "__main__":
    main()

