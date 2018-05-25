# Hintzen, Joost - 10434143
# Heijningen, Rutger van - 10272224
# Kemmere, Simon - 10798250
#
# Function that runs the determines every next connection of a train path,
# functioning within the given time constraits.
# Data that gets loaded in depends on the configuration chosen in
# main.py.

# Import
import csv
import random
import copy
import sys
from random import randint
from Python_files.Random import run_random_algorithm


# Random algorithm
def run(totaal, run_map, amount_of_trains):

    # Random start station
    random_start = totaal[randint(0, (len(totaal)-1))]["Begin"]

    # Loading start station with all possible connections
    def connection(random_start):

        # Temp array and temp variable
        temp_array = []
        temp = 0

        # Load connection in temp_array
        for i in totaal:
            if i["Begin"] == random_start:
                temp_array.append({"Begin":totaal[temp]["Begin"],
                                    "Eind":totaal[temp]["Eind"],
                                    "Tijd":int(totaal[temp]["Tijd"]),
                                    "M":int(totaal[temp]["M"])})

            temp += 1

        # Return traject
        traject = temp_array[randint(0, (len(temp_array)-1))]
        return traject

    # Array
    if run_map == 'North':
        dienstregeling = [[],[],[],[],[],[],[]]
    elif run_map == 'NL':
        dienstregeling = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    else:
        print("No valid array selected!")
        sys.exit()

    # Create 5 trains
    for i in range(amount_of_trains):
        br = 0
        time = 0
        score = 0

        # Create a single train with random connections
        while True:
            connect = connection(random_start)
            random_start = connect["Eind"]
            time += connect["Tijd"]
            br += 1

            # Break if traject is longer then 120 min
            if time > 120:
                break

            # Random break after 4 connection to create shorter trajects sometimes
            if br > 4:
                if 0.9 < random.uniform(0, 1):
                    break

            score += connect["Tijd"]
            dienstregeling[i].append(connect)

    ##### Minutes score #####
    a = 0
    total_minutes = 0
    mirror_list = []

    for i in dienstregeling:

        minute = 0
        b = 0

        for j in dienstregeling[a]:

            minute += dienstregeling[a][b]["Tijd"]
            mirror = dienstregeling[a][b]["M"]
            mirror_list.append(mirror)

            b += 1

        total_minutes += minute
        a += 1

    ##### P score #####
    all_tracks = copy.copy(totaal)

    for i in all_tracks:
        for j in mirror_list:
            if j == i["M"]:
                try:
                    all_tracks.remove(i)
                except:
                    continue

    tracks_left = len(totaal) - len(all_tracks)

    # Score function
    p = float(tracks_left) / (len(totaal)/2.)
    traject_score = ((p * 10000) - (amount_of_trains * 20 + total_minutes / 10.))

    return traject_score, dienstregeling

# Layout function
def layout_1(run_map, amount_of_trains, run_times, upperbound):

    # Welcome text
    if run_map == 'North':
        print("___________________________________________________________")
        print("Running Random Algorithm on the map 'North & South Holland'")
        print("___________________________________________________________")
    elif run_map == 'NL':
        print("_________________________________________________")
        print("Running Random Algorithm on the map 'Netherlands'")
        print("_________________________________________________")
    else:
        print("No valid map selected!")
        sys.exit()

    print("")

    # Configuration text
    print("Amount of trains = %i" %(amount_of_trains))
    print("Amount of times random runs = %i" %(run_times))
    print("Upperbound Score = %.2f" %(upperbound))
    print("")

# Layout function
def layout_2(run_map):

    # Layout
    if run_map == 'North':
        print("___________________________________________________________")
    if run_map == 'NL':
        print("_________________________________________________")

# Main
def main(maps, trains, totaal):

    # Choose which map you want (noord_zuid_holland or nationaal)
    run_map = maps
    amount_of_trains = trains

    # Configurations
    if run_map == 'North':
        min_minutes = 381
        amount_of_minutes = 120
        run_times = 10000
    elif run_map == 'NL':
        min_minutes = 1551
        amount_of_minutes = 180
        run_times = 1000
    else:
        print("No valid map selected!")
        sys.exit()

    # Upperbound Score
    upperbound = ((1 * 10000) - (amount_of_trains * 20 + min_minutes / 10.))


    # Welcome & configuration text
    layout_1(run_map, amount_of_trains, run_times, upperbound)

    # Run algorithm n times
    max_score = 0
    average = 0
    count = 0

    # Run algorithm n times
    for _ in range(run_times):
        # Call functions
        h_score, tracks = run(totaal, run_map, amount_of_trains)
        average += h_score

        if h_score > max_score:
            max_score = h_score
            final_track = tracks

        count += 1

        # Counter
        sys.stdout.write("\rRandom count = %i" %(count))
        sys.stdout.flush()

    # Print maximum traject score
    print("\n")
    print("Average Score = %.2f" %(average/count))
    print("Highest Score = %.2f" %(max_score))
    print("")

    # Layout
    layout_2(run_map)

    train_number = 1

    # Print traject
    for train in final_track:
        if train == final_track[amount_of_trains]:
            break
        print("")
        print("Train %i" %(train_number))
        for track in train:
            print(track)
        train_number += 1

# Run script
if __name__ == "__main__":
    main()
