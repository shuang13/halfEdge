from Face import Face
from Edge import Edge
from HalfEdge import HalfEdge
from HalfEdgePrev import HalfEdgePrev

def DeleteEdge(mesh, edgeIndex):
	edges = mesh.getEdges()
	edge = edges[edgeIndex]
	edgeHalfEdge = edge.getHalfEdge()
	edgeHalfEdgePrev = HalfEdgePrev(edgeHalfEdge)
	edgeHalfEdgeNext = edgeHalfEdge.getNextHalfEdge()
	edgeHalfEdgeVertex = edgeHalfEdge.getVertex()
	edgeHalfEdgeFace = edgeHalfEdge.getFace()
	edgeHalfEdgeFlip = edgeHalfEdge.getFlipHalfEdge()
	edgeHalfEdgeFlipPrev = HalfEdgePrev(edgeHalfEdgeFlip)
	edgeHalfEdgeFlipNext = edgeHalfEdgeFlip.getNextHalfEdge()
	edgeHalfEdgeFlipVertex = edgeHalfEdgeFlip.getVertex()
	edgeHalfEdgeFlipFace = edgeHalfEdgeFlip.getFace()

	edgeHalfEdgeFace.setHalfEdge(edgeHalfEdgeNext)
	edgeHalfEdgePrev.setNextHalfEdge(edgeHalfEdgeFlipNext)
	edgeHalfEdgeVertex.setHalfEdge(edgeHalfEdgeFlipNext)

	edgeHalfEdgeFlipPrev.setNextHalfEdge(edgeHalfEdgeNext)
	edgeHalfEdgeFlipVertex.setHalfEdge(edgeHalfEdgeNext)

	faces = mesh.getFaces()
	faces.pop(edgeHalfEdgeFlipFace.getIndex())
	for i in range(len(faces)):
		faces[i].setIndex(i)
	
	edges.pop(edgeIndex)
	for i in range(len(edges)):
		edges[i].setIndex(i)
	v1 = edgeHalfEdgeVertex.getIndex()
	v2 = edgeHalfEdgeFlipVertex.getIndex()
	keys = mesh.getEdgeKeys(v1, v2)
	edgeMap = mesh.getEdgeMap()
	del edgeMap[keys[0]]
	del edgeMap[keys[1]]