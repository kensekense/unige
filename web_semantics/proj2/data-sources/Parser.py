
ttl_file = open(r"C:\Users\kevin\Desktop\Web Semantics\Project-2\data-sources\wpCSP.ttl", "r")
write_file = open(r"C:\Users\kevin\Desktop\Web Semantics\Project-2\data-sources\wpCSPedited.ttl", "w")
lines = []

for line in ttl_file:
    lines.append(line)
    
for item in lines:
    word = item.split()
        if word == ":projectName":
            write_file.write(":name")
        elif word == ":discipline":
            write_file.write(":domain")
        elif word == ":area":
            write_file.write(":geography")
        elif word == ":began":
            write_file.write(":startYear")
        else:
            write_file.write(word)
