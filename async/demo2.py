import asyncio
import threading
async def task():
    print("定时任务执行")

async def main():
    event = asyncio.Event()
    loop = asyncio.get_running_loop()
    loop.call_later(10, event.set)  # 10秒后设置事件状态为已触发
    while not event.is_set():
        await asyncio.sleep(1)  # 每秒检查一次事件状态
        print("执行中...")
    print("主函数结束")

def run_main():
    asyncio.run(main())

# 创建一个线程执行定时任务
timer_thread = threading.Thread(target=run_main)

# 启动定时任务线程
timer_thread.start()

# 继续执行其他的代码
print("其他代码执行")

# 等待定时任务线程结束
timer_thread.join()

# 执行其他的代码
print("其他代码继续执行")
