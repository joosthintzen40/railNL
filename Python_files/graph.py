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

    #def __str__(self):


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
    with open('ConnectiesHolland.csv', 'r') as csvfile:
        nlreader = csv.reader(csvfile)

        for row in nlreader:
            g.add_station(row[0])
            g.add_station(row[1])
            g.add_connection(row[0], row[1], int(row[2]))
            print(row[0])
            print(row[1])


            #lists.append(row)
            #g.add_vertex(lists)

            #list.append(lists)
        #print(g.get_edges())

        # for v in g:
        #     for w in v.get_connections():
        #         vid = v.get_id()
        #         wid = w.get_id()
        #         print ('( %s , %s, %3d)'  % ( vid, wid, v.get_distance(w)))

        for v in g:
            print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

        #print(g.get_edges())

    # g = Graph()
    #
    # g.add_vertex('den helder')
    # g.add_edge('den helder', 'alkmaar', 36)
    #
    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
