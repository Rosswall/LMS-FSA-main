import psycopg2
try:
    conn = psycopg2.connect(
        dbname='lmsdb',
        user='lmsuser',
        password='password',
        host="42.118.115.246",
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
