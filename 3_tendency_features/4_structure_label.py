f = open("E:\\Research\\2nd_structure\\3_tendency_features\\modified.txt", "r")
o = open("E:\\Research\\2nd_structure\\3_tendency_features\\structure_label.txt", "w")

file = f.readlines()
for i in range(len(file)):
    if i % 3 == 2:
        for j in file[i].replace("\n", ""):
            print(j, file=o)


f.close
o.close
