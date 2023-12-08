import sys
import sqlalchemy

mindepth = sys.argv[1]
mingradient = sys.argv[2]

conn_string = "postgresql://tdi:qKmd8s5ze7WAYV@adventureworks.tditrain.com:5431/wells"
engine = sqlalchemy.create_engine(conn_string)
conn = engine.connect()
query = sqlalchemy.text("""
    SELECT latitude, longitude, depth, gradient FROM wells 
    WHERE depth > :mindepth AND gradient > :mingradient;
""")
result = conn.execute(query, {'mindepth': mindepth, 'mingradient': mingradient})
rows = result.fetchall()
print(rows)
