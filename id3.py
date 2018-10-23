#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Esteban Quintana
# Javier Rodríguez
import re
import fileinput

# Node def
# Node Parser
def parser():
    attributes = []
    atrr = []
    val_list = []
    for read in fileinput.input():
        if "@attribute" in read:
            attributes = re.split("[ \t]+|[ \t]+$", read,2)
            attributes[2] = attributes[2].replace('{', "").replace('}', "").replace(' ', "").replace("\n", "")
            attr = append.attributes[1]
            val = append.attributes[2].split(",")
            for v in val:
                val_list.append(v)



    return
# Tree

#ID3

# Entropy calc
# Information gain
# Greater gain

## Main
#Read file
