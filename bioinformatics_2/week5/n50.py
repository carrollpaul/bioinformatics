import typing


def n50(contigs: typing.List["int"]) -> int:
    """Calculate N50 for a sequence of numbers.

    Args:
        list_of_lengths (list): List of numbers.

    Returns:
        float: N50 value.

    """
    half = 500
    contigs.sort(reverse=True)
    for i in range(len(contigs)):
        if sum(contigs[:i]) >= half:
            return contigs[i - 1]


contigs = [20, 20, 30, 30, 50, 50, 60, 60, 80, 200]
print(n50(contigs))
