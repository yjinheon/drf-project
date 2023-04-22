import asyncio

async def my_coroutine():
    print('Coroutine started')
    await asyncio.sleep(1)  # Pause for one second
    print('Coroutine resumed')
    await asyncio.sleep(2)  # Pause for two seconds
    print('Coroutine finished')

async def main():
    print('Main started')
    await my_coroutine()
    print('Main finished')

asyncio.run(main())
