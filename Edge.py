class Edge:
	def __init__(self):
		self.halfEdge = None
		self.index = -1

	def setIndex(self, index):
		self.index = index

	def getIndex(self):
		return self.index

	def setHalfEdge(self, halfEdge):
		self.halfEdge = halfEdge

	def getHalfEdge(self):
		return self.halfEdge