class HalfEdge:
	def __init__(self):
		self.nextHalfEdge = None # 当前面的下一条半边
		self.flipHalfEdge = None # 另一条与当前半边方向相反的半边
		self.vertex = None # 当前半边的终点
		self.edge = None # 当前半边所在的边
		self.face = None # 包含这条半边的面
	
	def setVertex(self, vertex):
		self.vertex = vertex
	
	def getVertex(self):
		return self.vertex

	def setEdge(self, edge):
		self.edge = edge
	
	def getEdge(self):
		return self.edge
	
	def setFace(self, face):
		self.face = face
	
	def getFace(self):
		return self.face
	
	def setNextHalfEdge(self, halfEdge):
		self.nextHalfEdge = halfEdge
	
	def getNextHalfEdge(self):
		return self.nextHalfEdge
	
	def setFlipHalfEdge(self, halfEdge):
		self.flipHalfEdge = halfEdge
	
	def getFlipHalfEdge(self):
		return self.flipHalfEdge
	
	# 判断该半边是否为边缘的半边，也就是无孪生半边
	def onBoundary(self):
		if(self.getFlipHalfEdge()):
			return False
		return True