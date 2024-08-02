import re

pattern = r'dbslamsfmpen.bankcodesinfo'
count = 0
path = False

with open("clean.sql", 'w+', encoding="utf8") as f, open("other.sql", 'w+', encoding="utf8") as g:
    

    with open("dbslamsfmpen.sql", encoding="utf8") as infile:
        for line in infile:
            if path:
                f.write(line)
            else:
                g.write(line)

            if re.findall(pattern, line):
                print("test")
                path = True
                print(path)
