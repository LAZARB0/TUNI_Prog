"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {}
    lista_aakkosina = sorted(english_spanish)
    sanat = ', '.join(lista_aakkosina)
    print("Dictionary contents:")
    print(sanat)

    while True:



        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:

                print(word,"in Spanish is",english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            sana = input("Give the word to be added in English: ")
            käännös = input("Give the word to be added in Spanish: ")
            english_spanish[sana] = käännös

            lista_aakkosina = sorted(english_spanish)
            sanat = ', '.join(lista_aakkosina)
            print("Dictionary contents:")
            print(sanat)

        elif command == "R":

            poistettava = input("Give the word to be removed: ")
            if poistettava in english_spanish:

                del english_spanish[poistettava]
            else:
                print("The word hey could not be found from the dictionary.")

        elif command == "P":

            lista_aakkosina = sorted(english_spanish)
            print("")
            print("English-Spanish")
            for sana in lista_aakkosina:
                print(sana,english_spanish[sana])


            for sana in english_spanish:
                käännös = english_spanish[sana]
                spanish_english[käännös] = sana

            print("")
            print("Spanish-English")

            lista_aakkosina = sorted(spanish_english)
            for sana in lista_aakkosina:
                print(sana, spanish_english[sana])
            print("")


        elif command == "T":

            lause = input("Enter the text to be translated into Spanish: ")

            lause_lista = lause.split(" ")
            käännetty = ""
            for sana in lause_lista:
                if sana in english_spanish:
                    käännettysana = english_spanish[sana]
                    käännetty += käännettysana + " "
                else:
                    käännetty += sana + " "
            print("The text, translated by the dictionary:")
            print(käännetty)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
