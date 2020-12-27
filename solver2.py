import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys
import copy
import matplotlib.pyplot as plt


def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """
    # TODO: your code here!
    def checkSingleNode():
        for node in G.nodes():
            S = nx.Graph()
            S.add_node(node)
            if is_valid_network(G, S):
                return node

    result = None
    single = checkSingleNode()
    if single != None:
        result = nx.Graph()
        result.add_node(single)
        return result

    T = copy.deepcopy(G)
    sortededges = [i for i in T.edges()]
    sortededges.sort(reverse=True, key=lambda i:T[i[0]][i[1]]["weight"])
    minvalue = float('inf')
    minindex = -1
    for i in range(len(sortededges)):
        if nx.is_dominating_set(G, T):
            if nx.is_tree(T):
                value = average_pairwise_distance_fast(T)
                if value < minvalue:
                    minvalue = value
                    minindex = i
                    result = copy.deepcopy(T)
        else:
            if i != 0:
                pre = sortededges[i-1]
                T.add_edge(pre[0], pre[1], weight=G[pre[0]][pre[1]]['weight'])
        cur = sortededges[i]
        T.remove_edge(cur[0], cur[1])
        if T.degree(cur[0]) == 0:
            T.remove_node(cur[0])
        if T.degree(cur[1]) == 0:
            T.remove_node(cur[1])

    print(minindex, minvalue)
    return result

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
     assert len(sys.argv) == 2
     path = sys.argv[1]
     G = read_input_file(path)
     T = solve(G)
     #assert is_valid_network(G, T)
     #print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
     #write_output_file(T, 'out/test.out')
