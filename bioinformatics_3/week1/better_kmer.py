import typing
import os

def frequency_table(text: str, k: int) -> typing.Dict[str, int]:
    freq_map = {}
    n = len(text)
    for i in range(n - k):
        kmer = text[i:i+k]
        if kmer not in freq_map.keys():
            freq_map[kmer] = 1
        else:
            freq_map[kmer] += 1
    return freq_map

def max_map(freq_table: typing.Dict[str, int]) -> int:
    return max(freq_table.values())

def kmer_search(text: str, k: int) -> typing.List[str]:
    kmers = []
    freq_map = frequency_table(text, k)
    max_freq = max_map(freq_map)
    for key, value in freq_map.items():
        if value == max_freq:
            kmers.append(key)
    return kmers

def find_clumps(genome: str, window: int, frequency: int, kmer: int) -> typing.Set[str]:
    patterns = []
    for i in range(len(genome) - window):
        spotlight = genome[i:i+window]
        freq_map = frequency_table(spotlight, kmer)
        for key, value in freq_map.items():
            if value >= frequency:
                patterns.append(key)
    return set(patterns)

root = os.path.dirname(__file__)
with open(f"{root}/ecoli.txt", "r") as f:
    genome = f.readline()
    vals = f.readline().split()
    kmer = int(vals[0])
    window = int(vals[1])
    frequency = int(vals[2])

print(kmer_search("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA", 3))
