from VertexNeighbors import VertexNeighbors
from FaceVertices import FaceVertices
from InsertVertex import InsertVertex
from InsertEdge import InsertEdge

def QuadSubdivide(mesh):
	edges = mesh.getEdges()
	elen = len(edges)
	edgeVertices = {}

	for i in range(elen):
		edge = edges[i]
		InsertVertex(mesh, edge.getIndex())

	faces = mesh.getFaces()
	flen = len(faces)
	keys = []
	for i in range(flen):
		face = faces[i]
		edgeVertices[face.getIndex()] = []
		vertices = FaceVertices(face)
		vlen = len(vertices)
		for j in range(vlen):
			vertex = vertices[j]
			neighbors = VertexNeighbors(vertex)
			if(len(neighbors) == 2):
				edgeVertices[face.getIndex()].append(vertex)
	for key in edgeVertices:	
		keys.append(key)
	for i in range(len(keys)):
		faceIndex = keys[i]
		vertices = edgeVertices[faceIndex]
		v0 = vertices[0]
		v1 = vertices[1]
		v2 = vertices[2]
		v3 = vertices[3]
		result = InsertEdge(mesh, v0.getIndex(), v2.getIndex())
		cv = InsertVertex(mesh, result['edge'].getIndex())
		edgeVertices[faceIndex].append(cv)
		InsertEdge(mesh, v1.getIndex(), cv.getIndex())
		InsertEdge(mesh, v3.getIndex(), cv.getIndex())
