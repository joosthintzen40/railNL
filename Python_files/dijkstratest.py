import math
import csv
#
f = { "b": {"a": 2, "c": 4, "d": 3}, "a": {"b": 2}, "c": {"b": 4,"d": 3}, "d": {"b": 3, "e": 4,"c": 3}, "e": {"d": 4}}



# Load CSV
with open('ConnectiesHolland_test.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile))
totaal = {}

# for i in data:
#     if data[i] in totaal:
#
print(data)
# New dict for all connections

neighbor ={}
# Temp variable
temp_dict = 0

# Loading data in totaal
# for i in data:
#
#     neighbor[data[temp_dict][1]] = data[temp_dict][2]
#
#     temp_dict += 1
# for i in neighbor:
#     print(i)
#
# print(neighbor)
#print(totaal)


def dijkstra(graph, begin, goal):
  shortest_distance = {}
  previous = {}
  unvisited_stations = graph #.vert_dict
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
      #print(shortest_distance)
      print(node)
      print("##")
      print(min_node)


      #print(unvisited_stations)

      # for nodes in graph:
      for neighbor, distance in graph[min_node].items():#.adjacent.items():
          #print("distance from {} to {} is {}".format(nodes, neighbor, distance))
          # if distance < shortest_distance[min_node]:
          #     shortest_distance[min_node] = distance
          #     previous[min_node] = neighbor
          #     distance += shortest_distance[min_node]
          print(neighbor)
          print(distance)
          if distance + shortest_distance[min_node] < shortest_distance[neighbor]:
              shortest_distance[neighbor] = distance + shortest_distance[min_node]
              previous[neighbor] = min_node
              print("#"*30)
      #print(previous)
      unvisited_stations.pop(min_node)
      print("#")
  #print(shortest_distance)
  current = goal
  while current != begin:
      #print(current)
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

dijkstra(f, "a", 'c')
print("DONE")
