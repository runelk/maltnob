import sys
from subprocess import Popen, PIPE


def train(filename_train, filename_mco, maltparser_jar):
    sys.stderr.write("MaltParser jar: %s\n" % maltparser_jar)
    sys.stderr.write("Training on: %s\n" % filename_train)
    sys.stderr.write("Output: %s\n" % filename_mco)

    process = Popen(
        [
            'java', '-jar',
            maltparser_jar,
            '-i', filename_train,
            '-c', filename_mco,
            '-m', 'learn'
        ],
        stdout=PIPE,
        stderr=PIPE
    )

    return process.communicate()


def parse(filename_test, filename_mco, filename_out, maltparser_jar):
    sys.stderr.write("MaltParser jar: %s\n" % maltparser_jar)
    sys.stderr.write("Parsing %s\n" % filename_test)
    sys.stderr.write("Model: %s\n" % filename_mco)
    sys.stderr.write("Output: %s\n" % filename_out)

    process = Popen(
        [
            'java', '-jar',
            maltparser_jar,
            '-c', filename_mco,
            '-i', filename_test,
            '-o', filename_out,
            '-m', 'parse'
        ],
        stdout=PIPE,
        stderr=PIPE
    )

    return process.communicate()


def evaluate(filename_test, filename_result):
    sys.stderr.write(
        "Comparing %s with Maltparser result %s\n" %
        (filename_test, filename_result)
    )
