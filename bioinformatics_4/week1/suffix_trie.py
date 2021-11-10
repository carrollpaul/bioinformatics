import networkx as nx


def suffix_trie(text: str) -> nx.prefix_tree:
    text = text + "$"
    suffixes = [text[-i:] for i in range(1, len(text) + 1)]
    return nx.prefix_tree(suffixes)


if __name__ == "__main__":
    suffix_trie("test")
