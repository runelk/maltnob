#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path as path
import glob
from subprocess import Popen, PIPE

# Usage: python 08_parse_lbk.py <LBK_BASEPATH>
#        LBK_BASEPATH should be the top-level directory of the LBK corpus (the CONLL version)


# java -jar tools/maltparser-1.8.1/maltparser-1.8.1.jar -f finalOptionsFile.xml -m parse -c ndt_nob_optimized -i data_new/lbk/SA02SaJo01.conll -o data_new/lbk/SA02SaJo01.dep.conll


def make_popen_args(conll_filename,
                    maltparser_jar='tools/maltparser-1.8.1/maltparser-1.8.1.jar',
                    maltparser_mco='ndt_nob_optimized',
                    maltparser_config='finalOptionsFile.xml'):
    filename_out = conll_filename + ".dep"
    return [
        'java', '-jar',
        maltparser_jar,
        '-c', maltparser_mco,
        '-i', conll_filename,
        '-o', filename_out,
        '-m', 'parse'
    ]


def main(lbk_basepath):
    lbk_glob_str = path.join(lbk_basepath, "*/*/*.conll")
    files = glob.glob(lbk_glob_str)
    print lbk_glob_str
    for filename in files:
        if path.isfile(filename + '.dep'):
            continue
        sys.stderr.write("Parsing %s\n" % filename)
        popen_args = make_popen_args(filename)
        process = Popen(popen_args, stdout=PIPE, stderr=PIPE)
        process.communicate()


if __name__ == "__main__":
    main(sys.argv[1])
