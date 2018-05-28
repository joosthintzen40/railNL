# Hintzen, Joost - 10434143
# Heijningen, Rutger van - 10272224
# Kemmere, Simon - 10798250
# Function that runs the greedy algorithm x amount of times.
# Data that gets loaded in depends on the configuration chosen in
# main.py.


import csv
import random
import math
from itertools import chain
import copy
import sys
from Python_files.Greedy import graph_Simon2



def run_greedy(data, holland, iterations, p_driven, maps_minutes):

    # create liste for storing scores and stations
    score_list = []
    list_stations = []
    score_max = 0

    # open file that contains all stations
    with open(data, 'r') as stationsfile:
        stationreader = csv.reader(stationsfile)
        for row in stationreader:
            list_stations.append(row[0])


    # determines how many times the algorithm is run
    for j in range(iterations):


        # create lists to store upcoming information
        p_path = []
        minutes = []
        lijst = []
        path_list = []
        p_list = []

        # run greedy for pre-determined amount of times, i.e., trains
        for i in range(holland.train):

            # choose random begin station from list of all stations
            station = random.choice(list_stations)

            # append chosen begin station to new list
            lijst.append(station)

            # remove begin station from list of all stations
            list_stations.remove(station)

            # use begin station in greedy algorithm
            graph_Simon2.greedy(station, holland, p_path, minutes, map_minutes)

        # renew list of all stations by appending removed (begin) stations
        list_stations.extend(lijst)

        # keep track of amount of iterations
        sys.stdout.write("\riteration: %i" %(j))
        sys.stdout.flush()

        # unchain the paths of all stations
        p_list = list(chain.from_iterable(p_path))

        # therefor it can be turned into a tuple
        path_list = list(map(tuple,p_list))

        # determine amount of unique items
        uniq = set()
        for s in path_list:
            if not (s in uniq or (s[1], s[0]) in uniq):
                uniq.add(s)

        # amount of unique items corresponds with amount of ridden connections
        p = len(list(uniq))/p_driven

        # calculate score
        score_greedy = graph_Simon2.Score(p, holland.train, sum(minutes)).get_score()

        # remember score if score is higher than all previous ones
        if score_greedy > score_max:
                score_max = score_greedy
                final_track = p_path

        # append all scores to a list
        score_list.insert(0, score_greedy)

    # print all paths of all trains that reached the highest score
    train_count = 1
    for i in final_track:
        print("")
        print ("Traject of train", train_count)
        for j in i:
            print(j)
        train_count += 1
    print("")
    print("The score of these trajectories account for", score_max, "points")
