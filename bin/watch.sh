#!/bin/bash

# executes 'make html' whenever a file is changed

# fswatch
# -e '.#': ignore temporary files written by emacs
# -l 0.5: set latemcy to 0.5 seconds
# -0: delimiter
# -o: print a count of events instead of listing modified files

# xargs
# -n 1: invoke 'make html' with each line taken from stdin
# -I {}: effectively prevets stdin from being included as argument

fswatch -e output -e '.#' -e .git -l 0.5 -o . | \
    xargs -n 1 -I {} make html
