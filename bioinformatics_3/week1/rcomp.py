import os

def reverse_complement(dna: str) -> str:
    LOOKUP_TABLE = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    sequence = dna.upper()
    rcomp = ""
    for letter in sequence[::-1]:
        rcomp += LOOKUP_TABLE.get(letter)
    return rcomp


print(reverse_complement("GCTAGCT"))
