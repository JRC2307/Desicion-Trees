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

def get_entropy(node, root, data_types):
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
    new_list = copy.deepcopy(visited)
    node.entropy = get_entropy(node, root, data_types)
    #print(node)
    if float(node.entropy) == 0.0:

        #print("LEAF NODE")
        node.answer = node.data_frame[1][-1]
        #print(node.answer)
        return 0
    #print("entropy " + str(node.entropy))
    gains = {}
    #print(node.data_frame)
    for i in range(0, len(node.data_frame[0]) -1):
        if i not in visited:
            next = Node(node.data_frame[0][i], None, None, node, i, node.data_frame, None, None)
            gains[node.data_frame[0][i]] = information_gain(node, next, root, data_types)

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

def information_gain(actual_node, next, root, data_types):
    gain = 0.0
    entropy = 0.0
    entropies = []
    
    for k in data_types.keys():
        if k == next.name:
            for datatype in data_types[k]:
                aux = []
                aux.append(root.data_frame[0])
                for i in range(1, len(next.data_frame)):
                    if next.data_frame[i][next.number] == datatype:
                        aux.append(next.data_frame[i])
                n = Node(next.name, None, None, next, next.number, aux, None, None)
                en = get_entropy(n, root, data_types)
                en = en * ((len(n.data_frame) - 1) / (len(root.data_frame) -1) )

                entropies.append(en)
            for e in entropies:
                entropy += e
            gain = actual_node.entropy - entropy
    return gain
