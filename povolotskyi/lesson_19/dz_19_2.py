import networkx as nx
import matplotlib.pyplot as plt

with open("cities.csv") as file:
    text = file.read().splitlines()

db = []
for i in range(len(text)):
    text_string = text[i]
    new_element = text_string.split(';')
    third_to_int = int(new_element.pop())
    new_element.append(third_to_int)
    db.append(new_element)

g = nx.Graph()
for edge in db:
    g.add_edge(edge[0], edge[1], weight = edge[2])

def search_route(graph, first_point, second_point):
    route = nx.shortest_path(graph, first_point, second_point, weight='weight')
    route_length = nx.shortest_path_length(graph, first_point, second_point, weight='weight')
    return route, route_length

print(search_route(g, 'Zaporizhzhia', 'Kyiv'))