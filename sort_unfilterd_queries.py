import pymysql
import re
import sys

# Database connection
conn = pymysql.connect(host='localhost', user='root', password='root', db='dbslamsfmpen4')
cursor = conn.cursor()

# Input and output files
input_file = "failed_queries.sql"
failed_queries_file = "bad_tables.tmp"

# Pattern to detect the end of a SQL statement
pattern  = r'INSERT INTO'
deletepattern='DELETE'
database ='dbslamsfmpen4'
newdb='dbslamsfmpen'

# table = ''

switch=True

# Temporarily disable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
with open(input_file, 'r', encoding="utf8") as infile,open(failed_queries_file, 'w+', encoding="utf8") as g:
    for line in infile:
        if re.search(pattern , line):
            mid=(line.split(" "))
            # print(mid[2])
            table=(str(mid[2]).replace('`', ''))
            query=f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{database}' AND TABLE_NAME = '{table}';"""
            # print(query)
            cursor.execute(query)
            conn.commit()
            columns = cursor.fetchall()
            query1=''
            count=0
            for column in columns:
                if count==0:
                    query1 = f'`{column[0]}`'
                    count =7
                else:
                    query1=query1 +  f',`{column[0]}`'
                # print(column[0])
            # print(query1)
            copy_query = f'''INSERT INTO {table} \n ({query1})  \n SELECT {query1} \n FROM {newdb}.{table}'''
            try:
                print(copy_query)
                cursor.execute(f"""{copy_query}""")
                conn.commit() 
                
            except Exception as e:
                g.write(copy_query)
           
        #     switch=False
        # if switch==False:
        #     sys.exit()
            
        # g.write(line)
        
        # print(line.split(" "))
        # sys.exit()
        # if re.search(pattern , line):
        #     try:
        #         mid=(line.split(" "))
        #         # g.write(line)
        #         print
        #         # print(line.split(" "))
        #         sys.exit()

        #     except:
        #         pass
                

# cursor.execute("SQL_SAFE_UPDATES = 0;")

# SET SQL_SAFE_UPDATES = 0;

# List to store failed queries
# failed_queries = []