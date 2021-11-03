import typing
from collections import Counter


def AminoAcidMassDict():
    massTable = """
G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186"""
    mass = massTable.split()
    return {mass[i]: int(mass[i + 1]) for i in range(0, len(mass), 2)}


def CyclicSpectrum(peptide: str) -> typing.List["int"]:
    massDict = AminoAcidMassDict()
    n = len(peptide)
    PrefixMass = [0]
    for i in range(n):
        PrefixMass.append(PrefixMass[i] + massDict[peptide[i]])
    peptideMass = PrefixMass[n]
    cSpectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            cSpectrum.append(PrefixMass[j] - PrefixMass[i])
            if i > 0 and j < n:
                cSpectrum.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))
    return sorted(cSpectrum)


def peptide_score(peptide: str, spectrum: typing.List["int"]) -> int:
    theoretical_spectrum = Counter(CyclicSpectrum(peptide))
    exp_spectrum = Counter(spectrum)
    score = 0
    for key, value in exp_spectrum.items():
        if key in theoretical_spectrum:
            if theoretical_spectrum[key] >= value:
                score += value
            else:
                score += theoretical_spectrum[key]

    return score


if __name__ == "__main__":
    """
    with open("C:/Users/Paul/src/bioinformatics/bioinformatics_2/week4/dataset_102_3(1).txt") as f:
        peptide = f.readline().rstrip()
        spectrum = [int(line) for line in f.readline().rstrip().split()]
    """
    peptide = "MAMA"
    spectrum = [0, 71, 178, 202, 202, 202, 333, 333, 333, 404, 507, 507]
    print(peptide_score(peptide, spectrum))
