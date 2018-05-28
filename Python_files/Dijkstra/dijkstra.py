# Hintzen, Joost - 10434143
# Heijningen, Rutger van - 10272224
# Kemmere, Simon - 10798250
#
# Function that runs Dijkstra algorithm and calculates it´s score.
# Data that gets loaded in depends on the configuration chosen in
# main.py.

from Data.datastructuur_graph import Graph
from Python_files.Greedy import run_greedy
import csv
import math
import random
from itertools import chain
import copy
import sys


# class that when called upon calculates the end score
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


# dijkstra greedy algorithm
def dijkstra(begin, holland, p_path, minutes, maps_minutes):

    # instantiate variables/dicts/lists
    shortest_distance = {}
    previous = {}
    unvisited_stations = copy.deepcopy(holland.graph.vert_dict)
    infinity = math.inf
    path = []

    # set all distances in unvisited stations to infinity
    for station in unvisited_stations:
        shortest_distance[station] = infinity
    shortest_distance[begin] = 0

    breaker = False
    while unvisited_stations:

        # if no next station is given, i.e., first iteration
        # get begin station from method
        min_node = None
        for node in unvisited_stations:
            if min_node is None:
                min_node = node

            # else next station is begin station
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node


        for neighbor, distance in holland.graph.vert_dict[min_node].adjacent.items():

            if distance + shortest_distance[min_node] < shortest_distance[neighbor.id]:
                shortest_distance[neighbor.id] = distance + shortest_distance[min_node]
                previous[neighbor.id] = min_node
                goal = previous[neighbor.id]

            # determine whether total distance from begin station
            # will exceed time constraint
            if shortest_distance[neighbor.id] > maps_minutes:

                # if so pop last added station
                shortest_distance.pop(neighbor.id)

                # set goal to station before lastly added station
                goal = previous[neighbor.id]
                breaker = True

                # break out of forloop
                break

        # pop station from unvisited_stations, because visited
        unvisited_stations.pop(min_node)

        # if breaker was set to true, break out of while loop
        if breaker:
            break

    # paste all connections after another to create path of train
    current = goal
    while current != begin:

        try:
            connection = []
            connection.insert(0, current)
            current = previous[current]
            connection.insert(0, current)
            path.insert(0, connection)

        except KeyError:
            print("path not reachable")
            break

    # append to p_path to get p
    p_path.append(path)


    # make list of minutes per trajectory
    minutes.append(shortest_distance[current])
