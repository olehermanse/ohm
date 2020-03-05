#!/bin/sh
#
# Automatically check formatting before commiting, to enable:
#   cp -a pre-commit.sh .git/hooks/pre-commit

prettier --check *.html || (echo "Run: prettier --write *.html" ; exit 1)
