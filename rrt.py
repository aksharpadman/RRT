import matplotlib.pyplot as plt
from math import sqrt,cos,sin,atan2
import random
import networkx as nx
from ast import literal_eval


goal = literal_eval(raw_input("Enter goal coordinates '(x,y)' :"))
ques= str(raw_input("are there any obstacles? y or n: "))
if ques == "y":
	obstacle_list = literal_eval(raw_input("Please enter the  list of obstacles coordinates(ex:[(10,20),(30,40)]): ")) #nodes which are having obstacles or are out of the map
elif ques == "n":
	obstacle_list=[]

#dimension of workspace
Xdim =500
Ydim = 500
#area of workspace
area =(Xdim,Ydim)
#Start point
start=(0,0)

#size of step 
step_size = 5.0

#number of iterations
n_iter = 5000 
#goal position and goal limit to be achieved
g_rad = 5

#obstacle radius 
obs_limit = 10
#initializing graph
G = nx.Graph()
#environment setting with obstacles and goals
H = nx.Graph()
H.add_node('end',pos=goal,color = 'green')

#obstacle list 
#obstacle_list =[(100,250),(400,350)]
#T = nx.Graph()
for i in range(len(obstacle_list)):
	H.add_node(i,pos = obstacle_list[i],color='blue')
#node colors to represent obstacles and goal
colors = []	
for each in H.nodes():
	colors.append(H.node[each]['color'])

#function to check if newnode within obstacle limits
def within_obstacle_limit(node):
	result = False #default 
	for obstacle in obstacle_list:
		dist_sq = (obstacle[0]-node[0])**2 + (obstacle[1]-node[1])**2
		if dist_sq < obs_limit**2:
			result = True
			break
		else :
			result = False
	return result



def dist(point1,point2):
    return sqrt((point1[0]-point2[0])*(point1[0]-point2[0])+(point1[1]-point2[1])*(point1[1]-point2[1]))

#function to check if new node exceeds step size limit
def step_check(point1,point2):
	if dist(point1,point2) < step_size:
		return point2
	else:
		angle = atan2(point2[1]-point1[1],point2[0]-point1[0])
		return point1[0] + step_size*cos(angle), point1[1] + step_size*sin(angle)

#function to check if node is within goal radius
def check_end_radius(goal,newnode):
	return ((goal[0]-newnode[0])**2 + (goal[1]-newnode[1])**2)

#function to get the final path
def get_path(node):
	path_list = []
	parent=G.node[node]['parent']
	path_list.append((parent,node))

	while parent!=0:
		
		node = parent
		parent=G.node[node]['parent']
		path_list.append((parent,node))

	return path_list


def main():
	
	edge_list = []
	nodes = []
	G.add_node(0,pos=(0.0,0.0),parent=0) 
	nodes.append(start)
	n = 0
	for i in range(n_iter):
		rand_point = (random.random()*500.0, random.random()*500.0)
		nearn = nodes[0]
		nearestnode_index = 0
		for x,data in G.nodes(data=True):
			point = data['pos']
			if dist(point,rand_point) < dist(nearn,rand_point):
				nearn = point
				nearestnode_index = x
		newnode = step_check(nearn,rand_point)

		if within_obstacle_limit(newnode) == False:
			nodes.append(newnode)
			G.add_node(i,pos =newnode,parent=nearestnode_index)
			G.add_edge(nearestnode_index,i)
		else:
			continue

		if check_end_radius(goal,newnode)<(g_rad**2):
			finish = i	
			edge_list = get_path(finish)
			break

	plt.figure(figsize=(10,10))	
	plt.gca().set_xlim([0,500])
	plt.gca().set_ylim([0,500])

	nx.draw_networkx_edges(G,nx.get_node_attributes(G, 'pos'),edgelist=edge_list,edge_color='r',width=3)
	nx.draw_networkx_nodes(H,nx.get_node_attributes(H, 'pos'),nodelist=H.nodes(),node_color=colors,node_size=50)			
	nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=False, node_size=0)
	
	plt.show()
if __name__ == '__main__':
    main()
