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

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Random Graph Generation Example")
plt.show()