import sys
from words import makeWords


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("please provide <fileName> <word_to_search>")
        sys.exit(1)

    fileName = sys.argv[1]
    searchForWord = sys.argv[2]

    f = open(fileName, 'r')
    foundWord = False

    while True:
        line = f.readline()
        if line:
            wordList = makeWords(line)

            # Search for the word required
            for w in wordList:
                if w == searchForWord:
                    foundWord = True
                    break

            if foundWord:
                break
        else:
            break

    f.close()

    if foundWord:
        print("{} found in file {}".format(searchForWord, fileName))
    else:
        print("{} not found in file {}".format(searchForWord, fileName))
