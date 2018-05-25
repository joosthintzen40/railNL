import csv


def load_map(data):
    # Load CSV
    with open(data, 'r') as csvfile:
        data = list(csv.reader(csvfile))

    # New dict for all connections
    totaal = []

    # Temp variable
    temp_dict = 0

    # Loading data in totaal
    for i in data:
        totaal.append({"Begin":data[temp_dict][0], "Eind":data[temp_dict][1], "Tijd":data[temp_dict][2], "M":temp_dict})
        totaal.append({"Begin":data[temp_dict][1], "Eind":data[temp_dict][0], "Tijd":data[temp_dict][2], "M":temp_dict})
        temp_dict += 1

    return totaal
