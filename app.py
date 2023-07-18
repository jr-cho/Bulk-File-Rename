import os
from path import path


def main():
    i = 1
    p = path
    for filename in os.listdir(p):
        dest = "Text File " + str(i) + ".txt"
        source = path + filename
        dest = path + dest
        os.rename(source, dest)
        i += 1


if __name__ == "__main__":
    main()
