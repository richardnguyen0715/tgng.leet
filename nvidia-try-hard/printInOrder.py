import threading

class Foo:
    def __init__(self):
        self.sem1 = threading.Semaphore(0)  # Block second()
        self.sem2 = threading.Semaphore(0)  # Block third()

    def first(self, printFirst):
        printFirst()
        self.sem1.release()  # Cho phép second() chạy

    def second(self, printSecond):
        self.sem1.acquire()  # Chờ first() hoàn thành
        printSecond()
        self.sem2.release()  # Cho phép third() chạy

    def third(self, printThird):
        self.sem2.acquire()  # Chờ second() hoàn thành
        printThird()
        

class Foo:
    def __init__(self):
        self.step = 0

    def first(self, printFirst):
        printFirst()
        self.step = 1

    def second(self, printSecond):
        while self.step < 1:
            pass
        
        printSecond()
        self.step = 2

    def third(self, printThird):
        while self.step < 2:
            pass
        
        printThird()
    
        
class Foo:
    def __init__(self):
        self.first_done = False
        self.second_done = False

    def first(self, printFirst):
        printFirst()
        self.first_done = True

    def second(self, printSecond):
        while not self.first_done:
            pass
        
        printSecond()
        self.second_done = True

    def third(self, printThird):
        while not self.second_done:
            pass
        
        printThird()
        
    
    
class Foo:
    def __init__(self):
        self.completed = set()

    def first(self, printFirst):
        printFirst()
        self.completed.add('first')

    def second(self, printSecond):
        while 'first' not in self.completed:
            pass  # Chờ first() hoàn thành
        
        printSecond()
        self.completed.add('second')

    def third(self, printThird):
        while 'second' not in self.completed:
            pass  # Chờ second() hoàn thành
        
        printThird()
        

from threading import Event

class Foo:
    def __init__(self):
        self._first_done = Event()
        self._second_done = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._first_done.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self._first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self._second_done.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self._second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()