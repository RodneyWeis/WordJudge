#!/usr/bin/env python
# judge.py

import sys

# Choose the source file
path = "lexicon/wordlist.txt"

# Open the source file
text_file = open(path, "r")

# Assign the contents of the source file to words
words = text_file.readlines()

# Parse candidate words from the command line arguments
candidates = sys.argv[1:]

print("Words to be checked: " + str(candidates))

valid = True

# iterate over all of the candidate words
for candidate in candidates:
    word = candidate.upper()
    word = word + "\n"
#   print("Trying word: " + word)
    try:
        test = (words.index(word))
#       print(test)
    except ValueError:
        valid = False

if (valid):
    print("The play is acceptable")
else:
    print("The play is NOT acceptable")






# Close the source file
text_file.close()