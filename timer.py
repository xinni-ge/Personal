from functools import wraps

import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_msg=os.strerror(errno.ETIME)):
    def decorator(func):
        def _timeout(signo, frame):
            raise TimeoutError(error_msg)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator
