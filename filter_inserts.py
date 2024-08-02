import re

pattern = r'INSERT INTO'
pattern1 = r'\);\s*$'
pattern3 = r'DELETE'
path= False

with open("inserts.sql", 'w+', encoding="utf8") as f:
    with open("clean.sql", encoding="utf8") as infile:
        for line in infile:
            if re.findall(pattern3, line):
                f.write(line)
                f.write("\n"*2)
            if re.findall(pattern, line):
                path = True
                
            if path == True:
                f.write(line)
                if re.findall(pattern1, line):
                    path=False
            else:
                # g.write(line)
                pass

            # if re.findall(pattern, line):
            #     # print("test")
            #     path = True
            #     print(path)
            