"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    vokaalit = 0
    sana = input("Enter a word: ")
    for kirjain in range (0, len(sana)):
        if sana[kirjain] == "a" or sana[kirjain] == "e" or sana[kirjain] == "i" or sana[kirjain] == "u" or sana[kirjain] == "o" or sana[kirjain] == "y":
            vokaalit += 1
    konsonantit = len(sana) - vokaalit

    print(f'The word "{sana}" contains {vokaalit} vowels and {konsonantit} consonants.')

if __name__ == "__main__":
    main()
