import csv
import math
import random
from critical_connections_simon import check_list
from itertools import chain
import copy

class Station:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, distance=0):
        self.adjacent[neighbor] = distance

    def get_connections(self):
        return self.adjacent.keys()

    def get_graph(self):
        return self.adjacent

    def get_id(self):
        return self.id

    def get_distance(self, neighbor):
        return self.adjacent[neighbor]

    def __iter__(self):
        return iter(self.adjacent.values())


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_stations = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_station(self, node):
        self.num_stations = self.num_stations + 1
        if node not in self.vert_dict:
            new_station = Station(node)
            self.vert_dict[node] = new_station
            return new_station
        else:
            return None

    def get_station(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_connection(self, frm, to, distance = 0, number=-1):
        if frm not in self.vert_dict:
            self.add_station(frm)
        if to not in self.vert_dict:
            self.add_station(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], distance)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], distance)

    def get_stations(self):
        return self.vert_dict.keys()

class Score:
    def __init__(self, p, train, min):
        self.p = p
        self.train = train
        self.min = min

    def get_score(self):
        return self.p*10000 - (self.train*20 + self.min/10)


# making new graph
g = Graph()


# loading in stations and connections
with open('C:/Users/TU Delf SID/Documents/GitHub/railNL/Data/ConnectiesHolland.csv', 'r') as csvfile:
    nlreader = csv.reader(csvfile)
    for row in nlreader:
        g.add_station(row[0])
        g.add_station(row[1])
        g.add_connection(row[0], row[1], int(row[2]))


# greedy algorithm
def greedy(begin):

    # extract all connections and stations
    stations = copy.deepcopy(g.vert_dict)
    infinity = math.inf
    path = []

    #set values to variables
    breaker = False
    min_node = None
    station = None
    tot_dist = 0
    trajectlist = []

    # initiate loop where greedy paths are made
    while True:

        # instantiate beginstation
        if min_node is None:
            min_node = stations[begin]

        # else use last station as beginstation
        else:
            min_node = station

        # keep track of all neighbors
        neighbor_dict = {}

        # look up neighbors and distance from beginstation
        for neighbor, distance in stations[min_node.id].adjacent.items():

            #if neighbor is None:
               #trajectlist.append(min_node.id)
               #breaker = True
               #break
            # if unvisited_stations[station]

            # add dictionary of beginstation with neighboring station and distance
            neighbor_dict.update({neighbor: distance})

            station = min(neighbor_dict.items(), key=lambda x:x[1])[0]
            distance = min(neighbor_dict.items(), key=lambda x:x[1])[1]


        if breaker:
            break

        # if max distance is not reach append station for path
        if  tot_dist + distance < 121:
            trajectlist.append(min_node.id)

        # distance reached is maxed stop loop
        else:
            break

        # add distance to next station to total distance
        tot_dist += distance

        # set distance to infinity as to prevent backtracking
        stations[min_node.id].adjacent[station] = infinity
        stations[station.id].adjacent[min_node] = infinity

    # add from and to station in path list
    counter = 1
    for i in trajectlist[:-1]:
        path.insert(0, [trajectlist[counter], i])
        counter += 1

    # append path to as to get all paths
    p_path.append(path)

    # get total minutes per train
    minutes.append(tot_dist)

score_list = []
list_stations = []
score_max = 0

# open csv containing all stations in Holland and append to list
with open('C:/Users/TU Delf SID/Documents/GitHub/railNL/Data/StationsHolland.csv', 'r') as stationsfile:
    stationreader = csv.reader(stationsfile)
    for row in stationreader:
        list_stations.append(row[0])

# the amount times the greedy algorithm runs
for j in range(1):

    # reset all lists after all trains are run
    p_path = []
    minutes = []
    lijst = []
    path_list = []
    p_list = []

    # create number of wanted trajectories
    for i in range(5):

        # choose random station from all possible stations
        station = random.choice(list_stations)

        # append chosen station to list
        lijst.append(station)

        # remove station from all possible stations list
        list_stations.remove(station)

        # call greedy algorithm
        greedy(station)

    # add removed stations back to all possible stations
    list_stations.extend(lijst)

    # show amount of iterations
    print(j)

    # unlist wanted amount of paths
    p_list = list(chain.from_iterable(p_path))

    print(p_list)
    print("&"*10)
    print(p_path)

    # make tuple of every connection in a path
    path_list = list(map(tuple,p_list))

    # make set to filter amount of unqiue connections
    uniq = set()
    for s in path_list:
        if not (s in uniq or (s[1], s[0]) in uniq):
            uniq.add(s)

    # calculate p via amount ridden connections
    p = len(list(uniq))/28

    # determine score
    score_greedy = Score(p, 5, sum(minutes)).get_score()

    # keep track of the highest score and  corresponding path is
    if score_greedy > score_max:
            score_max = score_greedy
            final_track = p_path

    # insert all scores in to a list
    score_list.insert(0, score_greedy)

# Visualize path for every train and the total max score
train_count = 1
for i in final_track:
    print("")
    print ("Traject of train", train_count)
    for j in i:
        print(j)
    train_count += 1
print("")
print("The score of these trajectories account for", score_max, "points")
