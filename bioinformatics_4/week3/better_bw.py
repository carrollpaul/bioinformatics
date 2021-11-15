import typing


def suffix_array(text: str) -> typing.List["int"]:
    """
    Return a list of indices in lexigraphical order of all suffixes in text, starting with $.
    """
    if text[-1] != "$":
        text = text + "$"
    suffixes = {text[-i:]: len(text) - i for i in range(1, len(text) + 1)}
    indices = []
    sorted_keys = sorted(list(suffixes.keys()))
    for key in sorted_keys:
        indices.append(suffixes.get(key))
    return indices


def bw_count(symbol: str, i: int, col: str):
    """
    Find number of occurances of symbol in the first i positions of col.
    """
    pass


arr = suffix_array("panamabananas$")
print(arr)
