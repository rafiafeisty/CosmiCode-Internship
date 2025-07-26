import asyncio
import random

async def fetch_data(task_id):
    print(f"[Task {task_id}] Fetching data...")
    await asyncio.sleep(random.uniform(1, 3)) 
    print(f"[Task {task_id}] Data fetched!")
    return f"Result of Task {task_id}"

async def main():
    print("Starting async I/O operations...\n")

    tasks = [
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
    ]
    results = await asyncio.gather(*tasks)

    print("\nAll async tasks completed.")
    for result in results:
        print(result)
asyncio.run(main())
