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

    def __init__(self, maps, train):
        self.dir1 = 'C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/ConnectiesHolland.csv'
        self.dir2 = 'C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/ConnectiesNationaal.csv'
        self.graph = Graph()
        self.train = train
        self.maps = maps
        self.which_map()

    def get_graph(self, dir):
        with open(dir, 'r') as csvfile:

            nlreader = csv.reader(csvfile)
            for row in nlreader:
                self.graph.add_station(row[0])
                self.graph.add_station(row[1])
                self.graph.add_connection(row[0], row[1], int(row[2]))
        return self.graph


    def which_map(self):
        if self.maps == 'Noord Holland':
            self.get_graph(self.dir1)
        elif self.maps == 'Nationaal':
            self.get_graph(self.dir2)
        else:
            print('No valid load-file selected!')
            sys.exit()


# greedy algorithm
def greedy(begin):


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

    # append to p_path to get p
    p_path.append(path)

    # make list of minutes per trajectory
    minutes.append(tot_dist)


score_list = []
list_stations = []
score_max = 0

with open('C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/StationsHolland.csv', 'r') as stationsfile:
    stationreader = csv.reader(stationsfile)
    for row in stationreader:
        list_stations.append(row[0])

for j in range(10000):

    p_path = []
    minutes = []
    lijst = []
    path_list = []
    p_list = []

    for i in range(holland.train):
        station = random.choice(list_stations)
        lijst.append(station)
        list_stations.remove(station)
        greedy(station)

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
    score_greedy = Score(p, holland.train, sum(minutes)).get_score()

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
