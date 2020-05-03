
def makeWords(line):
    lwords = line.split()
    words = list()
    for word in lwords:
        word = stripNonAlphaLetters(word)
        words.append(word)
    return words


def stripNonAlphaLetters(word):
    startIndex = 0

    # Find the start of the word
    for letter in word:
        if isAlphaNum(letter):
            break
        startIndex += 1

    # strip the non-alphanum letters from this word
    # for example (abcd) --> abcd)
    word = word[startIndex:]

    endIndex = startIndex
    for letter in word:
        if not isAlphaNum(letter):
            break
        endIndex += 1

    # abcd) -> abcd
    return word[startIndex:endIndex]


def isAlphaNum(letter):
    return ((letter >= 'a' and letter <= 'z') or
            (letter >= 'A' and letter <= 'Z') or
            (letter >= '0' and letter <= '9'))
