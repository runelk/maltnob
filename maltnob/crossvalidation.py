

# leave-​​one-​​out cross-validation (LOOCV)
# accuracy measures are obtained as follows:

def mean_square_error(stuff):
    pass


def k_fold_evaluate(test_set, result):
    pass


# Compute the MSE from e_1^*, ...,e_n^*

def k_fold(partitions, f_train, f_test):
    """ Leave-one-out cross-validation. """

    for i in range(len(partitions)):
        # Let partition i form the test set
        test_set = partitions[i]
        # Let all partitions except partition i form the training set
        train_set = partitions[:i] + partitions[i+1:]
        # train the model using the other partitions
        f_train(train_set)
        # run the trained model on the test set
        result = f_test(test_set)
        # compute the error ( e_i^* = y_i - hat(y)_i ) for the omitted observation.
        k_fold_evaluate(test_set, result)
