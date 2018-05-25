import csv
import math
import random
from itertools import chain
from Data.datastructuur_graph import Graph
import copy
import sys
from Python_files.Greedy import run_greedy


class Score:
    def __init__(self, p, train, min):
        self.p = p
        self.train = train
        self.min = min

    def get_score(self):
        return self.p*10000 - (self.train*20 + self.min/10)

class Holland:

    def __init__(self, train, directory):
        self.dir = directory
        self.graph = Graph()
        self.train = train
        self.get_graph(self.dir)

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

    stations = copy.deepcopy(holland.graph.vert_dict)
    infinity = math.inf
    path = []

    breaker = False
    min_node = None
    station = None
    tot_dist = 0
    trajectlist = []
    while True:

        if min_node is None:
            min_node = stations[begin]
        else:
            min_node = station

        neighbor_dict = {}
        for neighbor, distance in stations[min_node.id].adjacent.items():

            neighbor_dict.update({neighbor: distance})

            station = min(neighbor_dict.items(), key=lambda x:x[1])[0]
            distance = min(neighbor_dict.items(), key=lambda x:x[1])[1]

        if breaker:
            break

        if  tot_dist + distance < 181:
            trajectlist.append(min_node.id)
        else:
            break

        tot_dist += distance

        stations[min_node.id].adjacent[station] = infinity
        stations[station.id].adjacent[min_node] = infinity

    counter = 1
    for i in trajectlist[:-1]:
        path.insert(0, [trajectlist[counter], i])
        counter += 1

    # append to p_path to get p
    p_path.append(path)


    # make list of minutes per trajectory
    minutes.append(tot_dist)
