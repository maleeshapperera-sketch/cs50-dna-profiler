import csv
import sys

def main():
    
    # TODO:check for command-line usage
    if len(sys.argv) != 3:
        print("usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
     reader1 = csv.DictReader(file)
     print(reader1.fieldnames)
     columns=reader1.fieldnames

    rows = []
    with open(sys.argv[1]) as file:
      reader2 = csv.DictReader(file)
      for row in reader2:
        rows.append(row) 
    temp=[]
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        sequence = file.read()
        
            
    # TODO: Find longest match of each STR in DNA sequence
    for i in range(1,len(columns)):
        temp.append(longest_match(sequence, columns[i]))
    # TODO: Check database for matching profiles
    for i in range(len(rows)):
        # FIXED: Compare each STR value individually
        match = True
        for j in range(1, len(columns)):
            if int(rows[i][columns[j]]) != temp[j-1]:
                match = False
                break
        if match:
            print(rows[i]["name"])
            return
        
    # FIXED: Removed else clause that was attached to for loop incorrectly
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length
            
            # FIXED: Add bounds checking to prevent index error
            if end > sequence_length:
                break

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
