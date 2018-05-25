from Data.datastructuur_graph import Graph
from Python_files.Greedy import run_greedy
import csv
import math
import random
from itertools import chain
import copy
import sys


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


# dijkstra greedy algorithm
def dijkstra(begin, holland, p_path, minutes):


    shortest_distance = {}
    previous = {}
    unvisited_stations = copy.deepcopy(holland.graph.vert_dict)
    infinity = math.inf
    path = []

    for station in unvisited_stations:
        shortest_distance[station] = infinity
    shortest_distance[begin] = 0

    breaker = False
    while unvisited_stations:
        min_node = None
        for node in unvisited_stations:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node


        for neighbor, distance in holland.graph.vert_dict[min_node].adjacent.items():

            if distance + shortest_distance[min_node] < shortest_distance[neighbor.id]:
                shortest_distance[neighbor.id] = distance + shortest_distance[min_node]
                previous[neighbor.id] = min_node
                goal = previous[neighbor.id]


            if shortest_distance[neighbor.id] > 180:
                shortest_distance.pop(neighbor.id)

                goal = previous[neighbor.id]
                breaker = True
                break

        unvisited_stations.pop(min_node)

        if breaker:
            break

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
