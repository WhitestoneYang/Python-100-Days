import threading
import time
import random

# 共享资源
items = []
# 创建 Condition 对象
# 使用 Condition 对象的 with 语句确保在进入和离开临界区时自动获取和释放锁，这有助于避免死锁。
# 同时，这个例子中的 Consumer 线程会无限循环，你可能需要在实际应用中根据具体需求调整其行为。
condition = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        global items
        # for i in range(10):
        while True:
            time.sleep(random.random())
            with condition:
                item = random.randint(1, 100)
                items.append(item)
                print(f'Producer produced item {item};\t items left: {items}')
                # 通知消费者有新物品可以消费
                # 当一个线程调用 condition.notify() 时，它会唤醒正在等待该 Condition 对象的另一个线程。
                # 这种机制常用于在多个线程之间同步某些状态的改变。
                # 当一个线程调用 condition.notify() 时，它会标记一个等待中的线程（如果有的话）为可被唤醒。然而，这个被唤醒的线程并不会立即执行。它必须等待当前持有锁的线程（在这个案例中是生产者）释放锁之后，才能尝试获取锁并继续执行.
                # 如果生产者线程在释放锁后很快又重新进入了一个 with condition: 块（例如因为它处于一个循环中），并且在这个时刻，操作系统选择了它来执行.
                condition.notify()
                time.sleep(random.random())

class Consumer(threading.Thread):
    def run(self):
        global items
        while True:
            with condition:
                if not items:
                    # 如果没有物品可以消费，等待
                    print('Consumer waiting for items...')
                    # 释放锁;等待通知;重新获取锁
                    # 在使用 condition.wait() 时，通常需要将其包裹在 with 语句中，以确保锁的正确获取和释放：
                    condition.wait()
                # 消费物品
                item = items.pop(0)
                print(f'Consumer consumed item {item};\t items left: {items}')
            time.sleep(random.random())

# 创建并启动生产者和消费者线程
producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()

producer.join()
consumer.join()
