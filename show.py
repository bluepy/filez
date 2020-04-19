import sys

# Goal:
# show the contents of a given file.

if __name__ == "__main__":
    # 1. read the file name from argument #1
    fileName = sys.argv[1]

    # 2. Open the file and assign to a variable f
    f = open(fileName, 'r')

    # 3. while true, read one line from the file f
    while True:
        line = f.readline()

        # 4. if that line is not empty print it
        if line:
            print(line, end='')
        else:  # 5. else stop
            break

    # 6. close the file
    f.close()
