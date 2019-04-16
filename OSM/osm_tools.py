"""Werkzeugkasten zur Verarbeitung von OSM Daten.
https://wiki.openstreetmap.org/wiki/Key:highway
https://stackoverflow.com/questions/14716497/how-can-i-find-a-list-of-street-intersections-from-openstreetmap-data?rq=1
"""

import xml.etree.ElementTree as ET


def load_osm_file(filename):
    """Lade einen OSM-Datensatz ein."""
    tree = ET.parse(filename)
    root = tree.getroot()
    
    return root


def get_node_lat_lon(root):
    """Erstelle Woerterbuch mit allen Knoten und deren Laengen- /Breitengraden"""
    node_lat_lon = dict()
    for node in root.findall('node'):
        nodeID = node.get('id')
        Breitengrad = node.get('lat')
        Laengengrad = node.get('lon')
        node_lat_lon[nodeID] = [Breitengrad, Laengengrad]

    return node_lat_lon



if __name__ == '__main__':
    osm_root = load_osm_file('./HHG-BHF.osm')
    node_lat_lon = get_node_lat_lon(osm_root)
    
    ways = osm_root.findall('way')  # List mit Weg Elementen
    
    # ein Weg Element hat Eigenschaften und wiederum Kinder
#    <way id="14357125" visible="true" version="26" changeset="56091012" timestamp="2018-02-05T17:37:29Z" user="devbrain" uid="58073">
#  <nd ref="139466306"/>
#  <nd ref="1201451389"/>
#  <tag k="cycleway" v="lane"/>
#  <tag k="highway" v="primary"/>
#  <tag k="maxspeed" v="50"/>
#  <tag k="name" v="Eisenbahnstraße"/>
#  <tag k="ref" v="B 37"/>
#  <tag k="surface" v="asphalt"/>
# </way>
    einWeg = ways[0]
    print(einWeg.get('id'))
    print(einWeg.get('timestamp'))
    
    Kinder = einWeg.getchildren()
    einKind = Kinder[0]
    einKind.attrib
    einKind.tag
    
    
    