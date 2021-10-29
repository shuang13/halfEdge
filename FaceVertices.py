def FaceVertices(face):
	originalHalfEdge = he = face.getHalfEdge()
	vertices = []
	while True:
		vertices.append(he.getVertex())
		he = he.getNextHalfEdge()
		if(he == originalHalfEdge):
			break;
	return vertices