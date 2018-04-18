# import csv data

import csv
from collections import defaultdict

def main():
    # graph = Graph()
    # with open('ConnectiesHolland.csv', 'r') as connecties_holland:
    #     nlreader =  csv.reader(connecties_holland)
    #     for station in nlreader:
    #         graph.add_edge(*station)



    noordholland = []
    g = Graph()
    noordholland.append([g.add_node('Alkmaar', 1)])
    noordholland.append([g.add_node('Hoorn', 0)])
    print(noordholland)


class Graph:
    def __init__(self):
        self.nodes = defaultdict(list)
        self.edges = defaultdict(list)
        self.distances = {}
        self.weight = {}

    def add_node(self, station, weight):
        self.nodes[station] = weight

    def add_edge(self, begin, end, distance):
        self.edges[begin].append(end)
        self.edges[end].append(begin)
        self.distances[(begin, end)] = distances


if __name__ == "__main__":
    main()
