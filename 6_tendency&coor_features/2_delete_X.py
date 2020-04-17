f = open("sequence&secstr.txt", "r")
o = open("seq&secstr_no_X.txt", "w")

aa = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L",
      "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y", " "]

file = f.readlines()
for i in range(len(file)):
    if i % 3 == 1:
        if ("X" not in file[i]) and ("U" not in file[i]) and ("O" not in file[i]) and ("B" not in file[i]):
            print(file[i - 1].replace("\n", ""), file=o)
            print(file[i].replace("\n", ""), file=o)
            print(file[i + 1].replace("\n", ""), file=o)

f.close
o.close
