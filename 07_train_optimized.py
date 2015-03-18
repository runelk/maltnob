#!/usr/bin/env python

import sys
import maltnob.maltparser as mp
import os.path as path


def main(conll_filename, k=10,
         maltparser_jar='tools/maltparser-1.8.1/maltparser-1.8.1.jar'):
    mp.train(
        'data_new/data_new/ndt_1-0_nob.conll',
        'ndt_full_optimized',
        maltparser_jar
    )

if __name__ == "__main__":
    main(sys.argv[1])
