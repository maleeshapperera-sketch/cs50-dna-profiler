# cs50-dna-profiler
DNA - CS50 Problem Set 6
A forensic DNA profiling program that identifies individuals by matching Short Tandem Repeats (STRs) in their DNA sequences.

🧬 The Problem
Given a CSV file containing DNA profiles (names and STR counts) and a text file containing a DNA sequence, this program identifies whose DNA matches the sequence.

🔬 How It Works
Reads the database - CSV with STR headers and counts for each person

Analyzes the DNA sequence - Counts consecutive repeats for each STR type

Compares and identifies - Finds the person whose STR counts exactly match

STR Analysis Example
text
Pattern: "AGAT"
Sequence: "AGATAGATAGAT" → Count = 3
📁 Files
dna.py - Main Python program

databases/ - CSV files with STR profiles (small.csv, large.csv)

sequences/ - TXT files containing DNA sequences

🛠️ Implementation Details
Agrep-style matching without regex libraries

Sliding window pattern detection for STR repeats

Dictionary-based data structure for profile storage

Command-line argument validation

🚀 Usage
bash
python dna.py databases/small.csv sequences/1.txt
python dna.py databases/large.csv sequences/5.txt
📊 Sample Output
text
Harry
# or "No match" if not found
✅ Validation
Correctly identifies matches in small database (8 people)

Correctly identifies matches in large database (100+ people)

Handles no-match cases properly
