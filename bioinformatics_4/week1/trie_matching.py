import os
from networkx.generators.trees import prefix_tree


def prefix_trie_matching(text: str, trie: prefix_tree):
    root, nil = 0, -1
    for v in trie.successors(root):
        char = 0
        while v != nil:
            node_val = str(trie.nodes[v]["source"])
            if node_val == text[char]:
                print(node_val)
                char += 1
                v = next(trie.successors(v))
        """
        while v != nil:
            print(v, str(trie.nodes[v]["source"]))
            v = next(trie.successors(v))
    
    for char in text:
        for v
    for edge in edges:
        if edge[1] == -1:
            pattern = []
            for v in trie.predecessors(-1):
                while v != 0:
                    prefix = ""
                    prefix = str(trie.nodes[v]["source"]) + prefix
                    v = next(trie.predecessors(v))
                pattern.append(prefix)
            print(pattern)"""


if __name__ == "__main__":
    patterns = ["ATCG", "GGGT"]
    text = "AATCGGGTTCAATCGGGGT"
    trie = prefix_tree(patterns)
    prefix_trie_matching(text, trie)
