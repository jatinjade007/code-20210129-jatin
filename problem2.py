from collections import defaultdict 
import os

# Function to build the graph 
def build_graph(edges): 
	graph = defaultdict(list) 
	
	for edge in edges: 
		a, b = edge[0], edge[1] 
		graph[a].append(b) 
		graph[b].append(a) 
	return graph 

def BFS_SP(graph, start, goal): 
	explored = [] 
	
	queue = [[start]] 
	
	if start == goal: 
		print("Same Node") 
		return
	
	while queue: 
		path = queue.pop(0) 
		node = path[-1] 
		if node not in explored: 
			neighbours = graph[node] 
			
			for neighbour in neighbours: 
				new_path = list(path) 
				new_path.append(neighbour) 
				queue.append(new_path) 
				
				if neighbour == goal: 
					print("Shortest path = ", *new_path) 
					return
			explored.append(node) 

	print("So sorry, but a connecting path doesn't exist :(") 
	return


def readFile():
	node1 = input ("Enter value from node 1: ")
	node2 = input ("Enter value from node 2: ")
	root = os.getcwd()
	root = root+"/data/"
	for path, subdirs, files in os.walk(root):
		for name in files:
			f = open(path+'/'+name,)
			first_line = f.readline().split('#')
			nodes = [int(i) for i in first_line[1].split() if i.isdigit()]
			edges = [int(i) for i in first_line[2].split() if i.isdigit()]
			datatable = [line.split() for line in f.read().splitlines()]
			graph = build_graph(datatable)
			BFS_SP(graph, node1, node2) 

if __name__ == "__main__": 
	readFile()
