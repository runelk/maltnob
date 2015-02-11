# MaltNob #
Python library and scripts for training and crossvalidating MaltParser using [NDT](http://www.nb.no/Tilbud/Forske/Spraakbanken/Tilgjengelege-ressursar/Tekstressursar) as training data.

NB: This is work-in-progress, proof-of-concept, specialized for one
and only one project, and so forth. Don't use it for anything
important.

# Installation #

In your preferred projects directory, clone the repo:
```
git clone git@github.com:runelk/maltnob.git
```

Run `download.sh` to get required tools and datasets:
```
sh download.sh
```

# Folders #

## ./data/ ##

Folder for the neccessary data sources.

## ./maltnob/ ##

Python library for customized training, parsing and crossvalidating
MaltParser on NDT, along with some corpus partitioning functionality.

## ./tools/ ##

Various tools neccessary to run this stuff.

# Scripts #
## download.sh ##

Download and unpack data and tools to the correct subdirectories.

## crossvalidate.py ##

Does a 10-fold cross validation for MaltParser using NDT as training
data (WIP).

## train.py ##

Train MaltParser on something (WIP).

## parse.py ##

Use MaltParser to parse something (WIP).
