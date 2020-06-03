from collections import deque
class Graph:
    
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
    def get_neighbors(self, v):
        return self.adjacency_list[v]
    def h(self, n):
        H = {
            'S': 6,
            'A': 8,
            'B': 6,
            'C': 5,
            'D': 4,
            'E': 2,
            'F': 1,
            'G': 0
        }
        return H[n]
    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        counter=0
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        print("OPEN\t\t\t\tCLOSE")
        while len(open_list) > 0:
            n = None
            counter+=1
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                
                print(open_list,"\t\t\t",closed_list)
                print()
                print('Path found: {}'.format(reconst_path))
                cost=0
                for i in range(len(reconst_path)-1):
                    node=(self.adjacency_list[reconst_path[i]])
                    for j in node:
                        if reconst_path[i+1] in j:
                            cost+=j[1]
                            break
                print("Total cost:",cost)
                    
                
                return reconst_path
            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
            if counter==1:
                print(open_list,end="\t\t\t\t")
                print(closed_list)
            else:
                print(open_list,end="\t\t\t")
                print(closed_list)
            counter+=1
        print('Path does not exist!')
        return None
adjacency_list = {
    'S': [('A', 6), ('B', 2), ('C', 1)],
    'A': [('D', 2), ('G', 20)],
    'B': [('D', 2), ('E', 6)],
    'C': [('E', 6), ('F', 4)],
    'D': [('F', 5)],
    'E': [('G', 2)],
    'F': [('G',1)],
    'G': []
    }
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('S', 'G')
