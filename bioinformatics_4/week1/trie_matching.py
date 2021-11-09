import typing
from collections import defaultdict
from networkx.generators.trees import prefix_tree


def recover_path(node: int, trie: prefix_tree) -> str:
    for v in trie.predecessors(node):
        prefix = str(trie.nodes[node]["source"])
        while v != 0:
            prefix = str(trie.nodes[v]["source"]) + prefix
            v = next(trie.predecessors(v))
    return prefix


def prefix_trie_matching(text: str, trie: prefix_tree, source: int = 0):
    if list(trie.successors(source)) == [-1]:
        return recover_path(source, trie)

    for child in list(trie.successors(source)):
        if text[0] == trie.nodes[child]["source"]:
            source = child
            text = text[1:]
            return prefix_trie_matching(text, trie, source)


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
    patterns = ["ATCG", "GGGT"]
    text = "AATCGGGTTCAATCGGGGT"
    trie = prefix_tree(patterns)
    print(trie_matching(text, trie))
