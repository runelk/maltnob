#!/usr/bin/env python

import sys
import maltnob.maltparser as maltparser

MALTPARSER_JAR = 'tools/maltparser-1.8.1/maltparser-1.8.1.jar'


# Usage: python train.py <CONLL_FILE> <MCO_FILE>
def main():
    stdout, stderr = maltparser.train(sys.argv[1], sys.argv[2], MALTPARSER_JAR)
    print stderr
    print stdout

if __name__ == "__main__":
    main()
