#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import maltnob.maltparser as mp
import os.path as path


def run_parsers(k, filename,
                maltparser_jar='tools/maltparser-1.8.1/maltparser-1.8.1.jar'):
    for i in range(0, k):
        filename_test = "%s.test.%02d" % (filename, i)
        filename_mco = "%s-%02d" % (path.basename(filename), i)
        filename_parsed = "%s.parsed.%02d" % (filename, i)
        stdout, stderr = mp.parse(
            filename_test, filename_mco, filename_parsed, maltparser_jar
        )
        print stdout
        print stderr


def main(conll_filename, k=10):
    run_parsers(k, conll_filename)

if __name__ == "__main__":
    main(sys.argv[1])
