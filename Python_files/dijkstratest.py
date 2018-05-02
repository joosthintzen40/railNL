f = {"a": {"b": 2, "c": 3}, "b": {"a": 2, "c": 4}, "c": {"a":3,"b": 4}}

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
      print(unvisited_stations)

      # for nodes in graph:
      for neighbor, distance in graph[min_node].items():#.adjacent.items():
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

dijkstra(f, "a", 'c')
print("DONE")
