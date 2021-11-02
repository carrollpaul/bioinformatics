import typing
from integer_mass_table import integer_mass_table
from theoretical_spectrum import cyclic_spectrum


def expand(candidates: typing.List['str']) -> typing.List['str']:
    aas = list(integer_mass_table.keys())
    if candidates == ['']:
        return aas
    else:
        return [candidate + aa for aa in aas for candidate in candidates]


def mass(peptide: str) -> int:
    mass = 0
    for aa in peptide:
        mass += integer_mass_table.get(aa)


def cyclopeptide_sequencing(spectrum: typing.List['int']) -> typing.List['str']:
    candidates = [""]
    winners = []
    while len(candidates) != 0:
        candidates = expand(candidates)
        for candidate in candidates:
            if mass(candidate) == spectrum[-1]:
                if cyclic_spectrum(candidate) == spectrum and candidate not in winners:
                    winners.append(candidate)
                candidates.pop(candidate)
            elif candidate:
                pass


if __name__ == '__main__':
    spectrum = [0, 113, 128, 186, 241, 299, 314, 427]
    cyclopeptide_sequencing(spectrum)
    print(expand(['']))
