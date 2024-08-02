import pymysql
import re

# Database connection
conn = pymysql.connect(host='localhost', user='root', password='root', db='dbslamsfmpen3')
cursor = conn.cursor()

# Input and output files
input_file = "inserts.sql"
failed_queries_file = "failed_queries.sql"

# Pattern to detect the end of a SQL statement
end_of_statement_pattern = r'\);\s*$'
deletepattern='DELETE'


# Temporarily disable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
# cursor.execute("SQL_SAFE_UPDATES = 0;")

# SET SQL_SAFE_UPDATES = 0;

# List to store failed queries
# failed_queries = []

with open(input_file, 'r', encoding="utf8") as infile,open(failed_queries_file, 'w+', encoding="utf8") as g:
    sql_statement = ''
    for line in infile:
        sql_statement += line
        if re.search(end_of_statement_pattern, line):
            try:
                sql_statement= re.sub(r"[\n\t]*", "", sql_statement)
                cursor.execute(f"""{sql_statement}""")
                conn.commit()
                sql_statement = ''
                # print(sql_statement)
            except pymysql.MySQLError as e:
                if "foreign key constraint fails" in str(e):
                    g.write(sql_statement)
                    # g.write('\n'*2)
                else:
                    g.write(sql_statement)
                    # g.write('\n'*2)
                    # print(sql_statement)
                    # raise  # Raise other errors

        if re.search(deletepattern, line):
            try:
                sql_statement= re.sub(r"[\n\t]*", "", sql_statement)
                cursor.execute(f"""{sql_statement}""")
                conn.commit()
                # print(sql_statement)
                sql_statement = ''
               
            except pymysql.MySQLError as e:
                g.write(sql_statement)
                # g.write('\n'*2)
                # if "foreign key constraint fails" in str(e):
                    
                
               
        
            

# Re-enable foreign key checks
# cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

# Close the connection
cursor.close()
conn.close()

# Write failed queries to a file
# with open(failed_queries_file, 'w', encoding="utf8") as f:
#     for query in failed_queries:
#         f.write(query)
#         f.write('\n')

print("Failed queries due to foreign key issues have been logged in:", failed_queries_file)
