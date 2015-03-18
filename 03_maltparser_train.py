#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import maltnob.maltparser as mp
import os.path as path


def make_models(k, filename,
                maltparser_jar='tools/maltparser-1.8.1/maltparser-1.8.1.jar'):
    for i in range(0, k):
        filename_train = "%s.train.%02d" % (filename, i)
        filename_mco = "%s-%02d" % (path.basename(filename), i)
        stdout, stderr = mp.train(
            filename_train, filename_mco, maltparser_jar
        )
        print stdout
        print stderr


def main(conll_filename, k=10):
    make_models(k, conll_filename)

if __name__ == "__main__":
    main(sys.argv[1])
