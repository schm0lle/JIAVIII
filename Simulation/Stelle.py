class Auto():
	def __init__(self,  Art, Ziel): #Ziel ist eine Liste in der die Kanten die das Auto fahren möchte angegeben sind und zwar als Objekte
		self.max_geschw = 13.0
		self.Art = Art
		self.Ziel = Ziel
		self.Stelle = 0   #Für den Stellenstempel
		self.Strecke = [] #Für Darstellund hier werden alle Punkte einer Kante angegeben
	def fahren(self, stop):#Stop ist bool
		if not stop:
			a = self.Strecke[-1]
			if self.max_geschw >= a:
				self.Strecke.delete(-1)
				pass
				#Grad Winkel für Umsetzung
				if not self.Strecke:
					self.Ziel[-1].abmelden(self.Ziel[-2])
			self.Stelle += max_geschw
			return self.Stelle
	def abbiegen(self, Grad, Punkt):
		self.Stelle = 0
		self.Strecke  = self.Ziel[-1].Punkte
		self.Ziel[-1].anmelden(self)
		self.Ziel.delete(-1)
		#Grad und Punkt für grafische Darstellung
		
		
#Das letzte Ziel ist immer eine virtuele Strasse auf der das Auto solange wartet bis es gebraucht wird