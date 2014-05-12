#!/usr/bin/env python

from src.sequence import Sequence

class Primer:

    def __init__(self, primer_name=None, target_sequence=None, left_start=None,\
            left_length=None, right_start=None, right_length=None):
        if not primer_name:
            self.primer_name = ""
        self.primer_name = primer_name
        if not target_sequence:
            self.target_sequence = Sequence()
        self.target_sequence = target_sequence
        if not left_start:
            self.left_start = 0
        self.left_start = left_start
        if not left_length:
            self.left_length = 0
        self.left_length = left_length
        if not right_start:
            self.right_start = 0
        self.right_start = right_start
        if not right_length:
            self.right_length = 0
        self.right_length = right_length

    def left_primer_to_fasta(self):
        result = self.target_sequence.header + "_"
        result += self.primer_name + "_"
        result += "left\n"
        start = self.left_start + 1  # sequence.get_subseq is 1-based, not 0-based
        stop = start + self.left_length - 1
        result += self.target_sequence.get_subseq(start, stop)
        result += "\n"
        return result

