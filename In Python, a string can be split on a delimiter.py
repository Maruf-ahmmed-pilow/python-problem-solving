def split_and_join(line):
    b=line.split()
    c="-".join(b)
    return c
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)