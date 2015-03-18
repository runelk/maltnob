#!/usr/bin/env sh

LBK_BASE_DIR="/Users/rkn083/mystuff/corpora/lbk_conll"
CUTOFF=2

python 09_extract_ngrams.py 1 $CUTOFF $LBK_BASE_DIR
mv ngrams_wordseq.tsv lbk_unigrams_wordseq.tsv
mv ngrams_deppairs.tsv lbk_unigrams_deppairs.tsv
python 09_extract_ngrams.py 2 $CUTOFF $LBK_BASE_DIR
mv ngrams_wordseq.tsv lbk_bigrams_wordseq.tsv
mv ngrams_deppairs.tsv lbk_bigrams_deppairs.tsv

python pmi.py lbk_unigrams_wordseq.tsv lbk_bigrams_wordseq.tsv > lbk_bigrams_wordseq_pmi.tsv
python pmi.py lbk_unigrams_deppairs.tsv lbk_bigrams_deppairs.tsv > lbk_bigrams_deppairs_pmi.tsv
