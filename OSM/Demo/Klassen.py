class Knoten:
    def __init__(self, laengengrad, breitengrad, osmID):  # diese Methode wird aufgerufen, wenn ein Knoten erstellt wird
        self.lat = breitengrad
        self.lon = laengengrad
        self.osmID = osmID

    def __str__(self):  #  mit dieser Methode koennt ihr die Bildschirmausgabe formatieren
        return('ID: %d,\nlat: %.4f,\nlon: %.4f '%(self.osmID, self.lon, self.lat))

    def compute_x_y(self):  # wandle die Laengen- und Breitengrade in x-y Koordinaten zur graphischen Darstellung um
        pass

class Kanten:
    def __init__(self, Start, Ende):
        self.start = Start
        self.end = Ende
