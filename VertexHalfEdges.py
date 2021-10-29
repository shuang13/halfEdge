def VertexHalfEdges(vertex):
	startHalfEdge = originalHalfEdge = he = vertex.getHalfEdge()
	halfEdges = []
	while True:
		if(he.getNextHalfEdge() == startHalfEdge):
			he = he.getFlipHalfEdge()
			startHalfEdge = he
			halfEdges.append(he)
		else:
			he = he.getNextHalfEdge()
		if(he == originalHalfEdge):
			break
	return halfEdges