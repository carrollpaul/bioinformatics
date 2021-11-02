import typing
from itertools import combinations, chain
from integer_mass_table import integer_mass_table


def linear_spectrum(peptide: str) -> typing.List['int']:
    prefix_mass = [0]
    for aa in peptide:
        mass = integer_mass_table.get(aa)
        prefix_mass.append(mass + prefix_mass[-1])

    linear_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])

    return sorted(linear_spectrum)


def cyclic_spectrum(peptide: str) -> typing.List['int']:
    prefix_mass = [0]
    for aa in peptide:
        mass = integer_mass_table.get(aa)
        prefix_mass.append(mass + prefix_mass[-1])

    peptide_mass = prefix_mass[-1]

    cyclic_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(
                    peptide_mass - (prefix_mass[j] - prefix_mass[i]))

    return sorted(cyclic_spectrum)


if __name__ == '__main__':
    peptide = 'VQMTGYPFYVFW'
    with open('output.txt', 'w') as f:
        for val in cyclic_spectrum(peptide):
            f.write(str(val))
            f.write(" ")
