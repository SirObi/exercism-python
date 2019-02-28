
# Codons are related - this is best represented as a tree/graph (simplified here)
MAP = {
    "AU": "Methionine",
    "UA": "Tyrosine",
    "UC": "Serine",
    "UG": {
        "G": "Tryptophan",
        "U": "Cysteine",
        "C": "Cysteine"
    },
    "UU": {
        "U": "Phenylalanine",
        "C": "Phenylalanine",
        "A": "Leucine",
        "G": "Leucine"
    }
}

STOP_CODON = "UAA, UAG, UGA"


def proteins(strand):
    '''Traverses a tree of codons and returns aminoacid name'''
    translation = []
    next_codon = zip(*[iter(strand)] * 3)
    for codon in next_codon:
        codon = ''.join(codon)
        if codon in STOP_CODON:
            return translation
        protein = MAP[codon[0:2]]
        protein = protein[codon[2]] if isinstance(protein, dict) else protein
        translation.append(protein)
    return translation
