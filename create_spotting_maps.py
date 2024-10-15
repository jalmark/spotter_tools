# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Fri Mar  1 14:56:51 2024
Last modified 15.10.2024

@author: Jalmari Kettunen

This Python script creates a 4 x 16 array that has integers 1 to N in random order. It also counts how many times each number occurs in the array.
Finally, the script prints the array and the frequencies for the user.

Prompt for ChatGPT 3.5 which was the starting point of this:
Print me an 4 x 16 array. Each position in the array has an integer between 1  and 10. Order of integers in the array is as close to random as possible. Each integer appears approximately the same number of times in the array. Finally, print me how many times each integer appear in the array
"""


import numpy as np

# Initialize the array with zeros
array = np.zeros((4, 16), dtype=int)

# Generate a list of integers between 1 and N. Change N to desired integer!
N = 10
integers = np.random.randint(1, 10+1, size=(4 * 16))

# Shuffle the list of integers
np.random.shuffle(integers)

# Populate the array with the shuffled integers
array = integers.reshape((4, 16))

# Count the occurrences of each integer in the array
counts = np.bincount(array.flatten())

print(array)
print("Number of occurrences of each integer in the array:")
for i, count in enumerate(counts[1:]):
    print(f"Integer {i+1}: {count}")
