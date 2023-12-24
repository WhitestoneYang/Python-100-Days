"""
异步I/O - async / await
"""
import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


async def main():
    """主函数"""
    loop = asyncio.get_event_loop()
    # asyncio.gather 接收一系列的协程或者异步任务（asyncio.Task 对象），然后并发地运行它们。当所有协程都完成时，gather 返回一个包含每个协程返回值的列表。
    # 如果 asyncio.gather 中的任一任务抛出异常，gather 会立即抛出这个异常。你可以通过设置 return_exceptions 参数为 True 来改变这个行为，这样的话，异常会作为结果列表中的元素返回，而不是被直接抛出。
    result1, result2 = await asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    print(result1)
    print(result2)
    # add_done_callback 是 Python asyncio 库中 Future 对象的一个方法。它允许你附加一个回调函数，这个回调函数将在 Future 对象完成时被调用。Future 对象代表了一个可能还没有完成的异步操作，当这个操作完成时，Future 将被设置为完成状态，并且可以获取到其结果。
    # future.add_done_callback(lambda x: print(x.result()))
    # loop.run_until_complete(future)
    # loop.close()


if __name__ == '__main__':
    # main()
    asyncio.run(main())
