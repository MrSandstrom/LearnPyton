import re


def tokenize(lines):
    lines_length = len(lines)
    return_array = []

    if lines_length == 0:
        return return_array

    if lines_length == 1:
        if len(lines[0]) == 0:
            return return_array

    if lines_length == 1:
        data = lines[0]
        # print ("Data='{}'".format(data))
        data = data.strip()
        # print ("Data='{}'".format(data))

        if len(data) == 0:
            return return_array

        # test4 & 5
        for line in lines:
            tokens = re.findall(r'\d+|\w+|\S', line.lower())
            return_array.extend(tokens)
        return return_array

    if lines_length == 1:
        tokens = tokenize(lines)


def countWords(words, stopWords):
    # test1
    if not words:
        return {}

    # test2,3,4
    word_count = {}

    for word in words:
        word = word.lower()

        if word in stopWords:
            continue

        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count


def printTopMost(frequencies, n):
    words = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    for word, freq in words[:n]:
        print(f"{word.ljust(20)}{str(freq).rjust(5)}")
