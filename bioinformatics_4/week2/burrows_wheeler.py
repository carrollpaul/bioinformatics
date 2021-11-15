from collections import Counter, defaultdict
import typing


def burrows_wheeler(text: str) -> str:
    original = text
    table = [original]
    ans = ""

    while True:
        prefix = text[:-1]
        suffix = text[-1:]
        new = suffix + prefix
        if new == original:
            break
        table.append(new)
        text = new

    return "".join(val[-1] for val in sorted(table)), sorted(table)


def index_column(col: typing.List["int"], first: bool = True) -> typing.Dict["str", "int"]:
    lookup = defaultdict(int)
    indexed = {}
    for index, val in enumerate(col):
        lookup[val] += 1
        if first:
            indexed[index] = val + str(lookup.get(val))
        else:
            indexed[val + str(lookup.get(val))] = index

    return indexed


def burrows_wheeler_inversion(text: str) -> str:
    last_col = index_column(text, first=False)
    first_col = index_column(sorted(text))

    char = "$1"
    ans = []
    while True:
        if len(ans) == len(text):
            final = ans[1:].append("$")
            return "".join(x for x in ans)

        # Get position of char in last column
        pos = last_col[char]

        # Get char in same position in first column
        char = first_col.get(pos)
        ans.append(char[0])


def last_to_first(first_col: str, last_col: str) -> int:
    """
    Create mapping of positions between equivalent chars in two strings.
    """
    last_column = index_column(last_col)
    first_column = index_column(first_col, False)

    d = {}
    for i in range(len(last_column)):
        # Get value at position i of last column
        val = last_column.get(i)
        # Get position of val in first column
        pos = first_column.get(val)
        d[i] = pos

    return d


def bw_matching(text: str, pattern: str) -> int:
    """
    Count number of occurances of pattern in Burrows-Wheeler inverted string of text.

    Args:
        text: A string that has been Burrows-Wheeler transformed
        pattern: String to match

    Returns:
        0 if pattern does not appear in text, else number of matches.
    """
    # Get first and last columns of M(text)
    last_col = text
    first_col = "".join(sorted(text))

    # Get mapping between columns
    col_map = last_to_first(first_col, last_col)

    top = 0
    bottom = len(first_col)
    while True:
        if pattern:
            # Pop last char in pattern
            symbol, pattern = pattern[-1], pattern[:-1]
            frame = last_col[top : bottom + 1]

            if symbol in frame:
                # Record first and last occurances of symbol in frame
                # Must account of relative position of frame within last column by
                # adding the top index to the sub string index
                top_index = frame.find(symbol) + top
                bottom_index = frame.rfind(symbol) + top

                # Get equivalent positions in first column
                top, bottom = col_map.get(top_index), col_map.get(bottom_index)

            else:
                # No matches
                return 0
        else:
            return bottom - top + 1


if __name__ == "__main__":
    text = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
    patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
    for pat in patterns:
        print(bw_matching(text, pat))
