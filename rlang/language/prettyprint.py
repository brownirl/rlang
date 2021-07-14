#!/usr/bin/env python

import sys
from nltk import Tree


def print_tree(st):
    tree = Tree.fromstring(st)
    tree.pretty_print()


data = sys.stdin.read()
print_tree(data)
