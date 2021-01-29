import os

MAXN = 10000001

tree = [0] * MAXN
for i in range(MAXN):
	tree[i] = []


path = [0] * 3
for i in range(3):
	path[i] = [0] * MAXN

flag = False

def dfs(cur: int, prev: int, pathNumber: int,
		ptr: int, node: int) -> None:

	global tree, path, flag

	for i in range(len(tree[cur])):
		if (tree[cur][i] != prev and not flag):

			# Pushing current node into the path
			path[pathNumber][ptr] = tree[cur][i]

			if (tree[cur][i] == node):

				# Node found
				flag = True

				# Terminating the path
				path[pathNumber][ptr + 1] = -1
				return

			dfs(tree[cur][i], cur, pathNumber,
				ptr + 1, node)

def LCA(a: int, b: int) -> int:
	global flag

	if (a == b):
		return a

	# Setting root to be first element
	# in path
	path[1][0] = path[2][0] = 1

	# Calculating path from root to a
	flag = False
	dfs(1, 0, 1, 1, a)

	# Calculating path from root to b
	flag = False
	dfs(1, 0, 2, 1, b)

	# Runs till path 1 & path 2 mathches
	i = 0
	while (path[1][i] == path[2][i]):
		i += 1

	# Returns the last matching
	# node in the paths
	return path[1][i - 1]


def addEdge(a: int, b: int) -> None:
	tree[a].append(b)
	tree[b].append(a)


def readFile():
	root = os.getcwd()
	root = root+"/data/"
	for path, subdirs, files in os.walk(root):
		for name in files:
			f = open(path+'/'+name,)
			first_line = f.readline().split('#')
			nodes = [int(i) for i in first_line[1].split() if i.isdigit()]
			edges = [int(i) for i in first_line[2].split() if i.isdigit()]
			Counter = 0
			for line in f.read().splitlines():
				if line:
					if Counter > 1:
						addEdge(int(line.split()[0]), int(line.split()[1]))
					Counter +=1


if __name__ == "__main__":
	readFile()

	print("LCA(4, 7) = {}".format(LCA(4, 7)))