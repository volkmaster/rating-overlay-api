import asyncio
from typing import Any, Awaitable


def get_loop() -> asyncio.AbstractEventLoop:
    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    return asyncio.get_event_loop()


def wait(loop: asyncio.AbstractEventLoop, func: Awaitable[Any]) -> Any:
    return loop.run_until_complete(func)
