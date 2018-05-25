# RailNL
# Random Algorithm
# Rutger van Heijningen
# 10272224

# Import
import csv
import random
import copy
import sys
from random import randint
from Python_files.Hillclimber import run_hillclimbing_algorithm

<<<<<<< HEAD
=======
# Map variables
noord_zuid_holland = 1
nationaal = 2

# Choose which map you want (noord_zuid_holland or nationaal)
run_map = noord_zuid_holland

# Configurations
if run_map == 1:
    min_minutes = 381
    amount_of_trains = 5
    amount_of_minutes = 120
    break_hill_after = 1000
    run_times = 100
elif run_map == 2:
    min_minutes = 1551
    amount_of_trains = 18
    amount_of_minutes = 180
    break_hill_after = 1000
    run_times = 30
else:
    print("No valid map selected!")
    sys.exit()

# Upperbound Score
upperbound = ((1 * 10000) - (amount_of_trains * 20 + min_minutes / 10.))

# Load CSV
if run_map == 1:
    with open('ConnectiesHolland.csv', 'r') as csvfile:
        data = list(csv.reader(csvfile))
elif run_map == 2:
    with open('ConnectiesNationaal.csv', 'r') as csvfile:
        data = list(csv.reader(csvfile))
else:
    print("No valid load-file selected!")
    sys.exit()

# New dict for all connections
totaal = []

# Temp variable
temp_dict = 0

# Loading data in totaal
for i in data:
    totaal.append({"Begin":data[temp_dict][0], "Eind":data[temp_dict][1], "Tijd":data[temp_dict][2], "M":temp_dict})
    totaal.append({"Begin":data[temp_dict][1], "Eind":data[temp_dict][0], "Tijd":data[temp_dict][2], "M":temp_dict})
    temp_dict += 1
>>>>>>> 167ec20ee3886f367a4e71974119d4537af52877

# Create random start formation
def start_position(totaal, run_map, amount_of_trains, amount_of_minutes):

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

            # Break if traject is longer then amount_of_minutes allowed
            if time > amount_of_minutes:
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

    # Loop trains
    for i in dienstregeling:

        minute = 0
        b = 0

        # Loop trajects
        for j in dienstregeling[a]:

            # Create mirror list
            minute += dienstregeling[a][b]["Tijd"]
            mirror = dienstregeling[a][b]["M"]
            mirror_list.append(mirror)

            b += 1

        # Total time
        total_minutes += minute
        a += 1

    ##### P score #####
    all_tracks = copy.copy(totaal)

    # Check for all possible tracks and delete and driven tracks
    for i in all_tracks:
        for j in mirror_list:
            if j == i["M"]:
                try:
                    all_tracks.remove(i)
                except:
                    continue

    # Total tracks - tracks driven = tracks left
    tracks_left = len(totaal) - len(all_tracks)

    # Score function
    p = float(tracks_left) / (len(totaal)/2.)
    traject_score = ((p * 10000) - (amount_of_trains * 20 + total_minutes / 10.))

    return traject_score, dienstregeling

# Hillclimber function
def hillclimber(tracks, h_score, amount_of_minutes, amount_of_trains, break_hill_after, totaal, run_map):

    # Hillclimber variables
    hill_track = copy.copy(tracks)
    hill_score = h_score
    counter = 0
    max_score = 0
    high_p = 0

    # If 1000 times no higher score, break
    while (counter < break_hill_after):

        # Random remove 1 train out of the list
        swap_number = randint(0, amount_of_trains - 1)
        hill_reverse = hill_track[swap_number]
        hill_track.remove(hill_track[swap_number])

        ##### Create a new random train to insert the removed train #####

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

        # Create 1 train
        for i in range(1):
            br = 0
            time = 0
            score = 0

            # Create a single train with random connections
            while True:
                connect = connection(random_start)
                random_start = connect["Eind"]
                time += connect["Tijd"]
                br += 1

                # Break if traject is longer then amount_of_minutes allowed
                if time > amount_of_minutes:
                    break

                # Random break after 4 connection to create shorter trajects sometimes
                if br > 4:
                    if 0.9 < random.uniform(0, 1):
                        break

                score += connect["Tijd"]
                dienstregeling[i].append(connect)

            # Insert train in the list to create a new dienstregeling
            hill_track.insert(0, list(dienstregeling[i]))

        ##### Minutes score #####
        a = 0
        total_minutes = 0
        mirror_list = []

        # Loop trains
        for i in hill_track:

            minute = 0
            b = 0

            # Loop trajects
            for j in hill_track[a]:

                minute += hill_track[a][b]["Tijd"]
                mirror = hill_track[a][b]["M"]
                mirror_list.append(mirror)

                b += 1

            # Total time
            total_minutes += minute
            a += 1

        ##### P score #####
        all_tracks = copy.copy(totaal)

        # Check for all possible tracks and delete and driven tracks
        for i in all_tracks:
            for j in mirror_list:
                if j == i["M"]:
                    try:
                        all_tracks.remove(i)
                    except:
                        continue

        # Total tracks - tracks driven = tracks left
        tracks_left = len(totaal) - len(all_tracks)

        # Score function
        p = float(tracks_left) / (len(totaal)/2.)
        traject_score = ((p * 10000) - (amount_of_trains * 20 + total_minutes / 10.))

        # Safe highest P per hillclimber
        if p > high_p:
            high_p = p
            best_track = copy.copy(hill_track)

        # Check if score is higher, set counter = 0
        if traject_score > hill_score:
            hill_score = traject_score
            counter = 0
        else:
            # Check for all possible tracks and delete and driven tracks
            hill_track.remove(hill_track[0])
            hill_track.insert(swap_number, hill_reverse)
            counter += 1

    return hill_score, best_track, high_p

