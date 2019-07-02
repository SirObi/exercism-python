from functools import reduce

DNA_TO_RNA = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna):
    return reduce(lambda a,b: a+b, (DNA_TO_RNA[n] for n in dna)) if dna else ''
