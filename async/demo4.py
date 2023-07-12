import asyncio

async def task1():
    print("任务1开始执行")
    await asyncio.sleep(2)
    print("任务1执行完成")

async def task2():
    print("任务2开始执行")
    await asyncio.sleep(2)
    print("任务2执行完成")

async def main():
    # 创建一个事件对象
    event = asyncio.Event()

    # 创建并发任务列表
    tasks = [task1(), task2()]

    # 启动任务并等待事件触发
    for task in tasks:
        asyncio.create_task(run_task_with_event(task, event))

    # 触发事件，只执行其中一个任务
    await asyncio.sleep(2)
    event.set()

async def run_task_with_event(task, event):
    await event.wait()
    await task

asyncio.run(main())