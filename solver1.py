import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys
import copy
import heapq
from Unionfind import UnionFind


def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """
    # TODO: your code here!
    MST = kruskal(G)
    if nx.is_empty(MST):
        MST.add_node(0)
        return MST
    leaves = []
    temp = []
    for e in MST.edges():
        u, v = e
        if MST.degree(u) == 1 or MST.degree(e) == 1:
            leaf = min(u, v, key=lambda x:MST.degree(x))
            temp.append(leaf)
            heapq.heappush(leaves ,(G[u][v]['weight'], (u,v), leaf))
    for n in temp:
        MST.remove_node(n)
    while leaves:
        node = heapq.heappop(leaves)
        u,v = node[1]
        oldcost = average_pairwise_distance_fast(MST)
        MST.add_edge(u, v, weight=node[0])
        newcost = average_pairwise_distance_fast(MST)
        if newcost <= oldcost:
            pass
        else:
            MST.remove_edge(u,v)
            MST.remove_node(node[2])
            break
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
