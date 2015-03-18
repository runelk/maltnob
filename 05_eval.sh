#!/usr/bin/env sh

java -jar ./tools/dist-20141005/lib/MaltEval.jar \
     -s ./data_new/ndt_1-0_nob.conll.parsed.00 \
     ./data_new/ndt_1-0_nob.conll.parsed.01 \
     ./data_new/ndt_1-0_nob.conll.parsed.02 \
     ./data_new/ndt_1-0_nob.conll.parsed.03 \
     ./data_new/ndt_1-0_nob.conll.parsed.04 \
     ./data_new/ndt_1-0_nob.conll.parsed.05 \
     ./data_new/ndt_1-0_nob.conll.parsed.06 \
     ./data_new/ndt_1-0_nob.conll.parsed.07 \
     ./data_new/ndt_1-0_nob.conll.parsed.08 \
     ./data_new/ndt_1-0_nob.conll.parsed.09 \
     -g ./data_new/ndt_1-0_nob.conll.00 \
     ./data_new/ndt_1-0_nob.conll.01 \
     ./data_new/ndt_1-0_nob.conll.02 \
     ./data_new/ndt_1-0_nob.conll.03 \
     ./data_new/ndt_1-0_nob.conll.04 \
     ./data_new/ndt_1-0_nob.conll.05 \
     ./data_new/ndt_1-0_nob.conll.06 \
     ./data_new/ndt_1-0_nob.conll.07 \
     ./data_new/ndt_1-0_nob.conll.08 \
     ./data_new/ndt_1-0_nob.conll.09 \
     > evaluation_report.txt
