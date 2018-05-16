import csv
import math


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

    def get_graph(self):
        return self.adjacent

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

    # dijkstra greedy algorithm
    def dijkstra(graph, begin):
        #goal = None
        shortest_distance = {}
        previous = {}
        unvisited_stations = graph.vert_dict
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


            for neighbor, distance in graph.vert_dict[min_node].adjacent.items():

                if distance + shortest_distance[min_node] < shortest_distance[neighbor.id]:
                    shortest_distance[neighbor.id] = distance + shortest_distance[min_node]
                    previous[neighbor.id] = min_node
                #print(neighbor.id)
                if shortest_distance[neighbor.id] > 120:
                    shortest_distance.pop(neighbor.id)
                    # previous.pop(neighbor.id)
                    #print(neighbor.id)
                    #print(previous)
                    goal = previous[neighbor.id]
                    print(goal)
                    breaker = True
                    break
                #elif :

                print(goal)
            if breaker:
                break

            unvisited_stations.pop(min_node)


        current = goal
        while current != begin:
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


    # calling of dijkstra algorithm
    dijkstra(g, "Amsterdam Centraal")
    print("DONE")
