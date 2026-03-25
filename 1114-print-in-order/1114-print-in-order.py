import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        printFirst()
        self.first_done.set()   # signal that first() is done

    def second(self, printSecond):
        self.first_done.wait()  # wait for first()
        printSecond()
        self.second_done.set()  # signal that second() is done

    def third(self, printThird):
        self.second_done.wait()  # wait for second()
        printThird()