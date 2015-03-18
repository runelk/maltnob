#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import sys
from collections import Counter
import codecs
import nltk
from nltk import BigramAssocMeasures


def pmi(filename_unigrams, filename_bigrams):
    total = 0
    words = {}
    results = {}

    with codecs.open(filename_unigrams, 'r', 'utf-8') as f:
        for line in f:
            if line:
                spl = line.split()
                freq = int(spl[-1])
                total += freq
                words["\t".join([spl[0], spl[1]])] = freq

    with codecs.open(filename_bigrams, 'r', 'utf-8') as f:
        for line in f:
            if line:
                spl = line.split()
                w1 = "\t".join([spl[0], spl[1]])
                w2 = "\t".join([spl[2], spl[3]])
                freq = spl[4]

                n_ii = float(freq)
                n_ix = float(words[w1] + (total - words[w1]))
                n_xi = float(words[w2] + (total - words[w2]))
                n_xx = float(total)

                results["\t".join([w1, w2])] = BigramAssocMeasures.pmi(
                    n_ii, (n_ix, n_xi), n_xx
                )
    return results


def count(filename):
    cnt = Counter()

    with codecs.open(filename, 'r', 'utf-8') as f:
        for line in f:
            spl = split()
            cnt["\t".join(spl[:-1])] = spl[-1]

    return cnt


def main(filename_unigram, filename_ngram):
    res = pmi(filename_unigram, filename_ngram)
    for r in sorted(res, key=lambda elm: res[elm]):
        pstr = "%s\t%f" % (r, res[r])
        print pstr.encode('utf-8')

    # pmi(filename_unigram, filename_ngram)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
