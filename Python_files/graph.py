import csv
import math

# class trajections:
#     def __init__(self):
#         g = Graph()
#         with open('ConnectiesHolland.csv', 'r') as csvfile:
#             nlreader = csv.reader(csvfile)
#             for row in nlreader:
#                 g.add_station(row[0])
#                 g.add_station(row[1])
#                 g.add_connection(row[0], row[1], int(row[2]))
#         self.trajections = []
#
#     def tree(self, begin, totdistance=0):
#         for v in g:
#             if v == begin:
#                 for w in v.get_connections():
#

    #
    #
    # def find(self, node, i):
    #     if node[i] == i:
    #         return
    #     return self.find(node, node[i])


class Station:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' is adjacent to: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, distance=0):
        self.adjacent[neighbor] = distance

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_distance(self, neighbor):
        return self.adjacent[neighbor]

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

    def add_connection(self, frm, to, distance = 0):
        if frm not in self.vert_dict:
            self.add_station(frm)
        if to not in self.vert_dict:
            self.add_station(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], distance)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], distance)

    def get_stations(self):
        return self.vert_dict.keys()


if __name__ == '__main__':

    # making new graph
    g = Graph()

    # loading in stations and connections
    with open('ConnectiesHolland.csv', 'r') as csvfile:
        nlreader = csv.reader(csvfile)
        for row in nlreader:
            g.add_station(row[0])
            g.add_station(row[1])
            g.add_connection(row[0], row[1], int(row[2]))


    # presentation of all possible connections and distances of map
    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print ('( %s, %s, %3d)'  % ( vid, wid, v.get_distance(w)))

    # presentation of all stations and their neighboring stations
    # for v in g:
    #     print ('%s' %(g.vert_dict[v.get_id()]))

    def dijkstra(graph, begin, goal):
        shortest_distance = {}
        previous = {}
        unvisited_stations = graph.vert_dict
        infinity = math.inf
        path = []

        #print(unvisited_stations)
        for station in unvisited_stations:
            shortest_distance[station] = infinity
        shortest_distance[begin] = 0
        #print(shortest_distance)
        while unvisited_stations:
            min_node = None
            for node in unvisited_stations:
                if min_node is None:
                    min_node = node
                elif shortest_distance[node] < shortest_distance[min_node]:
                    min_node = node
            print(unvisited_stations)

            for nodes in graph:
                for neighbor, distance in nodes.adjacent.items():
                    #print("distance from {} to {} is {}".format(nodes, neighbor, distance))
                    # if distance < shortest_distance[min_node]:
                    #     shortest_distance[min_node] = distance
                    #     previous[min_node] = neighbor
                    #     distance += shortest_distance[min_node]
                    #     print(previous)
                    if distance + shortest_distance[min_node] < shortest_distance[neighbor]:
                        shortest_distance[neighbor] = distance + shortest_distance[min_node]
                        previous[neighbor] = min_node
                        print(previous)
            #print(previous)
            unvisited_stations.pop(min_node)

        #print(shortest_distance)
        current = goal
        while current != begin:
            print(current)
            try:
                path.insert(0, current)
                current = previous[current]
            except KeyError:
                print("path not reachable")
                break

        path.insert(0, begin)
        if shortest_distance[goal] != infinity:
            print("shortest distance is " + str(shortest_distance[goal]))
            print("the path is" + str(path))

    dijkstra(g, 'Den Helder', 'Amsterdam Centraal')
    print("DONE")
