destination_displacement = {'a': 65,
                          'b': 80,
                          'c': 95,
                          'd': 87,
                          'e': 90,
                          'f': 75,
                          'g': 55,
                          'h': 45,
                          'i': 47,
                          'j': 45,
                          'k': 22,
                          'l': 0,
                          'm': 25}

maps =        { 'a':  [['g', 15, destination_displacement['g']],
                       ['e', 25, destination_displacement['e']],
                       ['b', 15, destination_displacement['b']],
                       ['h', 45, destination_displacement['h']]],
                'b':  [['c', 20, destination_displacement['c']],
                       ['i', 30, destination_displacement['i']]],
                'c':  [['b', 20, destination_displacement['b']],
                       ['d', 10, destination_displacement['d']]],
                'd':  [['c', 10, destination_displacement['c']],
                       ['e', 5, destination_displacement['e']]],
                'e':  [['f', 10, destination_displacement['f']],
                       ['a', 25, destination_displacement['a']],
                       ['d', 5, destination_displacement['d']]],
                'f':  [['g', 20, destination_displacement['g']],
                       ['e', 10, destination_displacement['e']]],
                'g':  [['f', 20, destination_displacement['f']],
                       ['a', 15, destination_displacement['a']],
                       ['h', 50, destination_displacement['h']]],
                'h':  [['g', 50, destination_displacement['g']],
                       ['m', 25, destination_displacement['m']],
                       ['i', 50, destination_displacement['i']],
                       ['a', 45, destination_displacement['a']]],
                'i':  [['h', 50, destination_displacement['h']],
                       ['b', 30, destination_displacement['b']],
                       ['j', 30, destination_displacement['j']]],
                'j':  [['k', 40, destination_displacement['k']],
                       ['i', 30, destination_displacement['i']]],
                'k':  [['j', 40, destination_displacement['j']],
                       ['l', 35, destination_displacement['l']]],
                'l':  [['m', 25, destination_displacement['m']],
                       ['k', 35, destination_displacement['k']]],
                'm':  [['l', 25, destination_displacement['l']],
                       ['h', 25, destination_displacement['h']]]}


from pprint import pprint

source = 'e'
destination = 'l'

def min_active_node_index(active_nodes):
  temp_min_sum_list = [i[1]+i[2] for i in active_nodes]
  return temp_min_sum_list.index(min(temp_min_sum_list))


def expand(active_nodes, min_node_index, count, parent_list):
  min_node_name = active_nodes[min_node_index][0]
  parent_list += active_nodes[min_node_index][0]

  with open('output.txt', 'a') as out:
      pprint(count, stream=out)
      pprint(min_node_name, stream=out)
      # pprint(parent_list, stream=out)

  next_active_nodes = maps[min_node_name]
  min_node_gn = active_nodes[min_node_index][1]

  del active_nodes[min_node_index]

  for i in next_active_nodes:
    i[1] = min_node_gn + i[1]
    # removing degrees of parent check results in sub-optimal routes
    # if (i[0] != parent_list[-1] and i[0] != parent_list[-2]):
    if (i[0] != parent_list[-1] and i[0] != parent_list[-2] and i[0] != parent_list[-3]):
      active_nodes.insert(min_node_index,i)


def aStar(source, destination):
  parent_list = [source, source]
  count = 0;
  active_nodes = [[source, 0, destination_displacement[source]]]
  min_node_index = min_active_node_index(active_nodes)
  # out_file = "bigintlist.txt"
  # afile = open(out_file, "w")

  while active_nodes[min_node_index][0] != destination:
    count+=1
    expand(active_nodes, min_node_index, count, parent_list)
    with open('output.txt', 'a') as out:
      pprint(active_nodes, stream=out)
      out.write("\n")
      # pprint('\nzz\n', stream=out)
    min_node_index = min_active_node_index(active_nodes)


aStar(source, destination)
