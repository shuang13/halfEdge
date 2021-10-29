def VertexNeighbors(vertex):
	startHalfEdge = vertex.getHalfEdge()
	originalHalfEdge = vertex.getHalfEdge()
	he = vertex.getHalfEdge()
	neighbors = []
	while True:
		
		if(he.getNextHalfEdge() == startHalfEdge):
			neighbors.append(he.getVertex())
			if(he.getFlipHalfEdge() == None):
				he = he.getNextHalfEdge()
			else:
				he = he.getFlipHalfEdge()
			startHalfEdge = he
		else:
			he = he.getNextHalfEdge()
		
		if(he == originalHalfEdge):
			break
	return neighbors