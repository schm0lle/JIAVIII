class Straße():
	def __init__(self, Länge, max_geschw, Knoten1, Knoten2, Punkte):
		self.Knoten1 = Knoten1
		self.Knoten2 = Knoten2
		self.Länge = Länge
		self.max_geschw = max_geschw
		self.Punkte = Punkte
		self.warten = None
		Auto_Ids = []
		self.Stellen = []
	def anmelden(self, Id):
		self.Auto_Ids.append(Id)
		Id.max_geschw = self.max_geschw
	def fahren(self):
		if Auto_Ids:
			Stelle = self.Auto_Ids[-1].Stelle
			for e in Auto_Ids:
				if Stelle == e.Stelle or Stelle - 1.5 > e.Stelle:
					Stelle = e.fahren(True)
				else:
					Stelle = e.fahren(False)
			if self.warten:
				Antwort, Grad, Punkt = self.Knoten2.kreuzen(n_Ziel)
				if Antwort:
					self.warten.abbiegen(Grad, Punkt)
					self.warten = None
	def abbiegen(self, n_Ziel)
		Punkt2.self = self.Auto_Ids[-1]
		self.Auto_Ids.delete(-1)