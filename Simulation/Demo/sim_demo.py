import Klassen as KL
import matplotlib.pyplot as plt

Zeit = [0]
dt = 1  # Zeitschritt

# Wir definieren ein Woerterbuch, welches unsere Strassen enthaelt
# mit KL.Strasse(osm_data) koennen wir ein neues Strassenobjekt erzeugen
osm_data = {'v_max_in_m/s' : 13.89, 'laenge_in_m': 500}  # diesen Datensatz liefert die OSM Gruppe 
Strassen = [KL.Strasse(osm_data), KL.Strasse(osm_data)]

# Wir definieren ein paar Autos
# mit KL.Auto(position) koennen wir ein neues Autobjekt erzeugen
Autos = []
position1 = [0, 0]  # das erste Auto befindet sich zu Beginn auf der ersten Strasse bei Abschnitt 0.0 (ganz am Anfang der Strasse)
Autos.append(KL.Auto(position1))
Strassen[0].add_Auto(0)
Autos.append(KL.Auto([0, 0.5 * Strassen[0].osm_data['laenge_in_m']]))  # das zweite Auto befindet sich in der Mitte der ersten Strasse 
Strassen[0].add_Auto(0)

# gib Infos ueber das erste Auto in der Liste aus
print(Autos[0])

# -------- ein Zeitschritt in der Simulation -----------
Zeit.append(Zeit[-1] + dt)
print('\n---------- Zeitpunkt %.2f --------------\n'%Zeit[-1])
# bewege alle Autos ein wenig nach vorne
Autos[0].move_one_step()
print(Autos[0])

y = [Autos[0].position[1]]
for t in range(0,10):  # Haupt-Simulationsschleife
    Zeit.append(Zeit[-1] + dt)
    Autos[0].move_one_step()
    y.append(Autos[0].position[1])


# graphische Ausgabe
plt.plot(Zeit[1:], y,'*')
plt.title('Strecke von Auto 0 entlang Strasse 0')
plt.xlabel('Zeitschritte')
plt.ylabel('Strecke in m')

plt.show()

