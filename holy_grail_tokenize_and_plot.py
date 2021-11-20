import matplotlib.pyplot as plt
from nltk import regexp_tokenize
import re

holy_grail = "SCENE 1: [wind] [clop clop clop] KING ARTHUR: Whoa there!  [clop clop clop] SOLDIER #1: Halt!  Who goes there? ARTHUR: It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign of all England! SOLDIER #1: Pull the other one! ARTHUR: I am, ...  and this is my trusty servant Patsy.  We have ridden the length and breadth of the land in search of knights who will join me in my court at Camelot.  I must speak with your lord and master. SOLDIER #1: What?  Ridden on a horse? ARTHUR: Yes! # Split the script into lines: lines"

# Split the script into lines: lines
lines = holy_grail.split("\n")

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, "", l) for l in lines]
print(lines)

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s, r"\w+") for s in lines]


# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# # Plot a histogram of the line lengths
bins_list = [10, 20, 40, 50, 60, 80]

plt.hist(line_num_words)
plt.xlabel("Line no. of words")
plt.ylabel("Frequency")
plt.title("Holygrail tokenization histogram")
plt.xlim(0, 100)

# Show the plot
plt.show()