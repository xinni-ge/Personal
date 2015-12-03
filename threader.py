import Queue
import threading
import time

from timer import timeout


class Threads(object):
    def __init__(self,currency=1):
        self.currency = currency
        self.threads = None
        self.queue = None

    def get_sleep(self, sid, seconds=5):
        tbegin = time.time()
        if sid == 3:
            seconds = 10 
        time.sleep(seconds)
        self.queue.put((sid,time.time()-tbegin))
        return "sleep %d"%sid

    def multithreads(self):
        self.queue = Queue.Queue()
        self.threads = []
        for i in range(self.currency):
            t = threading.Thread(name="%d"%i, target=self.get_sleep, args=(i,))
            self.threads.append(t)
            t.start()

        for t in self.threads:
            print "Thread", t
            t.join(5)
            print t, t.isAlive()

        while True:
            if self.queue.empty():
                break
            else:
                print self.queue.get()



if __name__ == "__main__":
    th = Threads(5)
    th.multithreads()
