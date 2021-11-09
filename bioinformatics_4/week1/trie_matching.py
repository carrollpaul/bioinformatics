import typing
import os
from collections import defaultdict
from networkx.generators.trees import prefix_tree


def recover_path(node: int, trie: prefix_tree) -> str:
    for v in trie.predecessors(node):
        prefix = str(trie.nodes[node]["source"])
        while v != 0:
            prefix = str(trie.nodes[v]["source"]) + prefix
            v = next(trie.predecessors(v))
    return prefix


def prefix_trie_matching(text: str, trie: prefix_tree, node: int = 0):
    if list(trie.successors(node)) == [-1]:
        return recover_path(node, trie)

    if len(text) == 0:
        return None

    for child in list(trie.successors(node)):
        if text[0] == trie.nodes[child]["source"]:
            node = child
            text = text[1:]
            return prefix_trie_matching(text, trie, node)


def trie_matching(text: str, trie: prefix_tree) -> typing.List["int"]:
    index = 0
    matches = defaultdict(list)
    while True:
        if index == len(text):
            return matches
        match = prefix_trie_matching(text[index:], trie)
        if match != None:
            matches[match].append(index)
        index += 1


if __name__ == "__main__":
    base = os.path.dirname(__file__)
    with open(f"{base}/dataset_294_8(2).txt") as f:
        lines = f.readlines()
        text = lines[0].strip()
        patterns = lines[1].strip().split()

    # patterns = ["ATCG", "GGGT"]
    # text = "AATCGGGTTCAATCGGGGT"
    print(patterns)
    trie = prefix_tree(patterns)
    result = trie_matching(text, trie)
    for key, value in result.items():
        suffix = " ".join(str(val) for val in value)
        print(f"{key}: {suffix}")
