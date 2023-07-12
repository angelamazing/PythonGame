"""
异步网络请求
"""

import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        'https://www.163.com',
        'https://www.zhibo8.cc',
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)

        # 并发执行所有任务
        responses = await asyncio.gather(*tasks)

        # 处理响应结果
        for url, response in zip(urls, responses):
            print(f"URL: {url}")
            print(f"Response: {response[:100]}...\n")


# 运行异步函数
asyncio.run(main())


