# judge.py

# Choose the source file
path = "lexicon/wordlist.txt"

# Open the source file
text_file = open(path, "r")

# Assign the contents of the source file to words
words = text_file.readlines()

# Calculate the length of the source file
words_length = (len(words))

print ("There are " + str(words_length) + " words.")


candidate = "RODNEYS\n"
print("The candidate is " + candidate)

valid = True


# TODO:  make this a function
# TODO:  iterate over one or multiple words
if (valid == True):
    try:
        test = (words.index(candidate))
    except ValueError:
        valid = False
    else:
        valid = True
if (valid):
    print("The play is acceptable")
else:
    print("The play is NOT acceptable")






# Close the source file
text_file.close()
