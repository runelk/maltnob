#!/usr/bin/env python

import sys
import os.path as path
import codecs
import maltnob.maltparser as maltparser
import maltnob.partitions as partitions

INPUT_ENC = 'utf-8'
OUTPUT_ENC = 'utf-8'
MALTPARSER_JAR = 'tools/maltparser-1.8.1/maltparser-1.8.1.jar'
FILENAME_MCO = 'test_kfold'
NDT_NOB_CONLL_FILENAME = 'data/ndt/NDT_1-01/ndt_1-0_nob.conll'
K = 10

def strip_test(line, at=6):
    return "\t".join(line.strip().split()[0:at])


def write_report(filename):
    sys.stderr.write("Writing report to %s" % filename)


def cleanup(filename):
    sys.stderr.write("Cleaning up after all this mess.")


def make_models(k, filename, maltparser_jar=MALTPARSER_JAR):
    for i in range(0, k):
        filename_train = "%s.train.%02d" % (filename, i)
        filename_mco = "%s-%02d" % (path.basename(filename), i)
        stdout, stderr = maltparser.train(filename_train, filename_mco, maltparser_jar)
        print stdout
        print stderr

def run_parsers(k, filename, maltparser_jar=MALTPARSER_JAR):
    for i in range(0, k):
        filename_test = "%s.test.%02d" % (filename, i)
        filename_mco = "%s-%02d" % (path.basename(filename), i)
        filename_parsed = "%s.parsed.%02d" % (filename, i)
        stdout, stderr = maltparser.parse(filename_test, filename_mco, filename_parsed, maltparser_jar)
        print stdout
        print stderr

# def run_cross_validation(k, filename, maltparser_jar=MALTPARSER_JAR):
#     make_models(k, filename, maltparser_jar)
#     run_parsers(k, filename, maltparser_jar)
    # for i in range(0, k):
    #     filename_train = "%s.train.%02d" % (filename, i)
    #     filename_mco = "%s-%02d" % (path.basename(filename), i)
    #     stdout, stderr = maltparser.train(filename_train, filename_mco, maltparser_jar)
    #     print stdout
    #     print stderr
        # result_train = maltparser.train(filename_train, filename_mco, maltparser_jar)
        # result_parse = maltparser.parse(filename_test, filename_mco, "testest", maltparser_jar)

        # print result_train
        # print result_parse
        # print result_evaluate

    # for i in range(0, k):
    #     result_evaluate = maltparser.evaluate("%s.test", result_parse)

def evaluate_parsed(filename_parsed, filename_test, input_enc='utf-8'):
    with codecs.open(filename_parsed, 'r', input_enc) as f_parsed:
        with codecs.open(filename_test, 'r', input_enc) as f_test:
            lines_parsed = f_parsed.readlines()
            lines_test = f_test.readlines()

            # Sanity check (line count should be equal)
            if len(lines_parsed) != len(lines_test):
                raise Exception(
                    "Line count mismatch (%d:%d)" % (len(lines_parsed), len(lines_test))
                )

            eq_lines = 0
            neq_lines = 0

            for i in range(0, len(lines_parsed)):
                if lines_parsed[i] == lines_test[i]:
                    eq_lines += 1
                else:
                    neq_lines += 1

            print "%s\t%d\t%d\t%f" % (
                filename_parsed, eq_lines, neq_lines,
                100.0 - (float(neq_lines) / float(len(lines_parsed))) * 100.0
            )


def evaluate_all_parsed(k, conll_filename):
    for i in range(0, K):
        filename_parsed = "%s.parsed.%02d" % (conll_filename, i)
        filename_test = "%s.test.%02d" % (conll_filename, i)
        evaluate_parsed(filename_parsed, filename_test)


def main(conll_filename=NDT_NOB_CONLL_FILENAME):
    partitions.make_corpus_partitions(K, conll_filename)
    partitions.make_train_and_test_partitions(K, conll_filename)
    make_models(K, conll_filename, MALTPARSER_JAR)
    run_parsers(K, conll_filename)
    evaluate_all_parsed(K, conll_filename)


if __name__ == "__main__":
    main()
