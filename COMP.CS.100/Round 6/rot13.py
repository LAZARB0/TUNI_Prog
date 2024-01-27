"""
COMP.CS.100 Programming 1
ROT13 program code template
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

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

def row_encryption(text):

    """
        Encrypts its parameter using ROT13 encryption technology.

        :param text: str,  string to be encrypted
        :return: str, <text> parameter encrypted using ROT13
        """

    lause = ""
    for luku in range(0, len(text)):
        merkki = text[luku]
        salattu = encrypt(merkki)
        lause += salattu

    return lause


def read_message():

    """Lukee käyttäjän syötteen ja muuttaa sen huudetuksi"""

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
    print("ROT13:")
    for rivi in msg:
        salattu = row_encryption(rivi)
        print(salattu)


if __name__ == "__main__":
    main()