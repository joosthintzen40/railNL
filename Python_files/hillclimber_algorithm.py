# RailNL
# Random Algorithm

# Import
import csv
from random import randint
import random
import copy

# Configuration
amount_of_trains = 5

# Load CSV
with open('ConnectiesHolland.csv', 'r') as csvfile:
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

def start_position():
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
    dienstregeling = [[],[],[],[],[],[],[]]

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
    p = float(tracks_left) / len(totaal)
    traject_score = (p * 10000 - ((amount_of_trains * 20) + (total_minutes / 10)))

    return traject_score, dienstregeling

def hillclimber(tracks, h_score):
    hill_track = copy.copy(tracks)
    hill_score = h_score
    counter = 0
    max_score = 0
    high_p = 0

    while (counter < 1000):
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
        dienstregeling = [[],[],[],[],[],[],[]]

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

                # Break if traject is longer then 120 min
                if time > 120:
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
        # print tracks_left
        # print(len(totaal)/2.)
        # Score function
        p = float(tracks_left) / (len(totaal)/2.)
        # print p
        # print total_minutes
        traject_score = ((p * 10000) - (amount_of_trains * 20 + total_minutes / 10.))
        # print traject_score, hill_score

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

        counter += 1

    return hill_score, best_track

def main():
    # Run algorithm n times
    hill_score = 0
    final_score = 0
    count = 0
    average = 0

    for _ in range(200):
        h_score, tracks = start_position()
        hill_score, best_track = hillclimber(tracks, h_score)
        average += hill_score

        if hill_score > final_score:
            final_score = hill_score
            final_track = best_track


        count += 1
        print count

    # Print maximum traject score
    print("Average Score = %.2f" %(average/count))
    print("Maximum Score = %.2f" %(final_score))

    train_number = 1

    for train in final_track:
        if train == final_track[amount_of_trains]:
            break
        print ""
        print "Train %i" %(train_number)
        for track in train:
            print track
        train_number += 1

# Run script
if __name__ == "__main__":
    main()

##### To Do #####
# Check Score
# 3 keer dezelfde M
# Aan het einde 2 keer dezelfde M
