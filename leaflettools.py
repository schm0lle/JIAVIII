def latlon2str(latlon):
    stringlist = []
    strstart = 'var marker = L.marker(['
    strend = ']).addTo(map);'
    for coordinate in latlon:
        stringlist.append(strstart + str(coordinate[0]) + ', ' + str(coordinate[1]) + strend)

    return stringlist


def plugin_data2leaflet(stringlisttoplugin):
    f1 = open('./leaflet_template.html', 'r')
    f2 = open('./leaflet_file_filled.html', 'w')
    for line in f1:
        content = line.split(" ")
        try:
            if content[1] == 'plugin':
                for s in stringlisttoplugin:
                    f2.write(s)
            else:
                f2.write(line)
        except:
            f2.write(line)
    f1.close()
    f2.close()
