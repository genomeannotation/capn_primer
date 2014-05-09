#!/usr/bin/env python

def parse_gff_attributes(attr):
    attr = attr.strip(' \t\n;').split(';') # Sanitize and split
    key_vals = [a.split('=') for a in attr]
    return dict(zip([kv[0] for kv in key_vals], [kv[1] for kv in key_vals]))

class GFFReader:

    def __init__(self):
        self.cds_segment_lengths = []

    def read(self, io_buffer):
        orphans = []
        for line in io_buffer:        
            columns = line.split('\t')
            attr = parse_gff_attributes(columns[8])
            #if columns[2] == 'mRNA':
                #self.cds_segment_lengths