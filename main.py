#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Esteban Quintana
# Javier Rodríguez
# Tree

#main
from id3 import *
from node import Node

def build_tree(data_frame, data_types):
    root = Node(data_frame[0][-1], None, [], None, len(data_frame[0]) -1, data_frame, None, data_frame[0][-1])
    id3(root, root, data_types, [])
    root.show_tree(-1)
    return 0

if __name__ == "__main__":
    data_frame = []
    attributes = []
    data_types = {}
    data = []
    data_lines = False

    for line in fileinput.input():

        if "@attribute" in line:
            aux =re.split("[ \t]+|[ \t]+$", line, 2)
            attributes.append(aux[1])
            aux[2] = aux[2].replace('{', "").replace('}', "").replace(' ', "").replace('\n', "")
            entropies = aux[2].split(',')
            data_types[aux[1]] = entropies
        if data_lines:
            if not "%" in line:
                new_line = line.replace('\n', "")
                entropies = new_line.split(',')
                data.append(entropies)
        if "@data" in line:
            data_lines = True

    data_frame.append(attributes)
    for d in data:
        data_frame.append(d)
    build_tree(data_frame, data_types)
