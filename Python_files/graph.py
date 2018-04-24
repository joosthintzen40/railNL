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
        new_station = Station(node)
        self.vert_dict[node] = new_station
        return new_station

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

    g = Graph()
    # g.add_station('a')
    # g.add_station('b')
    # g.add_station('c')
    # g.add_station('d')
    # g.add_station('e')
    # g.add_station('f')
    #
    # g.add_connection('a', 'b', 7)
    # g.add_connection('a', 'c', 9)
    # g.add_connection('a', 'f', 14)
    # g.add_connection('b', 'c', 10)
    # g.add_connection('b', 'd', 15)
    # g.add_connection('c', 'd', 11)
    # g.add_connection('c', 'f', 2)
    # g.add_connection('d', 'e', 6)
    # g.add_connection('e', 'f', 9)
    with open('ConnectiesHolland.csv', 'r') as csvfile:
        nlreader = csv.reader(csvfile)

        for row in nlreader:
            g.add_station(row[0])
            g.add_station(row[1])
        for row in nlreader:
            g.add_connection(row[0], row[1], int(row[2]))

        #print(g.get_stations())



    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s, %s, %3d)'  % ( vid, wid, v.get_distance(w)))

    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
