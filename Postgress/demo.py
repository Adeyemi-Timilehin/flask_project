import psycopg2

conn = psycopg2.connect(user="postgres",
                                  password="tolu1992",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="timik")

cursor = conn.cursor()


# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS timik;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE table2 (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")
cursor.execute("""
INSERT INTO table2(id,description) VALUES(2,'Livingproof');
""")

# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()