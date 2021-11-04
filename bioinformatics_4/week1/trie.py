import typing
import os
from collections import defaultdict
import networkx as nx
from networkx.generators.trees import prefix_tree


if __name__ == "__main__":
    # reads = ["ATAGA", "ATC", "GAT"]
    script_dir = os.path.dirname(__file__)
    with open(f"{script_dir}/dataset_294_4(1).txt") as f:
        reads = f.read().split()

    trie = prefix_tree(reads)
    with open(f"{script_dir}/output.txt", "w") as f:
        for edge in trie.edges:
            if edge[1] != -1:
                val = edge[0], edge[1], trie.nodes[edge[1]]["source"]
                print(*val)
                f.write(f"{val[0]} {val[1]} {val[2]}\n")
