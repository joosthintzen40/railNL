import csv

class Station:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

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

    def get_connections(self):
        return self.vert_dict


if __name__ == '__main__':

    # making new graph
    g = Graph()
    # s = Station()

    # loading in stations and connections
    with open('ConnectiesHolland.csv', 'r') as csvfile:
        nlreader = csv.reader(csvfile)
        for row in nlreader:
            g.add_station(row[0])
            g.add_station(row[1])
            g.add_connection(row[0], row[1], int(row[2]))


    # #presentation of all possible connections and distances of map
    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print ('( %s, %s, %3d)'  % ( vid, wid, v.get_distance(w)))
    #
    # # presentation of all stations and their neighboring stations
    # for v in g:
    #     print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
    #

    vid = [0].get_id()
    wid = [0].get_id()
    w = [0].get_connections():
        print ('( %s, %s, %3d)'  % ( vid, wid, [0].get_distance([0])))

    print(g.vert_dict["Alkmaar"])
    print(

    print(
