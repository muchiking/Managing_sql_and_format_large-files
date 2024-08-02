from sqlalchemy import create_engine

# Database connection
DATABASE_URI = 'mysql+pymysql://root:root@localhost/dbslamsfmpen3'

# Create an SQLAlchemy engine
conn = engine.connect() 

# Example: Connecting and running a simple query
result = conn.execute("show databases")