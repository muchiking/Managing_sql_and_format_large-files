import re
import os,sys
pattern = r'dbslamsfmpen.bankcodesinfo'
count=0
# f=open("dump2.sql",'w')
# f.write('--')
# f.close()

f=open("clean.sql",'w+')
g=open("other.sql",'w+')
path= False


with open("dbslamsfmpen.sql",encoding="utf8") as infile:
    for line in infile:
        # if path :
        #     f.write(line)
        # else:
        #     g.write(line)

        matches = re.finditer(pattern, line)
        print(matches)
        # if matches == True :
        #     print("test")
        #     path = False
        #     f.close()
            # sys.exit
        # f.close()
