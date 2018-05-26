# Hintzen, Joost - 10434143
# Heijningen, Rutger van - 10272224
# Kemmere, Simon - 10798250
#
# Function that runs Dijkstra algorithm x amount of times.
# Data that gets loaded in depends on the configuration chosen in
# main.py.

import csv
import random
import math
from itertools import chain
import copy
import sys
from Python_files.Dijkstra import dijkstra



def run_greedy(data, holland, iterations):
    score_list = []
    list_stations = []
    score_max = 0

    with open(data, 'r') as stationsfile:
        stationreader = csv.reader(stationsfile)
        for row in stationreader:
            list_stations.append(row[0])

    for j in range(iterations):

        p_path = []
        minutes = []
        lijst = []
        path_list = []
        p_list = []

        for i in range(holland.train):
            station = random.choice(list_stations)
            lijst.append(station)
            list_stations.remove(station)
            dijkstra.dijkstra(station, holland, p_path, minutes)

        list_stations.extend(lijst)
        sys.stdout.write("\riteration: %i" %(j))
        sys.stdout.flush()

        p_list = list(chain.from_iterable(p_path))


        path_list = list(map(tuple,p_list))
        uniq = set()
        for s in path_list:
            if not (s in uniq or (s[1], s[0]) in uniq):
                uniq.add(s)

        p = len(list(uniq))/28
        score_greedy = dijkstra.Score(p, holland.train, sum(minutes)).get_score()

        if score_greedy > score_max:
                score_max = score_greedy
                final_track = p_path

        score_list.insert(0, score_greedy)

    train_count = 1
    for i in final_track:
        print("")
        print ("Traject of train", train_count)
        for j in i:
            print(j)
        train_count += 1
    print("")
    print("The score of these trajectories account for", score_max, "points")
