"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""
def read_distance_file(file_name):

    data = {}

    try:
        file = open(file_name, mode="r")

        for row in file:
            row = row.rstrip()
            lähtö, määränpää, etäisyys = row.split(";")
            etäisyydet = {}

            if lähtö in data:
                etäisyydet = data[lähtö]
                etäisyydet[määränpää] = etäisyys
                data[lähtö] = etäisyydet
            else:
                etäisyydet[määränpää] = etäisyys
                data[lähtö] = etäisyydet

        return data

    except IOError:
        print(f"Error: '{file_name}' can not be read.")
        return None

        return data

def distance_to_neighbour(data, departure, destination):

    try:

        data_lähtevät = data[departure]

        etäisyys = data_lähtevät[destination]

        return etäisyys


    except KeyError:
        return None

def main():

    file = read_distance_file("distances1.txt")

    kaupunki1 = input("Kaupunk1i:")
    kaupunki2 = input("Kaupunki2:")


    etäisyys = distance_to_neighbour(file, kaupunki1, kaupunki2)

    print(etäisyys)

if __name__ == "__main__":
    main()
