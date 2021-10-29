from Vertex import Vertex
from Edge import Edge
from HalfEdge import HalfEdge
from Face import Face

class Mesh:
	def __init__(self):
		# 拓扑结构
		self.vertices = []
		self.edges = []
		self.halfEdges = []
		self.faces = []
		self.boundaries = []

		# 几何结构
		self.positions = []
		self.cells = []
		self.edgeMap = {}
	
	
	
	def getVertices(self):
		return self.vertices
	def getEdges(self):
		return self.edges
	
	def getFaces(self):
		return self.faces
	
	def getHalfEdges(self):
		return self.halfEdges
	
	def getBoundaries(self):
		return self.boundaries
	
	def getEdgeMap(self):
		return self.edgeMap
	
	def getEdgeKey(vertexIndex0, vertexIndex1):
		return str(vertexIndex0) + "-" + str(vertexIndex1)
	
	def getEdgeKeys(self, vertexIndex0, vertexIndex1):
		k1 = str(vertexIndex0) + "-" + str(vertexIndex1)
		k2 = str(vertexIndex1) + "-" + str(vertexIndex0)
		return [k1, k2]
	
	# 判断是否包含某条边
	def containsEdge(self, vertexIndex0, vertexIndex1):
		edgeMap = self.edgeMap
		keys = self.getEdgeKeys(vertexIndex0, vertexIndex1)

		if(edgeMap[keys[0]] != None and edgeMap[keys[1] != None]):
			return True
		return False
	
	def getEdge(self, vertexIndex0, vertexIndex1):
		edgeMap = self.edgeMap
		keys = self.getEdgeKeys(vertexIndex0, vertexIndex1)
		if(keys[0] in edgeMap and keys[1] in edgeMap):
			return edgeMap[keys[0]]
		return False
	
	def setPositions(self, positions):
		self.positions = positions
		for i in range(len(positions)):
			vertex = Vertex()
			vertex.setIndex(i)
			self.vertices.append(vertex)
	
	def getPositions(self):
		results = []
		vertices = self.vertices
		positions = self.positions
		for i in range(len(vertices)):
			index = vertices[i].getIndex()
			results.append(positions[index])
		return results

	def setCells(self, cells):
		self.cells = cells
		for i in range(len(cells)):
			face = Face()
			face.setIndex(i)
			self.faces.append(face)
		self.buildEdgeMap()

	def getCells(self):
		results = []
		faces = self.faces
		vertices = self.vertices
		for i in range(len(faces)):
			face = faces[i]
			halfEdgeStart = halfEdge = face.getHalfEdge()
			cell = []
			while True:
				vertex = halfEdge.getVertex()
				index = vertex.getIndex()
				cell.append(index)
				halfEdge = halfEdge.getNextHalfEdge()
				if(halfEdge == halfEdgeStart):
					break
			results.append(cell)
		return results
	
	def buildEdgeMap(self):
		cells = self.cells
		edges = self.edges
		edgeMap = self.edgeMap
		for i in range(len(cells)):
			cell = cells[i]
			for j in range(len(cell)):
				i0 = cell[j]
				i1 = cell[(j + 1) % len(cell)]

				key0 = str(i0) + "-" + str(i1)
				key1 = str(i1) + "-" + str(i0)

				if((key0 in edgeMap) == False and (key1 in edgeMap) == False):
					edge = Edge()
					edge.setIndex(len(edges))
					edges.append(edge)
					edgeMap[key0] = edge
					edgeMap[key1] = edge
				 
	def process(self):
		edgeMap = self.edgeMap
		edges = self.edges
		cells = self.cells
		vertices = self.vertices
		faces = self.faces
		halfEdges = self.halfEdges

		for faceIndex in range(len(cells)):
			cell = cells[faceIndex]
			face = faces[faceIndex]
			prevHalfEdge = None
			firstHalfEdge = None

			for vertexIndex in range(len(cells[faceIndex])):
				vertexIndexCurr = cell[vertexIndex]
				vertexIndexNext = cell[(vertexIndex + 1) % len(cells[faceIndex])]

				edge = edgeMap[str(vertexIndexCurr) + "-" + str(vertexIndexNext)]
				vertex = vertices[vertexIndexCurr]

				# 设置半边属性

				halfEdge = HalfEdge()
				halfEdge.setVertex(vertex)
				halfEdge.setFace(face)
				halfEdge.setEdge(edge)

				if(edge.getHalfEdge()):
					halfEdge.setFlipHalfEdge(edge.getHalfEdge() )
					edge.getHalfEdge().setFlipHalfEdge(halfEdge)
				else:
					edge.setHalfEdge(halfEdge)
				
				if(prevHalfEdge != None):
					prevHalfEdge.setNextHalfEdge(halfEdge)
				
				prevHalfEdge = halfEdge

				if(vertexIndex == 0):
					firstHalfEdge = halfEdge
				
				halfEdges.append(halfEdge)

				vertex.setHalfEdge(halfEdge)
			face.setHalfEdge(firstHalfEdge)
			prevHalfEdge.setNextHalfEdge(firstHalfEdge)
