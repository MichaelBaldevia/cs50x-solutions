import csv
import sys


def main():

    #Check for command-line usage
    if len(sys.argv) != 3:
     {
        exit()
     }

    #Read database file into a variable
    dnas = []
    with open(sys.argv[1] , "r") as strs:
        reader = csv.DictReader(strs)
        for row in reader:
            dnas.append(row)


    #Read DNA sequence file into a variable
    sequence = open(sys.argv[2], "r")
    dna_sequence = sequence.read()

    #Find longest match of each STR in DNA sequence

    #Check for STR column count
    #For long STR
    if (len(dnas[1].keys()) > 4):
        subsequence = ['AGATC' ,'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    #For short STR
    else:
        subsequence = ['AGATC', 'AATG', 'TATC']

    #Collect STR counts
    str_count = []
    for key in subsequence:
        str_count.append(longest_match(dna_sequence, key))

    #Check database for STR profiles
    for key in dnas:
        if (len(subsequence) > 4):
            if  (int(key["AGATC"]) == str_count[0] and int(key["TTTTTTCT"]) == str_count[1] and int(key["AATG"]) == str_count[2] and int(key["TCTAG"]) == str_count[3] and int(key["GATA"]) == str_count[4] and int(key["TATC"]) == str_count[5] and int(key["GAAA"]) == str_count[6] and int(key["TCTG"]) == str_count[7]):
                print(key["name"])
                exit()
        else:
            if  (int(key["AGATC"]) == str_count[0] and int(key["AATG"]) == str_count[1] and int(key["TATC"]) == str_count[2]):
                print(key["name"])
                exit()

    print("No match")

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

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
