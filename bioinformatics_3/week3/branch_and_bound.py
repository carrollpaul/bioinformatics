def branch_and_bound(n: int) -> int:
    """
    Find the number of subpeptides of a linear peptide of length n,
    including the empty peptide and the entire peptide.
    """
    return int(n * (n + 1) / 2 + 1)


print(branch_and_bound(13747))
