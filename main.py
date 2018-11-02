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
            str = re.split(' ', line, 2)
            str.pop(0)
            attributes.append(str[0])
            str[1] = str[1].replace('\n', "").replace('{', "").replace('}', "").replace(' ', "")
            values = str[1].split(',')
            data_types[str[0]] = values
        if data_lines:
            aux_line = line.replace("\n", "")
            values = aux_line.split(',')
            data.append(values)
        if "@data" in line:
            data_lines = True
    data_frame.append(attributes)
    for d in data:
        data_frame.append(d)
    build_tree(data_frame, data_types)
