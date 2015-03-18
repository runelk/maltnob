#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import os.path as path
import glob
from collections import Counter


# def count_ngrams_from_items(lst, n):
#     return Counter(zip(*[lst[i:] for i in range(n)]))


def make_ngrams_from_items(lst, n):
    return zip(*[lst[i:] for i in range(n)])


def extract_wordseq_ngrams(filename, n):
    current_sentence = []
    counter = Counter()

    for line in codecs.open(filename, 'r', 'utf-8'):
        spl = line.split()

        if not spl:
            if current_sentence:
                for ngr in make_ngrams_from_items(current_sentence, n):
                    # sys.stderr.write("WORDSEQ NGR: %s\n" % str(ngr))
                    counter[ngr] += 1
            current_sentence = []
        if spl:
            form = spl[1]
            cpostag = spl[3].upper()
            current_sentence += ["\t".join([form, cpostag])]
            # current_sentence += "\t".join([form, cpostag])
            # [form + " <[%s]>" % cpostag.upper()]

    return counter


def extract_deppair_ngrams(filename, n):
    deprels = []
    current_wordhash = {"0": "\t".join(["*ROOT*", "ROOT"])}
    counter = Counter()

    for line in codecs.open(filename, 'r', 'utf-8'):
        spl = line.split()
        if not spl:
            if deprels:
                for dr in deprels:
                    w_head = current_wordhash[dr[2]]
                    w_child = current_wordhash[dr[0]]
                    # counter[(w_head, w_child)] += 1

                    if n > 1:
                        counter[(w_head, w_child)] += 1
                    else:
                        counter[(w_head,)] += 1
                        counter[(w_child,)] += 1

                deprels = []
                current_wordhash = {"0": "\t".join(["*ROOT*", "ROOT"])}
        else:
            word_no = spl[0]
            head_no = spl[6]
            deprel = spl[7]
            form = spl[1]
            cpostag = spl[3].upper()
            current_wordhash[word_no] = "\t".join([form, cpostag])
            deprels += [(word_no, deprel, head_no)]

    return counter


def write_result(filename_out, cnt, cutoff=1):
    with codecs.open(filename_out, 'w', 'utf-8') as f_out:
        for k in sorted(cnt.items(), key=lambda elm: elm[1], reverse=True):
            if k[1] <= cutoff:
                break
            pstr = "%s\t%d\n" % ("\t".join(k[0]), k[1])
            # sys.stderr.write("%s\n" % str(k[0]))
            f_out.write(pstr)  # (pstr.encode('utf-8'))


def main(files, k=2, cutoff=1, wordseq=False, deppairs=False):
    # lbk_glob_str = path.join(lbk_basepath, "*/*/*.conll.dep")
    # files = glob.glob(lbk_glob_str)
    cnt_wordseqs = Counter()
    cnt_deppairs = Counter()

    flen = len(files)
    i = 1
    for filename in files:
        if wordseq:
            sys.stderr.write(
                "wordseq ngrams from %s (%d/%d)\n" % (filename, i, flen)
            )
            cnt_wordseqs += extract_wordseq_ngrams(filename, k)

        if deppairs:
            sys.stderr.write(
                "deppair ngrams from %s (%d/%d)\n" % (filename, i, flen)
            )
            cnt_deppairs += extract_deppair_ngrams(filename, k)

        i += 1

    if wordseq:
        filename_wordseqs = 'ngrams_wordseq.tsv'
        sys.stderr.write("Writing wordseq ngrams to %s\n" % filename_wordseqs)
        write_result(filename_wordseqs, cnt_wordseqs, cutoff=cutoff)

    if deppairs:
        filename_deppairs = 'ngrams_deppairs.tsv'
        sys.stderr.write("Writing deppair ngrams to %s\n" % filename_deppairs)
        write_result(filename_deppairs, cnt_deppairs, cutoff=cutoff)


if __name__ == "__main__":
    k = sys.argv[1]
    cutoff = sys.argv[2]
    # filelist = sys.argv[3:]
    lbk_basepath = sys.argv[3]
    lbk_glob_str = path.join(lbk_basepath, "*/*/*.conll.dep")
    filelist = glob.glob(lbk_glob_str)
    main(filelist, k=int(k), cutoff=int(cutoff), wordseq=True, deppairs=True)

    # main('/Users/rkn083/mystuff/corpora/lbk_conll',
    #      k=1, cutoff=1, wordseq=True, deppairs=True)
