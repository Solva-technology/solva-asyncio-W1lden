import asyncio


async def safe_divide(a, b):
    await asyncio.sleep(0.1)
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"


async def run_divisions():
    tasks = [
        safe_divide(25, 5),
        safe_divide(1, 0),
        safe_divide(18, 9)
    ]
    return await asyncio.gather(*tasks)
