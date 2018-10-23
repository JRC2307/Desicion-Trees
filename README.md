
**Esteban Quintana**
**Javier Rodríguez**


https://www.alphagrader.com/courses/17/assignments/165

Goal: learn how to use data mining tools to rapidly test and make experiments with several machine learning algorithms.
Size of teams: each team must be made up of at most 2


# Overview

  -  Download and install WEKA.
  -  Use WEKA to learn and visualize a decision tree. The objective is to learn to use the software and understand what the tool is doing since you will be using this later on in the course. See instructions below.
  -  Create your own implementation of ID3. See instructions below.
  -  Search for an appropriate data here. Check that the type of file matches WEKA’s sintaxis or reformat it to match WEKA’s .arff format. Check the output of your implementation against that of WEKA.

## WEKA

Weka tutorial for Decision Trees lab. (Thanks to Eduardo Vaca!)

  1.  Download Weka tool
  2. When launching it you have to choose between different modes of the tool. Choose ‘Explore’, there is a button for it
  3.  To load a dataset click on the button ‘Open File’
  4.  The test dataset from lab in arff can be found here
  5.  You can use this file for learning how to use the tool
  6.  After loading the dataset, to visualize the tree go to the tab “Classify”
  7.  In that tab you must choose a classifier (there a button on the top of the pague that says ‘Choose’)
  8.  A list of classifiers will be displayed, go to the ‘trees’ folder and select J48
  9.  Then, in the test options select ‘use training set’ and then click ‘Start’
  10.  A new record should appear on the Result list box, right click on that record and select ‘Visualize tree’
  11.  The decision tree should appear in its graphical representation

### Report

Write a 400-500 word report that includes the following points:

    - Explain the advantages and disadvantages of writing a program on your own vs using a pre-created suite such as WEKA.
    - Explain what criteria you followed to choose the datasets for your tree and the WEKA tests.
    - Include the graphics of the trees or part of the trees you generated in WEKA and your own program. Are they different, and if so, why?
    - Based in what you have learned so far where would you use decision trees?

### Evaluation

- Based on: WEKA trees, Implementation of ID3
- reate your own implementation of ID3

For this lab, you're going implement the ID3 algorithm to build a decision tree based on a dataset.
Objective

Your assignment is to build a program that reads a dataset in ARFF format, and construct a decision tree using the ID3 algorithm.
Input/Output

Your program must read from stdin and output to stdout. See here for instructions how to do this.

Basically, your program will be called by executing run < [problem_file], where problem_file is a file describing the problem (see below). Your program should output the solution as text to the terminal.

#### IMPORTANT: A number of testcases are provided in the testcase directory. Make sure your program gives the exact same output on the testcases.
Input

The input is given in the ARFF format. For details, see here. For examples, see the testcase directory.

  1.  All attributes will be nominal (categories), not continuous.
  2.  The final attribute is the output field.
  3.  All other attributes are input.

Output

Output consists of the hierarchical tree, one node per line. A node is either an internal node (a node with one or more children), or a leaf node.

These nodes should be shown in your output as follows:

    1. A leaf node is an ANSWER node, and should be shown in your output as: ANSWER: [output]. This is saying that the result of following the path gives the answer output (for example yes, no, maybe).
    2. An internal node is a decision node: [attribute]: [value]. For example: outlook: sunny. This means that the attribute outlook is set to sunny.

There are a number of extra requirements:

    All nodes need to be indented with 2 * depth spaces. So the decision nodes at root level are indented with 0 spaces, and an leaf node at depth 10 with 20 spaces.
    Decision nodes need to be ordered based on the occurrence of their value in the ARFF file. For example, if the attribute outlook appears in the ARFF file as @attribute outlook {sunny, overcast, rainy}, then the decision nodes for that attribute should appear in the order sunny, overcast and rainy.

Example

The following example encodes a very simple dataset for the OR function:

```
@relation or

@attribute A {TRUE, FALSE}
@attribute B {TRUE, FALSE}
@attribute AorB {TRUE, FALSE}

@data
TRUE,TRUE,TRUE
FALSE,FALSE,FALSE
TRUE,FALSE,TRUE
FALSE,TRUE,TRUE

Output:

A: TRUE
  ANSWER: TRUE
A: FALSE
  B: TRUE
    ANSWER: TRUE
  B: FALSE
    ANSWER: FALSE
```

More examples can be found under testcases tab above.
