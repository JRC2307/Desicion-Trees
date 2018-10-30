#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Esteban Quintana
# Javier Rodríguez
# Tree

#ID3

# Entropy calc
# Information gain
# Greater gain

## Main
#Read file

import re
import fileinput


class Node:
    def __init__(self, name, entropy, children, father, number, data_frame, answer, column):
        self.entropy = entropy
        self.name = name
        self.children = children
        self.father = father
        self.number = number
        self.data_frame = data_frame
        self.answer = answer
        self.column = column

    def set_entropy(self, ent):
        self.entropy = ent

    def set_children(self, c):
        self.children.append(c)

    def set_father(self, f):
        self.father = f

    def show_tree(self, spaces):
        if self.name != self.data_frame[0][-1]:
            print("  " * spaces + self.column + ": " +self.name)
        if self.answer:
            print ("  " * spaces + "  " +  "ANSWER: " + self.answer)
        for child in self.children:
            child.show_tree(spaces + 1)


def greater_gain(gains):
    current_greater = 0.0
    for g in gains:
        if gains[g] > current_greater:
            current_greater = gains[g]
    for g in gains:
        if gains[g] == current_greater:
            return g


def build_tree(data_frame, data):
    root = Node(data_frame[0][-1], None, [], None, len(data_frame[0]) -1, data_frame, None, data_frame[0][-1])


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
    print(data_frame)
    build_tree(data_frame, data_types)
