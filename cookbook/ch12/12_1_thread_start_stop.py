import time

def countdown(n) :
    while n>0 :
        print('T-minus', n)
        n -= 1
        time.sleep(1)


from threading import Thread

t=Thread(target=countdown, args=(10,))
#t=Thread(target=countdown, args=(10,), daemon=True)
#daemon thread는 join할 수 없다. 하지만 메인 스레드가 종료될 때 자동으로
#사라진다.
t.start()
        

if t.is_alive() :
    print('Still running')
else :
    print('Completed')
    
