import asyncio

async def async_task(name, duration):
    print(f"Starting {name}...")
    await asyncio.sleep(duration)
    print(f"{name} completed after {duration} seconds")

async def main():
    await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 3),
        async_task("Task 3", 1),
    )

if __name__ == "__main__":
    asyncio.run(main())