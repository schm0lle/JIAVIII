
# pro Iteration aendert sich die simulierte (physikalische) Zeit um dt 
dt = 1  # in Sekunden

class Strasse:
    def __init__(self, osm_data):  # hiermit wird ein neues Strassenobjekt erzeugt
        self.osm_data = osm_data
        self.Autos = []  # hier speichern wir die IDs der Autos auf dieser Strasse

    def add_Auto(self, ID):  # fuege Auto zur Strasse hinzu
        self.Autos.append(ID)


class Auto:
    def __init__(self, position, v0=13.89):  # hiermit wird ein Autoobjekt erzeugt
        self.v = v0  # Geschwindigkeit, wird mit Startgeschwindigkeit initialisiert
        self.position = position  # Position soll ein Tupel aus StrassenID und Position entlang der Strasse sein

    def move_one_step(self):  # laesst das Auto einen Zeitschritt fahren
        self.position[1] = self.position[1] + self.v * dt

    def __str__(self):
        return('Das Auto faehrt %.2f m / s,\nes befindet sich auf Strasse mit ID %d,\nbei Abschnitt  %.2f m '%(self.v, self.position[0], self.position[1]))
