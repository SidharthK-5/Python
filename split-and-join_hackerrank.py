def split_and_join(line):
    l = line.split(" ")
    l = "-".join(l)
    return l


if __name__ == "__main__":
    line = input()
    print(split_and_join(line))
