import sqlite3

DB_NAME = "db/mydb.sqlite3"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def check_task_exists(task_id: int) -> bool:
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute("SELECT 1 FROM status_table WHERE id = ? LIMIT 1", (task_id,))
  exists = cursor.fetchone() is not None
  conn.close()

  return exists

print(get_db_connection())