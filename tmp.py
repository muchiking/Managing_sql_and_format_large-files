
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

# Temporarily disable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
cursor.execute("DELETE FROM `bankingdashboard`;")
cursor.execute("INSERT INTO `bankingdashboard` (`id`) VALUES(1);")
