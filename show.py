import sys

# Goal:
# show the contents of a given file.


def printLine(line):
    print(line, end='')


def printWords(line):
    words = line.split()
    for word in words:
        word = makeWord(word)
        if word:
            print(word)


def makeWord(word):
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


if __name__ == "__main__":
    # 1. read the file name from argument #1
    fileName = sys.argv[1]
    if len(sys.argv) < 3:
        words = False
    else:
        words = bool(sys.argv[2])

    # 2. Open the file and assign to a variable f
    f = open(fileName, 'r')

    # 3. while true, read one line from the file f
    while True:
        line = f.readline()

        # 4. if that line is not empty print it
        if line:
            if words:
                printWords(line)
            else:
                printLine(line)
        else:  # 5. else stop
            break

    # 6. close the file
    f.close()
