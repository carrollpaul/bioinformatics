import itertools
from collections import defaultdict

genetic_code = {
    "ACC": "T",
    "GCA": "A",
    "AAG": "K",
    "AAA": "K",
    "GUU": "V",
    "AAC": "N",
    "AGG": "R",
    "UGG": "W",
    "GUC": "V",
    "AGC": "S",
    "ACA": "T",
    "AGA": "R",
    "AAU": "N",
    "ACU": "T",
    "GUG": "V",
    "CAC": "H",
    "ACG": "T",
    "AGU": "S",
    "CCA": "P",
    "CAA": "Q",
    "CCC": "P",
    "UGU": "C",
    "GGU": "G",
    "UCU": "S",
    "GCG": "A",
    "CGA": "R",
    "CAG": "Q",
    "CGC": "R",
    "UAU": "Y",
    "CGG": "R",
    "UCG": "S",
    "CCU": "P",
    "GGG": "G",
    "GGA": "G",
    "GGC": "G",
    "CCG": "P",
    "UCC": "S",
    "UAC": "Y",
    "CGU": "R",
    "GAA": "E",
    "AUA": "I",
    "AUC": "I",
    "CUU": "L",
    "UCA": "S",
    "AUG": "M",
    "UGA": " ",
    "CUG": "L",
    "GAG": "E",
    "AUU": "I",
    "CAU": "H",
    "CUA": "L",
    "UAA": " ",
    "GCC": "A",
    "UUU": "F",
    "GAC": "D",
    "GUA": "V",
    "UGC": "C",
    "GCU": "A",
    "UAG": " ",
    "CUC": "L",
    "UUG": "L",
    "UUA": "L",
    "GAU": "D",
    "UUC": "F",
}


def DNArc(DNA):
    # In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
    # The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss,
    # then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
    rvDNA = ""  # reverse DNA that will be returned
    for base in DNA:
        if base == "A":
            rvDNA = rvDNA + "T"
        elif base == "T":
            rvDNA = rvDNA + "A"
        elif base == "G":
            rvDNA = rvDNA + "C"
        elif base == "C":
            rvDNA = rvDNA + "G"

    rvDNA = rvDNA[::-1]
    return rvDNA


def protein_to_DNA(Prot_seq):
    # building a dict of aa to codons {'C': ['UGU', 'UGC']...}
    aa_to_codons = defaultdict(list)
    for k, v in genetic_code.items():
        aa_to_codons[v].append(k)

    # total number of possible RNA sequences
    total_RNA = 1
    # All possible RNA sequences [[],...]
    codons = []
    for e in Prot_seq:
        total_RNA *= len(aa_to_codons[e])
        codons.append(aa_to_codons[e])

    return codons


def all_Prot_RNA(protein):
    # list of possible RNA molecules for a protein sequence
    possible_RNAs = ["".join(x) for x in list(itertools.product(*protein_to_DNA(protein)))]
    return possible_RNAs


def RNA_to_DNA(RNAstring):
    DNAstring = ""
    for e in RNAstring:
        if e == "U":
            DNAstring = DNAstring + "T"
        else:
            DNAstring = DNAstring + e
    return DNAstring


def prot_in_genome(protein):

    # find all possible RNAs for protein
    RNAs = all_Prot_RNA(protein)

    # transform them to DNA
    DNAs = [RNA_to_DNA(e) for e in RNAs]

    # add their reverse complements
    rvDNAs = [DNArc(e) for e in DNAs]
    DNAs = DNAs + rvDNAs

    # Checking each possible DNA in the genome
    # list of all motifs found
    return len(DNAs)


options = [[1, 2, 3, 4, 5, 6], [1, 2], [1, 2, 3, 4], [1, 2], [1, 2], [1, 2, 3, 4, 5, 6]]
print(len(list(itertools.product(*options))))
