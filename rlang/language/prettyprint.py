#!/usr/bin/env python

import sys
from nltk import Tree


def print_tree(st):
    st = st.replace('indent', '')
    st = st.replace('dedent', '')
    st = st.replace('newLine', '')
    st = st.replace(':', '(COL :)')
    tree = Tree.fromstring(st)
    tree.pretty_print()


data = sys.stdin.read()
print_tree(data)
