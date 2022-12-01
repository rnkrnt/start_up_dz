import socket
import asyncio

async def add(x, y):
    return x + y
    await asyncio.sleep(0)

async def sub(x, y):
    return x - y
    await asyncio.sleep(0)

async def mult(x, y):
    return x * y
    await asyncio.sleep(0)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 60000))
    sock.listen(10)
    print('Server is running, please, press ctrl+c to stop')
    while True:
        conn, addr = sock.accept()
        print('connected:', addr)
        data = conn.recv(1024).decode('utf-8')

        lis_input = data.split()
        lis = []
        for i in lis_input:
            lis.append(int(i))

        ioloop = asyncio.get_event_loop()
        tasks = [ioloop.create_task(add(lis[0], lis[1])), ioloop.create_task(sub(lis[0], lis[1])), ioloop.create_task(mult(lis[0], lis[1]))]
        wait_tasks = asyncio.wait(tasks)
        ioloop.run_until_complete(wait_tasks)
        ioloop.close()

        answer = f"{str(tasks[0].result())}, {str(tasks[1].result())}, {str(tasks[2].result())}"

        conn.send(bytes(answer, encoding="utf-8"))

except KeyboardInterrupt as ex:
    print(f"Error: {ex}")
conn.close()
