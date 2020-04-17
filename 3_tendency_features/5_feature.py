f = open("E:\\Research\\2nd_structure\\3_tendency_features\\modified.txt", "r")
o = open("E:\\Research\\2nd_structure\\3_tendency_features\\feature.txt", "w")

file = f.readlines()

dic = {
    "A": "1.46 0.69 0.84",
    "C": "0.66 1.41 1.03",
    "D": "0.96 0.50 1.28",
    "E": "1.46 0.62 0.88",
    "F": "1.08 1.43 0.73",
    "G": "0.48 0.68 1.52",
    "H": "0.91 1.12 1.01",
    "I": "1.02 1.69 0.65",
    "K": "1.12 0.85 1.00",
    "L": "1.34 1.19 0.68",
    "M": "1.12 1.16 0.68",
    "N": "0.80 0.65 1.33",
    "P": "0.53 0.44 1.62",
    "Q": "1.25 0.76 0.95",
    "R": "1.25 0.80 0.94",
    "S": "0.76 0.90 1.23",
    "T": "0.69 1.26 1.09",
    "V": "0.91 1.85 0.64",
    "W": "1.15 1.48 0.66",
    "Y": "0.95 1.46 0.81",
    " ": "0 0 0"
}


for i in range(len(file)):
    if i % 3 == 1:
        s = file[i].replace("\n", "").split(",")
        for j in s:
            feature_line = ""
            for k in j:
                feature_line += dic[k] + " "
            print(feature_line.rstrip(" "), file=o)

f.close
o.close
