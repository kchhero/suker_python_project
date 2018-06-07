import threading

class SharedCounter:
    def __init__(self, initial_value=0) :
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1) :
        # 이전 버전의 파이썬의 경우 acquire, release를 사용했음.
        # self._value_lock.acquire()
        # self._value += delta
        # self._value_lock.release()
        with self._value_lock :
            self._value += delta
            print(self._value)

    def decr(self, delta=1) :
        # 이전 버전의 파이썬의 경우 acquire, release를 사용했음.        
        # self._value_lock.acquire()
        # self._value -= delta
        # self._value_lock.release()        
        with self._value_lock :
            self._value -= delta
            print(self._value)


t = SharedCounter(5)
t.decr()
t.incr()
