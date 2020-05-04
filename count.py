import sys
from words import makeWords


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("please provide <fileName> <word_to_search>")
        sys.exit(1)

    fileName = sys.argv[1]
    searchForWord = sys.argv[2]

    f = open(fileName, 'r')
    count = 0

    while True:
        line = f.readline()
        if line:
            wordList = makeWords(line)

            # Search for the word required
            for w in wordList:
                if w == searchForWord:
                    count = count + 1
        else:
            break

    f.close()

    print("{} found in file {} {} times".format(searchForWord, fileName, count))
