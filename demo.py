import xml.etree.ElementTree as ET
import numpy as np
import sys
import tools
import leaflettools as lt

tree = ET.parse('map_large.osm')
root = tree.getroot()

node_lat_lon = tools.get_node_lat_lon(root)
ways = tools.get_ways(root)
#np.save('Nodes.npy', node_lat_lon)
#np.save('Ways.npy',ways)
#node_lat_lon = np.load('Nodes.npy').item()
#node_lat_lon = np.load('Ways.npy').item()


sys.getsizeof(ways)
sys.getsizeof(node_lat_lon)

# Linie 115 finden
Linie115 = []
for rel in root.findall('relation'):
    tmp = rel.getchildren()
    for t in tmp:
        try:
            if t.get('v')=='Bus 115':
                Linie115.append(rel)
        except:
            pass

ways115 = []
for i in Linie115[1].getchildren():
    try:
        if i.get('type') == 'way':
            ways115.append(i.get('ref'))
    except:
        pass

# -----
#somenodes = []
#nodeIDs = ways[ways115[-1]]
#for i in nodeIDs:
#    try:
#        somenodes.append(node_lat_lon[i])
#    except:
#        pass
#
#
#str_aux = lt.latlon2str(somenodes)
#lt.plugin_data2leaflet(str_aux)

allnodes115 = []
for wayID in ways115:
    try:
        print(wayID)
        nodeIDs = ways[wayID]
        for i in nodeIDs:
            try:
                allnodes115.append(node_lat_lon[i])
            except:
                pass
    except:
        pass

str_aux = lt.latlon2str(allnodes115)
lt.plugin_data2leaflet(str_aux)


# ------ old shit ----------------


#print(root.findall('./node'))
#for way in root.findall('way'):
#    tag = way.find('.//tag')
  #  if tag.attrib['k'] == 'bridge' and tag.attrib['v'] == 'yes':
  #      print(tag)



#print(root.tag)
#print(root.attrib)
#print(root[1].tag)
#print(root[1].attrib)
#
#list_of_tags = []
#for element in root:
#    if not element.tag in list_of_tags:
#        list_of_tags.append(element.tag)
#
#print('\n-----------------------\nList of tags: \n')
#print(list_of_tags)

#list_of_node_attributes = []
#for element in root.findall('node'):
#    list_of_node_attributes = list(set(list_of_node_attributes).union(set(element.attrib.keys())))
#
#
#print('\n-----------------------\nList of node attributes: \n')
#print(list_of_node_attributes)

#list_of_way_attributes = []
#for element in root.findall('way'):
#    list_of_way_attributes = list(set(list_of_way_attributes).union(set(element.attrib.keys())))
#
#print('\n-----------------------\nList of way attributes: \n')
#print(list_of_way_attributes)
#
#
#list_of_relation_attributes = []
#for element in root.findall('relation'):
#    list_of_relation_attributes = list(set(list_of_relation_attributes).union(set(element.attrib.keys())))
#
#print('\n-----------------------\nList of relation attributes: \n')
#print(list_of_relation_attributes)
