def HalfEdgePrev(he):
	startHalfEdge = he
	while( he.getNextHalfEdge() != startHalfEdge):
		he = he.getNextHalfEdge()
	return he