#!/usr/bin/env sh

# See http://nil.fdi.ucm.es/maltoptimizer/userguide.html for usage details

DIR="$( cd "$( dirname "$0" )" && pwd )"
DIR_TOOLS="$DIR/tools"
DIR_MALTOPTIMIZER="$DIR_TOOLS/MaltOptimizer-1.0.3"
DIR_DATA="$DIR/data_new"
PATH_MALTPARSER="$DIR_TOOLS/maltparser-1.8.1/maltparser-1.8.1.jar"
PATH_TRAINING_CORPUS="$DIR_DATA/ndt_1-0_nob.conll"

(cd $DIR_MALTOPTIMIZER && \
	# Phase 1: Data Charact1eristics
	java -jar MaltOptimizer.jar -p 1 -m $PATH_MALTPARSER -c $PATH_TRAINING_CORPUS && \
	# Phase 2: Parsing Algorithm
	java -jar MaltOptimizer.jar -p 2 -m $PATH_MALTPARSER -c $PATH_TRAINING_CORPUS && \
	# Phase 3: Feature Models and Learning Algorithm
	java -jar MaltOptimizer.jar -p 3 -m $PATH_MALTPARSER -c $PATH_TRAINING_CORPUS)
