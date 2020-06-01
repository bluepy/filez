import sys
from words import makeWords

# Goal:
# show the contents of a given file.


def printLine(line, lowercase=False, uppercase=False):
    if lowercase:
        line = line.lower()
    elif uppercase:
        line = line.upper()
    print(line, end='')


def printWords(line, lowercase=False, uppercase=False):
    if lowercase:
        line = line.lower()
    elif uppercase:
        line = line.upper()
    words = makeWords(line)
    for word in words:
        print(word)


if __name__ == "__main__":
    fileName = ''
    words = False
    lowerCase = False
    upperCase = False
    # 1. read the file name from argument #1
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
    elif len(sys.argv) == 3:
        # 2. read if words to be printed from argument #2 (optional)
        fileName = sys.argv[1]
        words = True if sys.argv[2] == "True" else False
    elif len(sys.argv) == 4:
        # 3. read if lower case to be printed from argument #3 (optional)
        fileName = sys.argv[1]
        words = True if sys.argv[2] == "True" else False
        lowerCase = True if sys.argv[3] == "True" else False
    elif len(sys.argv) == 5:
        # 3. read if lower case to be printed from argument #3 (optional)
        fileName = sys.argv[1]
        words = True if sys.argv[2] == "True" else False
        lowerCase = True if sys.argv[3] == "True" else False
        upperCase = True if sys.argv[4] == "True" else False
    else:
        # error print how to run the program and exit with error 1
        print("Error: unsupported number of arguments")
        print("Usage: show.py <filename> [<words>] [<lowercase>]")
        sys.exit(1)

    # 2. Open the file and assign to a variable f
    f = open(fileName, 'r')
    # 3. while true, read one line from the file f
    while True:
        line = f.readline()

        # 4. if that line is not empty print it
        if line:
            if words:
                printWords(line, lowerCase, upperCase)
            else:
                printLine(line, lowerCase, upperCase)
        else:  # 5. else stop
            break

    # 6. close the file
    f.close()
