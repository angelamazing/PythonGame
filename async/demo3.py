import asyncio

async def my_task():
    # 模拟一个耗时的异步操作
    await asyncio.sleep(2)
    return "任务完成"

async def main():
    try:
        result = await asyncio.wait_for(my_task(), timeout=3)
        print("任务结果:", result)
    except asyncio.TimeoutError:
        print("任务超时")

asyncio.run(main())