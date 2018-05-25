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

        for i in hill_track:

            minute = 0
            b = 0

            for j in hill_track[a]:

                minute += hill_track[a][b]["Tijd"]
                mirror = hill_track[a][b]["M"]
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

        p = float(tracks_left) / (len(totaal)/2.)
        traject_score = ((p * 10000) - (amount_of_trains * 20 + total_minutes / 10.))

        if p > high_p:
            high_p = p
            best_track = copy.copy(hill_track)

        if traject_score > hill_score:
            hill_score = traject_score
            counter = 0
        else:
            hill_track.remove(hill_track[0])
            hill_track.insert(swap_number, hill_reverse)
            counter += 1

    return hill_score, best_track, high_p

# Fine tuning best hillclimber track
def fine_tune(fine_tune_track, amount_of_trains):

    # Fine tune
    fine_tune_score = 0
    fine_tune_counter = 0
    fine_tuned_track = fine_tune_track

    for train in fine_tuned_track:
        # print""
        if train == fine_tuned_track[amount_of_trains]:
            break

        value = 0
        traject_place = 0

        while (traject_place < (len(train) - 3)):
            if train[value]["M"] == train[value + 1]["M"] and train[value + 1]["M"] == train[value + 2]["M"]:
                train.remove(train[value + 1])
                train.remove(train[value + 1])
                traject_place += 3
            else:
                traject_place += 1
            train_length = len(train)

            value += 1

    for train in fine_tuned_track:
        # print""
        if train == fine_tuned_track[amount_of_trains]:
            break

        end_1 = (len(train) - 2)
        end_2 = (len(train) - 1)

        # for track in train:
        #     print track

        # print train[end_1]
        # print train[end_2]
        # print""
        # print train[end_1]["M"]
        # print train[end_2]["M"]

        if train[end_1]["M"] == train[end_2]["M"]:
            # print"hello"
            # print train[end_2]
            train.remove(train[end_2])
            fine_tune_counter += 1
        # print ""
        #
        # for track in train:
        #     print track
        # print ""

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
    count = 0
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

        count += 1

        # Counter
        sys.stdout.write("\rHillclimber count = %i" %(count))
        sys.stdout.flush()

    # Fine tuning track
    fine_tune_track = copy.deepcopy(final_track)
    master_track, master_score = fine_tune(fine_tune_track, amount_of_trains)

    # Print maximum traject score
    print("\n")
    print("Amount of times p has a value of 1.0 = %i" %(p_times))
    print("")
    print("Average Score = %.2f" %(average/count))
    print("Highest Score = %.2f" %(final_score))
    print("Finetuned Score = %.2f" %(master_score))
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

    print("")
    print("----------> Fine tuning")

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

##### To Do #####
# Check Score
# 3 keer dezelfde M
# Aan het einde 2 keer dezelfde M
# random start station update, alleen starten vanaf nog niet gestart station