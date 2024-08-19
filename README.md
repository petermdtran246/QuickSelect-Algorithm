# QuickSelect Algorithm in Python
## Overview
This repository contains a Python implementation of the QuickSelect algorithm, which is used to find the k-th smallest element in an unsorted array. The QuickSelect algorithm is an efficient selection algorithm that works in average-case O(n) time.

## Features
  -  QuickSelect Function: Implements the QuickSelect algorithm to find the k-th smallest element in an array.
  -  Random Array Generation: Generates a random array of 1000 unique elements within a specified range.
  -  User Input: Prompts the user to input the value of k to find the k-th smallest element in the array.

## QuickSelect Algorithm
The QuickSelect algorithm is a selection algorithm that, given an array, finds the k-th smallest element. It works similarly to the QuickSort algorithm, using the partitioning method but only recurses into the partition containing the k-th smallest element.

## Key Concepts
  -  Partitioning: The array is partitioned around a pivot element, such that elements less than the pivot come before it, and elements greater come after it.
  -  Recursion: The algorithm then recurses only into the partition that contains the k-th smallest element.

## Files
  -  main.py: The entry point of the program. It generates the random array, takes user input, and finds the k-th smallest element.
  -  quick_select.py: Contains the implementation of the QuickSelect algorithm and helper functions.
