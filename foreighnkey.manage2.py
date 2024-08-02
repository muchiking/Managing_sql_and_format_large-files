import pymysql
import re

# Database connection
conn = pymysql.connect(host='localhost', user='root', password='root', db='dbslamsfmpen4')
cursor = conn.cursor()

# Input and output files
input_file = "inserts.sql"
failed_queries_file = "failed_queries.sql"
openfiles='clean.sql'

# Pattern to detect the end of a SQL statement
end_of_statement_pattern = r';\s*$'
deletepattern = 'DELETE'

# Temporarily disable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

# List to store failed queries
with open(input_file, 'r', encoding="utf8") as infile, open(failed_queries_file, 'w+', encoding="utf8") as g, open(openfiles, 'w+', encoding="utf8") as f:
    sql_statement = ''
    for line in infile:
        sql_statement += line
        if re.search(end_of_statement_pattern, line):
            try:
                cursor.execute(sql_statement)
                conn.commit()
                f.write(sql_statement)
                sql_statement = ''

            except pymysql.MySQLError as e:
                g.write(sql_statement + '\n')
                # g.write(f"Error: {str(e)}\n")
                sql_statement = ''  # Clear the statement after writing to failed file

        # elif re.search(deletepattern, line):
        #     try:
        #         cursor.execute(sql_statement)
        #         conn.commit()
        #         sql_statement = ''
        #     except pymysql.MySQLError as e:
        #         g.write(sql_statement + '\n')
        #         g.write(f"Error: {str(e)}\n")
        #         sql_statement = ''  # Clear the statement after writing to failed file

# Re-enable foreign key checks
# cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

# Close the connection
cursor.close()
conn.close()

print("Failed queries due to foreign key issues have been logged in:", failed_queries_file)
