import asyncio


async def delayed_echo(text, delay):
    await asyncio.sleep(delay)
    print(text)
    return text


async def echo_all():
    return await asyncio.gather(
        delayed_echo("hello", 1),
        delayed_echo("world", 2),
        delayed_echo("!", 3),
    )
