DES-S1-Differential-Cryptanalysis

This repo has everything I used for my CS 538 project where I tested how small input changes affect the output of the DES S1 substitution box. I ran the experiment in Python, collected the results, and used them in my paper and presentation.

What’s in this repo

Code

sbox_diff_demo.py - It does two things:

Runs the differential experiment for a chosen ΔX

Runs a small key-space reduction demo that scores all 64 possible 6-bit S1 subkeys

The S1 lookup table in the file is the exact table from the DES standard.

Data

These are the raw results the script printed when I ran the ΔX tests:

results_delta_1_run1.txt

results_delta_1_run2.txt

results_delta_2_run1.txt

results_delta_2_run2.txt

Each file shows how often each output difference (ΔY) appeared out of 20,000 trials.

How to recreate my experiment

Install Python 3

Open sbox_diff_demo.py

Change this line depending on the ΔX you want:

# For ΔX = 1
delta_in = 0b000001

# For ΔX = 2
delta_in = 0b000010


Make sure trials are set to 20,000:

num_trials = 20000


Run the script:

python sbox_diff_demo.py


It prints the differential results and the key-space scores to the console.

If you want to save output:

python sbox_diff_demo.py > results.txt


That’s all that’s needed to reproduce everything I used in my paper.