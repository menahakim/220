def read_data(file_name):
    infile = open(file_name, "r")
    read_file = infile.read()
    replacing = read_file.replace("\n", " ")
    file_split = replacing.split(" ")
    i = 0
    while i < len(file_split):
        file_split[i] = int(file_split[i])
        i = i + 1
    return file_split


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if list[i] == search_val:
            return True
        i = i + 1
    return False





