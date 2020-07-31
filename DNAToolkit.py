import collections
from structures import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    # tmpFreqDict = {"A": 0, "C":0, "G":0, "T":0}
    # for nuc in seq:
    #     tmpFreqDict[nuc]+=1
    # return tmpFreqDict
    return dict(collections.Counter(seq))

#transcription: process where DNA is transcribed
def transcription(seq):
    """DNA -> RNA Transription Replacing Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]