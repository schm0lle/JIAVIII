import numpy as np
import matplotlib.pyplot as plt

# Simulationsparameter
p = dict()
p['end_time'] = 5 * 60.0  # s
p['avg_nr_of_cars_per_min'] = 3  # durchschnittliche Anzahl an Autos pro Minute, die in die erste Strasse einbiegen. Mit dieser Info koennen wir den Zufallsgenerator speisen.
p['dt'] = 1  # s

# Zufallsgenerator
def car_randomgenerator(p):
    """ Fuehrt Zufallsexperiment einmal aus. Falls positiv, gibt es ID des generierten Autos zurueck."""
    gen_prob = p['avg_nr_of_cars_per_min'] * p['dt'] / 60.0  # Wahrscheinlichkeit, dass Auto im naechsten Zeitschritt in die Strasse einbiegt
    zufallszahl = np.random.uniform()
    if zufallszahl < gen_prob:
        return 1 
    else:
        return 0


# your turn ...

    
# ---------------------------
#S = list(set(Anzahl_Autos_Liste))  # unique
#Y = []
#for s in S:
#    Y.append(Anzahl_Autos_Liste.count(s))

#plt.plot(S, Y, '*')
#plt.show()




