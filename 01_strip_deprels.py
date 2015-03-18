#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs


def main(filename, col=6, input_enc='utf-8', output_enc='utf-8'):
    with codecs.open(filename, 'r', input_enc) as fin:
        for line in fin:
            cols_keep = line.strip().split()[:col]
            cols_discard = line.strip().split()[col:]
            cols_empty = ['_'] * len(cols_discard)
            print "\t".join(cols_keep + cols_empty).encode(output_enc)


if __name__ == "__main__":
    main(sys.argv[1])
