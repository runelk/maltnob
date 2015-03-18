#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import maltnob.partitions as p


def main(conll_filename, k=10):
    p.make_corpus_partitions(k, conll_filename)
    p.make_train_and_test_partitions(k, conll_filename)

if __name__ == "__main__":
    main(sys.argv[1])
