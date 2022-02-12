destination_displacement = {'Arad': 366,
                          'Bucharest': 0,
                          'Craiova': 160,
                          'Dobreta': 242,
                          'Eforie': 161,
                          'Fagaras': 176,
                          'Giurgui': 77,
                          'Hirsova': 151,
                          'Iasi': 226,
                          'Lugoj': 244,
                          'Mehadia': 241,
                          'Neamt': 234,
                          'Oradea': 380,
                          'Pitesti': 100,
                          'Riminu Vilcea': 193,
                          'Sibiu': 253,
                          'Timisoara': 329,
                          'Urziceni': 80,
                          'Vaslui': 199,
                          'Zerind': 374}

maps =        {'Oradea':  [['Zerind', 71, 374],
                           ['Sibiu', 151, 253]],
             'Zerind':    [['Oradea', 71, 380],
                           ['Arad', 75, 366]],
             'Arad'  :    [['Zerind', 75, 374],
                           ['Sibiu', 140, 253],
                           ['Timisoara', 118, 329]],
             'Timisoara': [['Arad', 118, 366],
                           ['Lugoj', 111, 244]],
             'Lugoj':     [['Timisoara', 111, 329],
                           ['Mehadia', 70, 241]],
             'Mehadia':   [['Lugoj', 70, 244],
                           ['Dobreta', 75, 242]],
             'Dobreta':   [['Mehadia', 75, 241],
                           ['Craiova', 120, 160]],
             'Sibiu':     [['Oradea', 151, 380],
                           ['Arad', 140, 366],
                           ['Riminu Vilcea', 80, 193],
                           ['Fagaras', 99, 176]],
             'Riminu Vilcea': [['Sibiu', 80, 253],
                           ['Pitesti', 97, 100],
                           ['Craiova', 146, 160]],
             'Craiova':   [['Dobreta', 120, 242],
                           ['Riminu Vilcea', 146, 193],
                           ['Pitesti', 138, 100]],
             'Pitesti':   [['Bucharest', 101, 0],
                           ['Riminu Vilcea', 97, 193],
                           ['Craiova', 138, 160]],
             'Fagaras':   [['Sibiu', 99, 253],
                           ['Bucharest', 211, 0]],
             'Bucharest': [['Urziceni', 85, 80],
                           ['Giurgui', 90, 77],
                           ['Pitesti', 101, 100],
                           ['Fagaras', 211, 176]],
             'Giurgui':   [['Bucharest', 90, 0]],
             'Neamt':     [['Iasi', 87, 226]],
             'Iasi':      [['Neamt', 87, 234],
                           ['Vaslui', 92, 199]],
             'Vaslui':    [['Iasi', 92, 226],
                           ['Urziceni', 142, 80]],
             'Urziceni':  [['Bucharest', 85, 0],
                           ['Vaslui', 142, 199],
                           ['Hirsova', 98, 151]],
             'Hirsova':   [['Urziceni', 98, 80],
                           ['Eforie', 86, 161]],
             'Eforie':    [['Hirsova', 86, 151]]}

map_graph = {'Oradea':    [['Zerind', 71],
                           ['Sibiu', 151]],
             'Zerind':    [['Oradea', 71],
                           ['Arad', 75]],
             'Arad'  :    [['Zerind', 75],
                           ['Sibiu', 140],
                           ['Timisoara', 118]],
             'Timisoara': [['Arad', 118],
                           ['Lugoj', 111]],
             'Lugoj':     [['Timisoara', 111],
                           ['Mehadia', 70]],
             'Mehadia':   [['Lugoj', 70],
                           ['Dobreta', 75]],
             'Dobreta':   [['Mehadia', 75],
                           ['Craiova', 120]],
             'Sibiu':     [['Oradea', 151],
                           ['Arad', 140],
                           ['Riminu Vilcea', 80],
                           ['Fagaras', 99]],
             'Riminu Vilcea': [['Sibiu', 80],
                           ['Pitesti', 97],
                           ['Craiova', 146]],
             'Craiova':   [['Dobreta', 120],
                           ['Riminu Vilcea', 146],
                           ['Pitesti', 138]],
             'Pitesti':   [['Bucharest', 101],
                           ['Riminu Vilcea', 97],
                           ['Craiova', 138]],
             'Fagaras':   [['Sibiu', 99],
                           ['Bucharest', 211]],
             'Bucharest': [['Urziceni', 85],
                           ['Giurgui', 90],
                           ['Pitesti', 101],
                           ['Fagaras', 211]],
             'Giurgui':   [['Bucharest', 90]],
             'Neamt':     [['Iasi', 87]],
             'Iasi':      [['Neamt', 87],
                           ['Vaslui', 92]],
             'Vaslui':    [['Iasi', 92],
                           ['Urziceni', 142]],
             'Urziceni':  [['Bucharest', 85],
                           ['Vaslui', 142],
                           ['Hirsova', 98]],
             'Hirsova':   [['Urziceni', 98],
                           ['Eforie', 86]],
             'Eforie':    [['Hirsova', 86]]}

source = 'Arad'
destination = 'Bucharest'

def getNeighbours(node):
  return [i[0] for i in map_graph[node]]

def getNodeDisplacements(nodes):
  return [destination_displacement[i] for i in nodes]

def getNeighbourWithMinDisplacement(node):
  neighbouring_nodes = getNeighbours(node);
  neighbour_displacements = getNodeDisplacements(neighbouring_nodes)
  return neighbouring_nodes[neighbour_displacements.index(min(neighbour_displacements))]

def greedyBFS(source, destination):
  current_node = source
  destination = destination
  while (current_node != destination):
    print(current_node)
    print("↓")
    current_node = getNeighbourWithMinDisplacement(current_node)
  print(current_node)

# greedyBFS(source, destination)
# e-f, b-i don't satisfy distance heuristic
def min_active_node_index(active_nodes):
  temp_min_sum_list = [i[1]+i[2] for i in active_nodes]
  return temp_min_sum_list.index(min(temp_min_sum_list))

def expand(active_nodes, min_node_index):
  min_node_name = active_nodes[min_node_index][0]
  print(min_node_name)
  next_active_nodes = maps[min_node_name]
  min_node_gn = active_nodes[min_node_index][1]
  del active_nodes[min_node_index]

  for i in next_active_nodes:
    i[1] = min_node_gn + i[1]
    active_nodes.insert(min_node_index,i)

from pprint import pprint

def aStar(source, destination):
  active_nodes = [[source, 0, destination_displacement[source]]]
  min_node_index = min_active_node_index(active_nodes)

  while active_nodes[min_node_index][0] != destination:
    expand(active_nodes, min_node_index)
    min_node_index = min_active_node_index(active_nodes)

# greedyBFS(source, destination)
# aStar(source, destination)
