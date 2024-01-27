"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def main():
    fiilis = int(input("How do you feel? (1-10) "))
    if fiilis > 10:
        print("Bad input!")

    elif fiilis <= 0:
            print("Bad input!")
    else:
        if fiilis == 1:
            print ("A suitable smiley would be :'(")
        elif fiilis == 10:
            print("A suitable smiley would be :-D")
        elif fiilis > 7:
            print("A suitable smiley would be :-)")
        elif fiilis < 4:
            print ("A suitable smiley would be :-(")
        else:
            print("A suitable smiley would be :-|")
if __name__ == "__main__":
    main()
