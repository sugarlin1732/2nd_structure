f = open("modified.txt", "r")
o = open("structure_lable.txt", "w")

file = f.readlines()
for i in range(len(file)):
    if i % 3 == 2:
        for j in file[i].replace("\n", ""):
            print(j, file=o)


f.close
o.close
