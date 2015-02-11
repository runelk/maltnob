#!/usr/bin/env sh

DIR="$( cd "$( dirname "$0" )" && pwd )"
TOOLS_DIR="$DIR/tools"
DATA_DIR="$DIR/data"
NDT_DIR="$DATA_DIR/ndt"

echo "Creating directories for tools...\n"
mkdir -p $TOOLS_DIR

echo "Creating directories for data...\n"
mkdir -p $NDT_DIR

echo "Downloading and extracting MaltParser v1.8.1 ...\n"
curl http://maltparser.org/dist/maltparser-1.8.1.tar.gz | tar xvz -C $TOOLS_DIR

echo "Downloading and extracting MaltOptimizer v1.0.3 ...\n"
curl http://nil.fdi.ucm.es/maltoptimizer/MaltOptimizer-1.0.3.tar.gz | tar xvz -C $TOOLS_DIR

echo "Downloading and extracting NDT v1.0.1 ...\n"
curl http://www.nb.no/sbfil/tekst/20140328_NDT_1-01.tar.gz | tar xvz -C $NDT_DIR



