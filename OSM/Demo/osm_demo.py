import Klassen as KL
import matplotlib.pyplot as plt

# erstelle einen Knoten mit folgendem Aufruf:
node = KL.Knoten(7.78, 49.44, 123)
# zeige die Infos auf dem Bildschirm an
print(node)

# Liste von Knoten

nodes = [KL.Knoten(7.78, 49.44, 312),
     KL.Knoten(7.8, 49.6, 844),
     KL.Knoten(7.9, 49.8, 853),
     KL.Knoten(8.0, 49.3, 934),
     KL.Knoten(7.6, 50, 475)]


# mit folgendem Befehl kann man eine Kante erstellen
edge = KL.Kanten(nodes[0], nodes[1])


# Zusatz: Netzwerkk toolbox
import networkx as nx
G = nx.DiGraph()

G.add_node(0, data=nodes[0])
G.add_node(1, data=nodes[1])
G.add_node(2, data=nodes[2])
G.add_node(3, data=nodes[3])
G.add_node(4, data=nodes[4])

G.add_edges_from([(0,1)])

G.add_edges_from([(1, 3),(1, 6), (2,5), (5,6), (4,6)])
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
