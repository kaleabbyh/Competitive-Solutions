

def to_rna(dna: str):
    code = str.maketrans('TCGA', 'AGCU')
    return dna.translate(code)
