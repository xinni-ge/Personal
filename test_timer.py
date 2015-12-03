import time

from timer import timeout


@timeout(1)
def long_sleep():
    time.sleep(5)

if __name__ == "__main__":
    tbegin = time.time()
    try:
        long_sleep()
    except Exception as e:
        print str(e)
    tend = time.time()
    print tend-tbegin
