"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi


Project 3: Matkareitin optimoija
"""


def read_distance_file(file_name):


    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: dictionary | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
    """

    data = {}

    # Try - except rakenteella ensin tiedoston avaus.

    try:

        file = open(file_name, mode="r")

        # For loopilla tiedoston rivien luku ja tietojen tallentaminen rakenteeseen.

        for row in file:
            row = row.rstrip()
            departure, destination, distance = row.split(";")
            distances = {}

            if departure in data:
                distances = data[departure]
                distances[destination] = distance
                data[departure] = distances
            else:
                distances[destination] = distance
                data[departure] = distances
        return data

    except IOError:
        return None


def add_distance(data):


    """
    Reads the distance information given as the input value of the departure_city,
    destination_city and distance variables and adds the wanted distance to the
    file given as the parameter.

    :param data: data file read and created from the file given in read_distance_file.
    :return: the updated data structure containing the keys and values added
             is returned / None, if the given distance is not an integer.
    """


    departure_city = input("Enter departure city: ")
    destination_city = input("Enter destination city: ")
    distance = input("Distance: ")

    # Try - except rakenteella syötteen tallentaminen tietorakenteeseen
    # jos virheitä ei ilmene.

    try:
        data[departure_city][destination_city] = int(distance)

        return data

    except KeyError:
        distances = {}
        distances[destination_city] = distance
        data[departure_city] = distances
        return data

    except ValueError:
        print(f"Error: '{distance}' is not an integer.")
        return None

    # Except KeyErrorilla korjattu ei oletettu virhe joka ilmeni syöttäessä uutta lähtökaupunkia.
    # Except ValueErrorilla virheilmoitus jos distance muuttuja ei ole kokonaisluku.

def remove_distance(data):


    """
    Reads the distance information given as the input value of the departure_city and
    destination_city variables and removes the given distance from the file
    given as the parameter.

    :param data: data file read and created from the file given in read_distance_file.
    :return: the updated data structure from which the defined distance has been removed
            / if there is no road segment between the cities or the input is invalid
            an error message is printed and the original data structure is returned.
    """


    departure_city = input("Enter departure city: ")
    if departure_city in data:

        destination_city = input("Enter destination city: ")

        if destination_city in data[departure_city]:

            data[departure_city].pop(destination_city, None)

            return data

        else:
            print(f"Error: missing road segment between '{departure_city}' and '{destination_city}'.")
            return data

    else:
        print(f"Error: '{departure_city}' is unknown.")
        return data


def find_route(data, departure, destination):


    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: dictionary which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stores twice.
    """


    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def route(data, departure, destination):


    """
    Uses the funcion find_route to find a route between <departure>
    and <destination> cities and calculates the distance from the route
    and prints the route and distance

    :param data: dictionary which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: None
        """


    route = find_route(data, departure, destination)

    # Jos lahtö ja määränpää kaupungit ovat samat edetään seuraavalla rakenteella:

    if len(route) == 2 and route[0] == route[1]:
        string = "-".join(route)
        print(f"{string} (0 km)")

    # Jos reittiä ei löydetty find_route funktiosta:

    elif route == []:
        print(f"No route found between '{departure}' and '{destination}'.")

    # Virhetarkastelu jos lähtökaupunkia ei löydy rakenteesta on tehty syötteiden lisäksi main-funktioon
    # Jos virhetarkasteluissa ei löydy virheitä:

    else:
        string = "-".join(route)

        route = find_route(data, departure, destination)

        # For loopilla haetaan tietorakenteesta etäisyydet ja summataan ne distance muuttujaan

        distance = 0

        for ind in range(1, len(route)):
            distance += distance_to_neighbour(data, route[ind - 1], route[ind])

        print(f"{string} ({distance} km)")


def fetch_neighbours(data, city):


    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: dictionary, A data structure containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """

    try:

        data_departures = data[city]

        cities = data_departures.keys()
        cities = sorted(cities)

        return cities

    # Jos funktioon annetuilla parametreillä syntyy virhe palautetaan tyhjä lista.

    except ValueError:
        return []
    except KeyError:
        return []


def distance_to_neighbour(data, departure, destination):


    """
    Calculates the distance from the departure city to the
    destination city and returns the distance.

    :param data: dictionary, a data structure containing the
           distance information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: the distance calculated as the distance between
           the parameter cities.
    """

    try:

        data_departures = data[departure]
        distance = int(data_departures[destination])
        return distance

    except KeyError:
        return None


def display_all(data):


    """
    Goes through the given data structure and prints all the keys and
    the values in the data structure.

    :param data: dictionary, A data structure containing the distance
           information between the known cities.
    :return: None
    """


    for departure_city in sorted(data):
        data_departures = data[departure_city]

        for destination_city in sorted(data_departures):
            print(f"{departure_city:<14}{destination_city:<14}{data_departures[destination_city]:>5}")


def display_neighbours(data, departure_city):


    """
    Goes through the data structure inside the dictionary assigned to the key
    in the parameter <data> and prints all the keys and values.

    :param data: dictionary, A data structure containing the distance
           information between the known cities.
    :param departure_city: str, the name of the city of which the neighbour cities
           re wanted to be displayed.
    :return: None
    """

    # Virhetarkastelu jossa käydään läpi löytyykö kaupunki
    # rakenteesta avaimena tai minkä tahansa avaimen
    # arvon sisältämän dictionaryn avaimena, sillä tehtävänannon
    # mukaan jos lähtökaupunki löytyy tietorakenteesta, täytyy
    # sen naapurit tulostaa, vaikka kaupungista ei olisi lähteviä
    # yhteyksiä

    departure_cities = data.keys()
    error_ind = 0
    for city in departure_cities:
        if departure_city in data[city]:
            error_ind = 1
            break

    if error_ind == 0:
        print(f"Error: '{departure_city}' is unknown.")
        pass
    else:

        try:

            data_departures = data[departure_city]

            for kaupunki_index in sorted(data_departures):

                print(f"{departure_city:<14}{kaupunki_index:<14}{data_departures[kaupunki_index]:>5}")

        except KeyError:
            pass


def main():


    input_file = input("Enter input file name: ")

    distance_data = read_distance_file(input_file)

    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")

        if action == "":
            print("Done and done!")
            return

        elif "display".startswith(action):

           display_all(distance_data)

        elif "add".startswith(action):

            distance_data = add_distance(distance_data)

        elif "remove".startswith(action):

            distance_data = remove_distance(distance_data)

        elif "neighbours".startswith(action):

            departure_city = input("Enter departure city: ")

            display_neighbours(distance_data, departure_city)

        elif "route".startswith(action):

            departure_city = input("Enter departure city: ")

            departure_cities = distance_data.keys()

            # Virhetarkastelu jossa käydään läpi löytyykö kaupunki
            # rakenteesta avaimena tai minkä tahansa avaimen
            # arvon sisältämän dictionaryn avaimena

            error_ind = 0
            for city in departure_cities:
                if departure_city in distance_data[city]:
                    error_ind = 1
                    break

            if error_ind == 0:
                print(f"Error: '{departure_city}' is unknown.")
                pass

            else:
                destination_city = input("Enter destination city: ")

                route(distance_data, departure_city, destination_city)

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()