# Fine tuning best hillclimber track
def fine_tune(fine_tune_track, amount_of_trains):

    # Fine tune
    fine_tune_score = 0
    fine_tune_counter = 0
    fine_tuned_track = copy.copy(fine_tune_track)
    time_off = []

    # Loop trains
    for train in fine_tuned_track:
        if train == fine_tuned_track[amount_of_trains]:
            break

        value = 0
        traject_length = len(train)

        # Check for repeating tracks (3,4 or 5 times same track)
        while (value < (traject_length - 2)):
            if train[value]["M"] == train[value + 1]["M"]:
                if train[value + 1]["M"] == train[value + 2]["M"]:
                    del train[value + 1]
                    time_off.append(train[value + 1]["Tijd"])
                    time_off.append(train[value + 1]["Tijd"])
                    del train[value + 1]
                    value += -1
                    traject_length += -2
                else:
                    value += 1
            else:
                value += 1

        end_1 = (traject_length - 1)
        end_2 = (traject_length - 2)

        # Check for repeating tracks on the end of trains
        if train[end_2]["M"] == train[end_1]["M"]:
            time_off.append(train[end_1]["Tijd"])
            del train[end_1]

    # Raise score with deleted tracks
    fine_tune_score = (sum(time_off) / 10.)

    return fine_tuned_track, fine_tune_score

# Layout function
def layout_1(run_map, amount_of_trains, run_times, upperbound, break_hill_after):

    # Welcome text
    if run_map == 'North':
        print("_______________________________________________________________")
        print("Running Hillclimber Algorithm on the map 'Noord & Zuid Holland'")
        print("_______________________________________________________________")
    elif run_map == 'NL':
        print("____________________________________________________")
        print("Running Hillclimber Algorithm on the map 'Nederland'")
        print("____________________________________________________")
    else:
        print("No valid map selected!")
        sys.exit()

    print("")

    # Configuration text
    print("Amount of trains = %i" %(amount_of_trains))
    print("Amount of attemps before hillclimber breaks = %i" %(break_hill_after))
    print("Amount of times hillclimber runs = %i" %(run_times))
    print("Upperbound Score = %.2f" %(upperbound))
    print("")

# Layout function
def layout_2(run_map):

    # Layout
    if run_map == 'North':
        print("_______________________________________________________________")
    if run_map == 'NL':
        print("____________________________________________________")

# Main
def main(maps, trains, totaal):

    # Choose which map you want (noord_zuid_holland or nationaal)
    run_map = maps
    amount_of_trains = trains

    # Configurations
    if run_map == 'North':
        min_minutes = 381
        amount_of_minutes = 120
        break_hill_after = 1000
        run_times = 1
    elif run_map == 'NL':
        min_minutes = 1551
        amount_of_minutes = 180
        break_hill_after = 1000
        run_times = 30
    else:
        print("No valid map selected!")
        sys.exit()

    # Upperbound Score
    upperbound = ((1 * 10000) - (amount_of_trains * 20 + min_minutes / 10.))

    # Welcome & configuration text
    layout_1(run_map, amount_of_trains, run_times, upperbound, break_hill_after)

    # Variables
    hill_score = 0
    final_score = 0
    algorithm_counter = 0
    average = 0
    p_times = 0

    # Run algorithm n times
    for _ in range(run_times):

        # Call functions
        h_score, tracks = start_position(totaal, run_map, amount_of_trains, amount_of_minutes)
        hill_score, best_track, p_value = hillclimber(tracks, h_score, amount_of_minutes, amount_of_trains, break_hill_after, totaal, run_map)
        average += hill_score

        if hill_score > final_score:
            final_score = hill_score
            final_track = best_track

        if p_value == 1.0:
            p_times += 1

        algorithm_counter += 1

        # Counter
        sys.stdout.write("Hillclimber count = %i\r" %(algorithm_counter))
        sys.stdout.flush()

    # Fine tuning track
<<<<<<< HEAD
    fine_tune_track = copy.deepcopy(final_track)
    master_track, master_score = fine_tune(fine_tune_track, amount_of_trains)
=======
    fine_tune_track = copy.copy(final_track)
    master_track, master_score = fine_tune(fine_tune_track)
    print master_score
>>>>>>> 167ec20ee3886f367a4e71974119d4537af52877

    # Print maximum traject score
    print("\n")
    print("Amount of times p has a value of 1.0 = %i" %(p_times))
    print("")
    print("Average Score = %.2f" %(average/algorithm_counter))
    print("Highest Score = %.2f" %(final_score))
    print("Fine tuned Score = %.2f" %(final_score + master_score))
    print("")

    # Layout
    layout_2(run_map)

    train_number = 1

    # Print traject
    for train in master_track:
        if train == master_track[amount_of_trains]:
            break
        print("")
        print("Train %i" %(train_number))
        for track in train:
            print(track)
        train_number += 1

# Run script
if __name__ == "__main__":
    main()
