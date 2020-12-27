from parse import *
import networkx as nx
import os
import solver

if __name__ == "__main__":
    output_dir = "submission"
    input_dir = "inputs"
    for input_path in os.listdir(input_dir):
        graph_name = input_path.split(".")[0]
        G = read_input_file(f"{input_dir}/{input_path}")
        T = solver.solve(G)
        write_output_file(T, f"{output_dir}/{graph_name}.out")
