import codecs
import sys


def corpus_partition_filename(i, base_filename):
    return "%s.%02d" % (base_filename, i)


def corpus_partition_filenames(k, base_filename):
    for i in range(0, k):
        yield corpus_partition_filename(i, base_filename)


def corpus_partition_files(k, base_filename, output_enc='utf-8'):
    for filename in corpus_partition_filenames(k, base_filename):
        yield codecs.open(filename, 'w', output_enc)


def join_partitions(partition_numbers, base_filename, output_filename,
                    input_enc='utf-8', output_enc='utf-8'):
    with codecs.open(output_filename, 'w', output_enc) as f_out:
        for i in partition_numbers:
            partition_filename = corpus_partition_filename(i, base_filename)
            with codecs.open(partition_filename, 'r', input_enc) as f_in:
                f_out.write(f_in.read())


def make_corpus_partitions(k, filename, input_enc='utf-8'):
    f = codecs.open(filename, 'r', input_enc)
    lines = sum(1 for line in f)  # Total line count in original
    partition_size = lines / k    # Approx. size (lines) of one partition
    f.seek(0)                     # Rewind file pointer

    # File generator for k partitions
    partition_filenames = corpus_partition_files(k, filename)
    pf = next(partition_filenames)  # Get first partition file

    i = 0
    for line in f:
        i += 1
        pf.write(line)

        # If we've reached the approx. size limit of one partition,
        # and we're at end-of-sentence (i.e. blank line)
        if i >= partition_size and not line.strip():
            sys.stderr.write("Done writing partition %s\n" % pf.name)
            pf.close()  # Done with this partition
            i = 0       # Reset partition size counter

            # Continue on next partition file
            pf = next(partition_filenames)

    sys.stderr.write("Done writing partition %s\n" % pf.name)
    pf.close()  # Make sure the last file was closed


def make_train_and_test_partition(k, test_partition, filename,
                                  input_enc='utf-8', output_enc='utf-8'):
    filename_train = "%s.train.%02d" % (filename, test_partition)
    filename_test = "%s.test.%02d" % (filename, test_partition)

    sys.stderr.write(
        "Creating train/test partitions from %s (test partition: %d)\n" %
        (filename, test_partition)
    )

    with codecs.open(filename_train, 'a', output_enc) as f_train:
        with codecs.open(filename_test, 'w', output_enc) as f_test:
            for i in range(0, k):
                with codecs.open(corpus_partition_filename(i, filename),
                                 'r', input_enc) as f_partition:
                    content = f_partition.read()
                    if i == test_partition:
                        sys.stderr.write("Writing %s to %s\n" %
                                         (f_partition.name, f_test.name))
                        f_train.write(content)
                    else:
                        sys.stderr.write("Writing %s to %s\n" %
                                         (f_partition.name, f_train.name))
                        f_test.write(content)

    return filename_train, filename_test


def make_train_and_test_partitions(k, filename):
    for i in range(0, k):
        filename_train, filename_test = make_train_and_test_partition(k, i, filename)
