import sys
from wordfreq import tokenize, countWords, printTopMost

# Read stop word file and separate into a string array
inp_file = open(sys.argv[1], encoding="utf-8")
stop_word_array = []
for line in inp_file:
    line = line.strip()
    stop_word_array.append(line)
inp_file.close()
print("total number of stop_words: {}".format(len(stop_word_array)))


# Read article file and separate into a big string
inp_file = open(sys.argv[2], encoding="utf-8")
complete_article_string = ""
for line in inp_file:
    line_array = [line]
    complete_article_string += line
inp_file.close()

# Move our String to an array with length 1
article_array = [complete_article_string]

# Now our tokenize method can accept and pare the input
article_tokens = tokenize(article_array)

# Now our dictionary method can handle the input
article_dictionary = countWords(article_tokens, stop_word_array)

# read the wanted printing rows and convert from string to int
print_length = int(sys.argv[3])

# finally
printTopMost(article_dictionary, print_length)
