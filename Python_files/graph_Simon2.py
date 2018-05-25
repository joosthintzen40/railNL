import csv
import math
import random
from critical_connections_simon import check_list
from itertools import chain
import copy
<<<<<<< HEAD
import sys
=======
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76

class Station:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

<<<<<<< HEAD
=======
    def __str__(self):
        return str(self.id) + ' is adjacent to: ' + str([x.id for x in self.adjacent])

>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
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
<<<<<<< HEAD

=======
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
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

class Holland:
<<<<<<< HEAD
    def __init__(self, maps, train):
        self.dir1 = 'C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/ConnectiesHolland.csv'
        self.dir2 = 'C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/ConnectiesNationaal.csv'
        self.graph = Graph()
        self.train = train
        self.maps = maps
        self.which_map()
        

    def get_graph(self, dir):
        with open(dir, 'r') as csvfile:
=======
    def __init__(self):
        self.dir = 'C:/Users/TU Delf SID/Documents/GitHub/railNL/Data/ConnectiesHolland.csv'
        self.graph = Graph()
        self.get_graph()



    def get_graph(self):
        with open(self.dir, 'r') as csvfile:
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
            nlreader = csv.reader(csvfile)
            for row in nlreader:
                self.graph.add_station(row[0])
                self.graph.add_station(row[1])
                self.graph.add_connection(row[0], row[1], int(row[2]))
        return self.graph

<<<<<<< HEAD
    def which_map(self):
        if self.maps == 'Noord Holland':
            self.get_graph(self.dir1)
        elif self.maps == 'Nationaal':
            self.get_graph(self.dir2)
        else:
            print('No valid load-file selected!')
            sys.exit()







trains = 5
maps = 'Nationaal'
holland = Holland(maps, trains)
=======


    # def add_train(self):



# class Nationaal:

# for v in g:
#     for w in v.get_connections():
#         vid = v.get_id()
#         wid = w.get_id()
#         print('( %s , %s, %3d)'  % ( vid, wid, v.get_distance(w)))

#
# for v in g:
#     print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

# making new graph
# g = Graph()
#
#
# # loading in stations and connections
# with open('C:/Users/TU Delf SID/Documents/GitHub/railNL/Data/ConnectiesHolland.csv', 'r') as csvfile:
#     nlreader = csv.reader(csvfile)
#     for row in nlreader:
#         g.add_station(row[0])
#         g.add_station(row[1])
#         g.add_connection(row[0], row[1], int(row[2]))

holland = Holland()
print(holland)
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76

# greedy algorithm
def greedy(begin):

<<<<<<< HEAD
    stations = copy.deepcopy(holland.graph.vert_dict)
=======
    stations = copy.deepcopy(holland.vert_dict)
    # unvisited_stations = copy.deepcopy(holland.vert_dict)
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
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

<<<<<<< HEAD
=======
            #if neighbor is None:
               #trajectlist.append(min_node.id)
               #breaker = True
               #break
            # if unvisited_stations[station]

>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
            neighbor_dict.update({neighbor: distance})

            station = min(neighbor_dict.items(), key=lambda x:x[1])[0]
            distance = min(neighbor_dict.items(), key=lambda x:x[1])[1]

<<<<<<< HEAD
=======

>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
        if breaker:
            break

        if  tot_dist + distance < 181:

<<<<<<< HEAD
=======

>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
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

<<<<<<< HEAD
    # append to p_path to get p
    p_path.append(path)

    #print(path)
=======

    # if tot_dist != infinity:
    #     print("shortest distance is " + str(tot_dist))
    #     print("the path is" + str(path))

    # append to p_path to get p
    p_path.append(path)

>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76

    # make list of minutes per trajectory
    minutes.append(tot_dist)












score_list = []
list_stations = []
score_max = 0

<<<<<<< HEAD
with open('C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/StationsHolland.csv', 'r') as stationsfile:
=======
with open('C:/Users/TU Delf SID/Documents/GitHub/railNL/Data/StationsHolland.csv', 'r') as stationsfile:
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
    stationreader = csv.reader(stationsfile)
    for row in stationreader:
        list_stations.append(row[0])


<<<<<<< HEAD
for j in range(10000):
=======
for j in range(1000):
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
    p_path = []
    minutes = []
    lijst = []
    path_list = []
    p_list = []


<<<<<<< HEAD
    for i in range(holland.train):
=======
    for i in range(5):
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
        station = random.choice(list_stations)
        lijst.append(station)
        list_stations.remove(station)
        greedy(station)

    list_stations.extend(lijst)

<<<<<<< HEAD
    sys.stdout.write("\riteration: %i" %(j))
    sys.stdout.flush()
=======

    print(j)
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
    p_list = list(chain.from_iterable(p_path))


    path_list = list(map(tuple,p_list))
    uniq = set()
    for s in path_list:
        if not (s in uniq or (s[1], s[0]) in uniq):
            uniq.add(s)

    p = len(list(uniq))/28
<<<<<<< HEAD
    score_greedy = Score(p, holland.train, sum(minutes)).get_score()
=======
    score_greedy = Score(p, 5, sum(minutes)).get_score()
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76


    if score_greedy > score_max:
            score_max = score_greedy
            final_track = p_path

    score_list.insert(0, score_greedy)

<<<<<<< HEAD
train_count = 1
for i in final_track:
    print("")
    print ("Traject of train", train_count)
    for j in i:
        print(j)
    train_count += 1
print("")
print("The score of these trajectories account for", score_max, "points")
=======
print(score_max, final_track)

print("DONE")
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
