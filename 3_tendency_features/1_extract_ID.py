f1 = open("cullpdb_pc30_res2.0_R0.25_d180813_chains11177", "r")
f2 = open("ss.txt", "r")

o = open("sequence&secstr.txt", "w")

file1 = f1.readlines()
file2 = f2.readlines()

dic = {}
switch = ""
key = ""
for i in range(len(file2)):
    if "sequence" in file2[i]:
        dic[file2[i][1:7]] = {"sequence": ""}
        key = file2[i][1:7]
        switch = "sequence"

    elif "secstr" in file2[i]:
        dic[file2[i][1:7]]["secstr"] = ""
        switch = "secstr"
    else:
        dic[key][switch] += file2[i].replace("\n", "")




for i in range(1, len(file1)):
    key = file1[i][:4] + ":" + file1[i][4]
    if key in dic:
        print(key, file=o)
    try:
        print(dic[key]["sequence"], file=o)
        print(dic[key]["secstr"], file=o)
    except:
        pass


f1.close
f2.close
o.close
