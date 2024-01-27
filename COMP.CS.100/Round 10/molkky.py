"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


class Player:

    def __init__(self, name):

        self.__name = name
        self.__points = 0
        self.__throws = 0
        self.__total_points = 0
        self.__hit_count = 0
        self.__hit_percentage = 0.0

    def get_name(self):

        return self.__name

    def add_points(self, points):

        self.__points += points

        if self.__points > 50:
            print("Matti gets penalty points!")
            self.__points = 25

        elif self.__points >= 40 and self.__points < 50:

            print(f"{self.__name} needs only {50 - self.__points} points. It's better to avoid ", end = "")
            print("knocking down the pins with higher points.")


    def get_points(self):

        return self.__points

    def has_won(self):

        if self.__points == 50:
            return True
        else:
            return False

    def cheers_counter(self, points):

        self.__total_points += points
        self.__throws += 1

        keskiarvo = self.__total_points / self.__throws

        if points > keskiarvo:
            print(f"Cheers {self.__name}!")


    def hit_percentage(self, points):

        try:

            if points > 0:
                self.__hit_count += 1
            else:
                pass
            percentage = self.__hit_count / self.__throws * 100
            percentage = f"{percentage:.1f}"
            self.__hit_percentage = percentage
        except ZeroDivisionError:
            self.__hit_percentage = 0.0

    def get_percentage(self):

        return self.__hit_percentage




def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        in_turn.cheers_counter(pts)

        in_turn.hit_percentage(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,","hit percentage",player1.get_percentage())
        print(player2.get_name() + ":", player2.get_points(), "p,","hit percentage",player2.get_percentage())
        print("")

        throw += 1


if __name__ == "__main__":
    main()
