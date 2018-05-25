# Hintzen, Joost - 10434143
# Heijningen, Rutger van - 10272224
# Kemmere, Simon - 10798250
#
# Function that runs the determines every next connection of a train path,
# functioning within the given time constraits.
# Data that gets loaded in depends on the configuration chosen in
# main.py.


import csv
import math
import random
from itertools import chain
from Data.datastructuur_graph import Graph
import copy
import sys
from Python_files.Greedy import run_greedy

# class that when called upon calculates the score for a timetable
class Score:
    def __init__(self, p, train, min):
        self.p = p
        self.train = train
        self.min = min

    def get_score(self):
        return self.p*10000 - (self.train*20 + self.min/10)


# class that gets called upon by main.py
class Holland:

    def __init__(self, train, directory):

        # instantiate directory path
        self.dir = directory

        # instantiate graph class
        self.graph = Graph()

        # instantiate amount of trains
        self.train = train

        # call method with instantiated directory
        self.get_graph(self.dir)

    # method that loads connections and it´s corresponding distance
    def get_graph(self, dir):
        with open(dir, 'r') as csvfile:
            nlreader = csv.reader(csvfile)
            for row in nlreader:
                self.graph.add_station(row[0])
                self.graph.add_station(row[1])
                self.graph.add_connection(row[0], row[1], int(row[2]))
        return self.graph


# greedy algorithm
def greedy(begin, holland, p_path, minutes):

    # instantiate variables/dicts/lists
    stations = copy.deepcopy(holland.graph.vert_dict)
    infinity = math.inf
    path = []

    breaker = False
    min_node = None
    station = None
    tot_dist = 0
    trajectlist = []

    while True:

        # if no next station is given, i.e., first iteration
        # get begin station from method
        if min_node is None:
            min_node = stations[begin]

        # else next station is begin station
        else:
            min_node = station


        # create dict, where neighbors of repeatingly updated begin station are stored
        neighbor_dict = {}

        # loop through all neigbours of determined begin station
        for neighbor, distance in stations[min_node.id].adjacent.items():

            # add station from adjecency list to neighbor_dict
            neighbor_dict.update({neighbor: distance})

            # check which distance, and corresponding station is shortest from
            # begin station
            station = min(neighbor_dict.items(), key=lambda x:x[1])[0]
            distance = min(neighbor_dict.items(), key=lambda x:x[1])[1]

        #
        if breaker:
            break

        # determine whether total distance + distance of begin station
        # to be will exceed time constraint
        if  tot_dist + distance < 181:
            trajectlist.append(min_node.id)
        else:
            break

        # add distance to total distance becaues new connections
        # didn't exceed time constraint
        tot_dist += distance

        # set ridden connection to infinity as to prevent backtracking
        stations[min_node.id].adjacent[station] = infinity
        stations[station.id].adjacent[min_node] = infinity

    # add begin and end station to list
    # as to keep track of ridden paths
    counter = 1
    for i in trajectlist[:-1]:
        path.insert(0, [trajectlist[counter], i])
        counter += 1

    # append to p_path to get p
    p_path.append(path)


    # make list of minutes per trajectory
    minutes.append(tot_dist)
