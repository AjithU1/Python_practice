f = open("log.txt")
c = f.readlines()
d = {"INFO": 0, "ERROR": 0, "WARNING": 0, "MSG": 0}
count_i = 0
count_e = 0
count_w = 0
count_m = 0

for i in c:
    if "INFO" in i:
        count_i += 1
    elif "ERROR" in i:
        count_e += 1
    elif "WARNING" in i:
        count_w += 1
    else:
        count_m += 1

    d["INFO"] = count_i
    d["ERROR"] = count_e
    d["WARNING"] = count_w
    d["MSG"] = count_m

print(d)
