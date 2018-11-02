#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Esteban Quintana
# Javier Rodríguez
# Tree

#id3
# Information gain
# Greater gain

import re
import fileinput
import math
import copy
from node import Node
from main import *

def calculate_entropy(node, root, data_types):
    entropies = []
    entropy = 0.0
    denominator = len(node.data_frame) - 1
    for element in data_types[root.name]:
        counter = 0
        for i in range(1, denominator + 1):
            if element == node.data_frame[i][root.number]:
                counter += 1
        if counter > 0:
            e_entropy = -((counter/denominator) * math.log(counter/denominator, 2))
        else:
            e_entropy = 0
        entropies.append(e_entropy)
    for e in entropies:
        entropy += e

    return entropy

# id3 Alg
def id3(node, root, data_types, visited):
    node.entropy = calculate_entropy(node, root, data_types)
    new_list = copy.deepcopy(visited)
    if float(node.entropy) == 0.0:
        node.answer = node.data_frame[1][-1]
        return 0
    gains = {}
    for i in range(0, len(node.data_frame[0]) -1):
        if i not in visited:
            next_node = Node(node.data_frame[0][i], None, None, node, i, node.data_frame, None, None)
            gains[node.data_frame[0][i]] = information_gain(node, next_node, root, data_types)
    split_to_node = greater_gain(gains)
    new_number = root.data_frame[0].index(split_to_node)
    new_list.append(new_number)

    for element in data_types[split_to_node]:
        new_data_frame = []
        new_data_frame.append(root.data_frame[0])
        new_node = Node(element, None, [], node, new_number, None, None, node.data_frame[0][new_number])
        for row in node.data_frame:
            if row[new_number] == element:
                new_data_frame.append(row)
        new_node.data_frame = new_data_frame
        node.children.append(new_node)
        id3(new_node, root, data_types, new_list)
    return 0

def greater_gain(gains):
    current_greater = 0.0
    for g in gains:
        if gains[g] > current_greater:
            current_greater = gains[g]
            for g in gains:
                if gains[g] == current_greater:
                    return g

def information_gain(actual_node, next_node, root, data_types):

                        gain = 0.0
                        entropy = 0.0
                        values = []
                        gains = {}
                        for key in data_types.keys():

                            if key == next_node.name:
                                for datatype in data_types[key]:
                                    aux_data = []
                                    aux_data.append(root.data_frame[0])
                                    for i in range(1, len(next_node.data_frame)):

                                        if next_node.data_frame[i][next_node.number] == datatype:
                                            aux_data.append(next_node.data_frame[i])
                                            new_node = Node(next_node.name, None, None, next_node, next_node.number, aux_data, None, None)
                                            val = calculate_entropy(new_node, root, data_types)
                                            val = val * ((len(new_node.data_frame) - 1) / (len(root.data_frame) -1) )

                                            values.append(val)
                                            for element in values:
                                                entropy += element
                                                gain = actual_node.entropy - entropy
                                                return gain
