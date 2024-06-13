# import timeit
# start = timeit.default_timer()
# with open("db.sql" ,buffering=100000) as infile:


# with open("db.sql" ) as infile:
#     for line in infile:
#         print(line)

# end = timeit.default_timer()
# print("Elapsed time:", end - start, "seconds")
# Elapsed time: 0.1224870000150986 seconds


import re
counter=0
counter2=0
code=''
pastcode=''
fin=0
test=0
cypher='utf8mb4'

f=open('test3','w')
# f.write(pastcode)
f.write('--')
f.close()

    # FK_transtypeinfo_doctypeinfo


# Your pattern
pattern = r'FK_TravelPolicyPremiumHistory_PolicyNumber'

# Dump20240429.sql

# with open("Dump20240429.sql",encoding="latin") as infile:
with open("Dump20240429.sql",encoding=cypher) as infile:
    for line in infile:
        if counter2 <= 100 :
            code += line
            counter2+=1
        else :
            counter2 = 0
            pastcode=''
            pastcode=code
            code= ''

        if counter==1:
          
            test+=1
           
            if test== 99:

                f=open('test3','+ab')
                # f.write(pastcode)
                f.write(code.encode(cypher))
                f.close()
                counter =0
                
            
        
        


        matches = re.finditer(pattern, line)
        
        for match in matches:
            # print(f"Found at position {match.start()}: {match.group()}")
            f=open('test3','ab')
            f.write(pastcode.encode('utf8'))
            f.write(code.encode('utf8'))
            f.close()
            counter=1

        # if fin == 1:
