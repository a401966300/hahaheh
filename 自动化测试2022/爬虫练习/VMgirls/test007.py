import threading


def one():
    for i in range(1, 10, 2):
        print(i)
    try:
        print(2/0)
    except Exception as e:
        print(e)


def two():
    for i in range(2, 11, 2):
        print(i)


if __name__ == '__main__':
    t1 = threading.Thread(target=one,)
    t2 = threading.Thread(target=two,)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
