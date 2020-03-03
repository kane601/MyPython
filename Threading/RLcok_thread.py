
import threading
import time

def Func(lock):
    global gl_num
    lock.acquire()
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    lock.release()

if __name__ == '__main__':
    gl_num = 0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=Func, args=(lock,))
        t.start()