import numpy as np

def get_node_lat_lon(root):
    node_lat_lon = dict()
    for node in root.findall('node'):
        nodeID = node.get('id')
        Breitengrad = node.get('lat')
        Laengengrad = node.get('lon')
        node_lat_lon[nodeID] = [Breitengrad, Laengengrad]

    return node_lat_lon

def get_ways(root):
    ways = dict()
    for way in root.findall('way'):
        wayID = way.get('id')
        tmp = way.getchildren()
        nodes = []
        for t in tmp:
            if t.keys()[0] == 'ref':
                nodes.append(t.get('ref'))
        ways[wayID] = nodes
    return ways
 
