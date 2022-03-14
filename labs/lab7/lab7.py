def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    read_in_file = infile.readlines()
    outfile = open(out_file_name, "w")
    class_average = 0
    valid = 0
    for line in read_in_file:
        acc = 0
        split_line = line.split(": ")
        grades = split_line[1].split(" ")
        grade_total = 0
        for i in range(0, len(grades), 2):
            grade_total += (int(grades[i]) * int(grades[i + 1]))
            acc = acc + int(grades[i])
        if acc == 100:
            weighted_avg = grade_total / 100
            class_average += weighted_avg
            valid += 1
            print(split_line[0], weighted_avg, file = outfile)
        elif acc < 100:
            print("Error: The weights are less than 100", file = outfile)
        else:
            print("Error: The weights are more than 100", file = outfile)
    print("Class average: ", class_average / valid, file = outfile)



if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")

