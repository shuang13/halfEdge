from Mesh import Mesh
def Profile(profile):
	mesh = Mesh()
	positions = []
	frontFace = []
	backFace = []

	for i in range(len(profile)):
		positions.append([profile[i][0], profile[i][1], 0.0])
		frontFace.append(i)
		backFace.append(len(profile) - 1 - i)
	
	# 正反面构成封闭拓扑
	cells = [frontFace, backFace]

	mesh.setPositions(positions)
	mesh.setCells(cells)
	mesh.process()
	return mesh

if __name__ == '__main__':
    mesh = Profile([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])
