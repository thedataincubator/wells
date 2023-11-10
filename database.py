import sqlalchemy

conn_string = "postgresql://tdi:qKmd8s5ze7WAYV@adventureworks.tditrain.com:5431/wells"
engine = sqlalchemy.create_engine(conn_string)
conn = engine.connect()
result = conn.execute("""
    SELECT latitude, longitude, depth, gradient FROM wells LIMIT 10;
""")
rows = result.fetchall()
print(rows)
