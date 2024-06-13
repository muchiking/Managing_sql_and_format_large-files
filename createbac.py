import re
pattern = r'travelpolicypremiumhistory '
count=0
f=open("dump2.sql",'w')
f.write('--')
f.close()

f=open("dump2.sql",'a+')


with open("Dump20240429.sql",encoding="latin1") as infile:
    for line in infile:
        matches = re.finditer(pattern, line)
        for match in matches:
            count=1
        if count >=1 and count <= 4 :
            print(line)
            count+=1
        if count>=4:
                f.write(line)
            
           
f.close()



