import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys
import copy
from Unionfind import UnionFind
import heapq

def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """
    # TODO: your code here!
    oneNode = nx.Graph()
    oneNode.add_node(0)
    if (G == None):
        return oneNode
    elif (len(G) == 1):
        return oneNode
    elif len(G.edges()) == len(G)*(len(G)-1)/2:
        return oneNode
    MST = kruskal(G)
    leaves = []
    heap = []
    for e in MST.edges():
        u = e[0]
        v = e[1]
        if MST.degree(u)==1 or MST.degree(v)==1:
            leafnode = min(u, v, key=lambda x: MST.degree(x))
            leaves.append(leafnode)
            heapq.heappush(heap, (G[u][v]['weight'], e, leafnode))
    for node in leaves:
        MST.remove_node(node)
    costG = average_pairwise_distance_fast(MST)
    minEdge = heapq.heappop(heap)
    MST.add_edge(minEdge[1][0], minEdge[1][1], weight=minEdge[0])
    costGprime = average_pairwise_distance_fast(MST)
    while (costGprime < costG):
    	costG = average_pairwise_distance_fast(MST)
    	minEdge = heapq.heappop(heap)
    	MST.add_edge(minEdge[1][0], minEdge[1][1], weight=minEdge[0])
    	costGprime = average_pairwise_distance_fast(MST)
    MST.remove_edge(minEdge[1][0], minEdge[1][1])
    MST.remove_node(minEdge[2])
    return MST


def kruskal(G):
    MST = nx.Graph()
    uf = UnionFind(len(G.nodes()))
    sortededges = [i for i in G.edges()]
    sortededges.sort(key=lambda i:G[i[0]][i[1]]["weight"])
    for e in sortededges:
        u, v = e
        if not uf._samePartition(u, v):
            MST.add_edge(u, v, weight=G[u][v]['weight'])
            uf._union(u, v)
    return MST

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
     assert len(sys.argv) == 2
     path = sys.argv[1]
     G = read_input_file(path)
     T = solve(G)
     assert is_valid_network(G, T)
     print("Average pairwise distance: {}".format(average_pairwise_distance(T)))
     #write_output_file(T, 'out/test.out')
