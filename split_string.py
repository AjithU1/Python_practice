def split_and_join(line):
    # write your code here
    ls = line.split()
    js = "-".join(ls)
    return js


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
