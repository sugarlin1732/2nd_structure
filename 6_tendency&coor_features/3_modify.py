f = open("E:\\Research\\2nd_structure\\3_tendency_features\\seq&secstr_no_X.txt", "r")
o = open("modified.txt", "w")

file = f.readlines()

for i in range(len(file)):
    if i % 3 == 0:
        print(file[i].replace("\n", ""), file=o)
    elif i % 3 == 1:
        new_seq = " " * 6 + file[i].replace("\n", "") + " " * 6
        new_line = ""
        for j in range(6, len(new_seq) - 6):
            new_line += new_seq[j - 6:j + 7] + ","
        print(new_line.rstrip(","), file=o)
    else:
        new_str = ""
        for j in file[i].replace("\n", ""):
            if j in ["E"]:
                new_str += j
            elif j in ["H", "G", "I"]:
                new_str += "H"
            else:
                new_str += "C"
        print(new_str, file=o)


f.close
o.close
