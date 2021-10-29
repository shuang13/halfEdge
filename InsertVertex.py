from Face import Face
from Edge import Edge
from HalfEdge import HalfEdge
from Vertex import Vertex

def InsertVertex(mesh, edgeIndex, *position):
	edges = mesh.getEdges()
	halfEdges = mesh.getHalfEdges()
	edgeMap = mesh.getEdgeMap()
	vertices = mesh.getVertices()
	positions = mesh.positions

	originalEdge = edges[edgeIndex]
	originalHalfEdge = originalEdge.getHalfEdge()
	originalHalfEdgeFace = originalHalfEdge.getFace()
	originalHalfEdgeNext = originalHalfEdge.getNextHalfEdge()
	originalHalfEdgeFlip = originalHalfEdge.getFlipHalfEdge()
	
	originalVertex = originalHalfEdge.getVertex()
	originalVertexIndex = originalVertex.getIndex()
	originalVertexPosition = positions[originalVertexIndex]

	originalVertexNext = originalHalfEdgeNext.getVertex()
	originalVertexNextIndex = originalVertexNext.getIndex()
	originalVertexNextPosition = positions[originalVertexNextIndex]

	newEdge = Edge()
	newVertex = Vertex()
	newHalfEdge = HalfEdge()
	newHalfEdgeFlip = HalfEdge()

	newVertexIndex = len(positions)
	newVertexPosition = [[],[],[]]
	if position:
		newVertexPosition = position
	else:
		newVertexPosition[0] = (originalVertexPosition[0] + originalVertexNextPosition[0]) * 0.5
		newVertexPosition[1] = (originalVertexPosition[1] + originalVertexNextPosition[1]) * 0.5
		newVertexPosition[2] = (originalVertexPosition[2] + originalVertexNextPosition[2]) * 0.5

	newVertex.setIndex(newVertexIndex)
	newVertex.setHalfEdge(newHalfEdge)
	positions.append(newVertexPosition)
	vertices.append(newVertex)

	newHalfEdge.setVertex(newVertex)
	newHalfEdge.setFace(originalHalfEdgeFace)
	newHalfEdge.setNextHalfEdge(originalHalfEdgeNext)
	newHalfEdge.setFlipHalfEdge(originalHalfEdgeFlip)
	newHalfEdge.setEdge(newEdge)

	originalHalfEdge.setNextHalfEdge(newHalfEdge)
	originalHalfEdge.setFlipHalfEdge(newHalfEdgeFlip)

	originalEdgeKey0Old = str(originalVertexIndex) + '-' + str(originalVertexNextIndex);
	originalEdgeKey1Old = str(originalVertexNextIndex) + '-' + str(originalVertexIndex);
	del edgeMap[originalEdgeKey0Old]
	del edgeMap[originalEdgeKey1Old]

	originalEdgeKey0New = str(originalVertexIndex) + '-' + str(newVertexIndex)
	originalEdgeKey1New = str(newVertexIndex) + '-' + str(originalVertexIndex)

	edgeMap[originalEdgeKey0New] = originalEdge
	edgeMap[originalEdgeKey1New] = originalEdge

	newEdge.setIndex(len(edges))
	edges.append(newEdge)
	newEdge.setHalfEdge(newHalfEdge)

	newEdgeKey0 = str(newVertexIndex) + '-' + str(originalVertexNextIndex)
	newEdgeKey1 = str(originalVertexNextIndex) + '-' + str(newVertexIndex)

	edgeMap[newEdgeKey0] = newEdge
	edgeMap[newEdgeKey1] = newEdge

	originalHalfEdgeFlipFace = originalHalfEdgeFlip.getFace()
	originalHalfEdgeFlipNext = originalHalfEdgeFlip.getNextHalfEdge()
	originalHalfEdgeFlip.setNextHalfEdge(newHalfEdgeFlip)
	originalHalfEdgeFlip.setFlipHalfEdge(newHalfEdge)
	originalHalfEdgeFlip.setEdge(newEdge)

	newHalfEdgeFlip.setNextHalfEdge(originalHalfEdgeFlipNext)
	newHalfEdgeFlip.setFlipHalfEdge(originalHalfEdge)
	newHalfEdgeFlip.setVertex(newVertex)
	newHalfEdgeFlip.setEdge(originalEdge)
	newHalfEdgeFlip.setFace(originalHalfEdgeFlipFace)
	halfEdges.append(newHalfEdgeFlip)

	return newVertex