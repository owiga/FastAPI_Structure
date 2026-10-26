import asyncio
import random
from os.path import curdir

from fastapi import FastAPI, BackgroundTasks
from db.db import get_db_connection, check_task_exists
from schemas import Url

app = FastAPI()

async def parse_url(task_id: str, url: Url):
    print(f"{task_id}: {url} - Принята")
    conn = get_db_connection()
    cursor = conn.cursor()
    if not check_task_exists(int(task_id)):
        cursor.execute("INSERT INTO status_table (status, id) VALUES (?, ?)", ("none", task_id))
    cursor.execute(
        "UPDATE status_table SET status = ? WHERE id = ?", ("processing", task_id)
    )
    conn.commit()

    await asyncio.sleep(random.randint(12, 15))

    cursor.execute("UPDATE status_table SET status = ? WHERE id = ?", ("done", task_id))
    conn.commit()

    conn.close()

    print(f"{task_id} - Завершился")

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM status_table WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()

    return {
        "status": row['status'] if row else "None",
        "task_id": row["id"] if row else task_id,
    }

@app.post("/create_task/{task_id}")
async def create_task(url: Url, background_tasks: BackgroundTasks, task_id: str):
    task_id = task_id
    background_tasks.add_task(parse_url, task_id, url)

    print("Парсим ccылку...")

    return {
        "status": "success",
        "task_id": task_id,
        "message": "Ваша ссылка принята!"
    }



