import asyncio

async def start_strongman(name, power):
    print (f'Силач {name} начал соревнования.')
    for baulder_num in range(1,6):
        await asyncio.sleep(6 - power)
        print (f'Силач {name} поднял {baulder_num}.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Andrey', 5))
    task2 = asyncio.create_task(start_strongman('Lesha', 4))
    task3 = asyncio.create_task(start_strongman('Vasya', 2))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())