from tkinter.constants import NO
from Face import Face
from Edge import Edge
from HalfEdge import HalfEdge
from HalfEdgePrev import HalfEdgePrev
from VertexHalfEdges import VertexHalfEdges

def InsertEdge(mesh, startVertexIndex, endVertexIndex):
	edges = mesh.getEdges()
	halfEdges = mesh.getHalfEdges()
	edgeMap = mesh.getEdgeMap()
	vertices = mesh.getVertices()
	faces = mesh.getFaces()
	edge = mesh.getEdge(startVertexIndex, endVertexIndex)

	if(edge):
		return
	startVertex = vertices[startVertexIndex]
	endVertex = vertices[endVertexIndex]

	cfaces = commonFaces(startVertex, endVertex)
	clen = len(cfaces)
	halfEdgeA = None
	halfEdgeB = None
	halfEdgeC = None
	halfEdgeD = None
	for i in range(clen):
		face = faces[cfaces[i]]
		faceHalfEdge = face.getHalfEdge()
		he = faceHalfEdge
		while True:
			vertexIndex = he.getVertex().getIndex()
			if(vertexIndex == startVertexIndex):
				halfEdgeA = he
			if(vertexIndex == endVertexIndex):
				halfEdgeC = he
			he = he.getNextHalfEdge()
			if(he == faceHalfEdge):
				break
		if(halfEdgeC != None or halfEdgeA != None):
			break

		halfEdgeC = None
		halfEdgeA = None
	if(halfEdgeC == None or  halfEdgeA == None):
		return
	halfEdgeB = HalfEdgePrev(halfEdgeC)
	halfEdgeD = HalfEdgePrev(halfEdgeA)

	newEdge = Edge()
	newEdge.setIndex(len(edges))
	edgeKeys = mesh.getEdgeKeys(startVertexIndex, endVertexIndex)
	edgeMap[edgeKeys[0]] = newEdge
	edgeMap[edgeKeys[1]] = newEdge
	edges.append(newEdge)

	newFace = Face()
	newFace.setIndex(len(faces))
	faces.append(newFace)

	newHalfEdgeAB = HalfEdge()
	newHalfEdgeCD = HalfEdge()

	newHalfEdgeAB.setNextHalfEdge(halfEdgeA)
	newHalfEdgeAB.setFlipHalfEdge(newHalfEdgeCD)
	newHalfEdgeAB.setVertex(endVertex)
	newHalfEdgeAB.setEdge(newEdge)
	newHalfEdgeAB.setFace(face)
	halfEdges.append(newHalfEdgeAB)
	newHalfEdgeCD.setNextHalfEdge(halfEdgeC)
	newHalfEdgeCD.setFlipHalfEdge(newHalfEdgeAB)
	newHalfEdgeCD.setVertex(startVertex)
	newHalfEdgeCD.setEdge(newEdge)
	newHalfEdgeCD.setFace(newFace)
	halfEdges.append(newHalfEdgeCD)
	newEdge.setHalfEdge(newHalfEdgeAB)
	face.setHalfEdge(newHalfEdgeAB)
	newFace.setHalfEdge(newHalfEdgeCD)
	halfEdgeD.setNextHalfEdge(newHalfEdgeCD)
	halfEdgeB.setNextHalfEdge(newHalfEdgeAB)
	setHalfEdgeLoopFace(newHalfEdgeCD, newFace)
	setHalfEdgeLoopFace(newHalfEdgeAB, face)
	return { "edge": newEdge, "face": newFace }

def commonFaces(vertex0, vertex1):
	results = []
	hes0 = VertexHalfEdges(vertex0)
	hes0l = len(hes0)
	hes1 = VertexHalfEdges(vertex1)
	hes1l = len(hes1)

	for i in range(hes0l):
		he0f = hes0[i].getFace()
		for j in range(hes1l):
			he1f = hes1[j].getFace()
			if(he0f.getIndex() == he1f.getIndex()):
				results.append(he0f.getIndex())
	return results

def setHalfEdgeLoopFace(he, face):
	starthe = he
	while True:
		he.setFace(face)
		he = he.getNextHalfEdge()
		if(he == starthe):
			break