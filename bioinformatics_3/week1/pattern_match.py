import typing

def pattern_match(pattern: str, genome: str) -> typing.List[int]:
    n = len(genome)
    k = len(pattern)
    indices = []
    for i in range(n - k):
        kmer = genome[i:i+k]
        if kmer == pattern:
            indices.append(i)
    return indices

print(pattern_match("CGC", "ATGACTTCGCTGTTACGCGC"))