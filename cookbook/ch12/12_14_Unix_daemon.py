#!/usr/bin/env python3
#  daemon.py

import os
import sys
import atexit
import signal

def daemonize(pidfile, *, stdin='/dev/null',
                          stdout='/dev/null',
                          stderr='/dev/null'):
    if os.path.exists(pidfile) :
        raise RuntimeError('Already running')

    #first fork
    try :
        if os.fork() > 0 :
            raise SystemExit(0)  #parent exit
    except OSError as e :
        raise RuntimeError('fork #1 failed')

    os.chdir('/')
    os.umask(0)
    os.setsid()

    #second fork
    try :
        if os.fork() > 0 :
            raise SystemExit(0)
    except OSError as e :
        raise RuntimeError('fork #2 failed')

    # input,output buffer flush
    sys.stdout.flush()
    sys.stderr.flush()

    # stdin, stdout, stderr file descriptor replace
    with open(stdin, 'rb', 0) as f :
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f :
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f :
        os.dup2(f.fileno(), sys.stderr.fileno())

    #PID file write
    with open(pidfile, 'w') as f:
        print(os.getpid(), file=f)

    # when exit, PID file remove
    atexit.register(lambda: os.remove(pidfile))

    # handler about exit
    def sigterm_handler(signo, frame) :
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)

def main() :
    import time
    sys.stdout.write('Daemon started with pid {}\n'.format(time.ctime()))
    time.sleep(10)

if __name__ == '__main__' :
    PIDFILE = '/tmp/daemon.pid'

    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)

    if sys.argv[1] == 'start' :
        try :
            daemonize(PIDFILE,
                      stdout='/tmp/daemon.log',
                      stderr='/tmp/daemon.log')
        except RuntimeError as e :
            print(e, file=sys.stderr)
            raise SystemExit(1)

        main()

    elif sys.argv[1] == 'stop' :
        if os.path.exists(PIDFILE) :
            with open(PIDFILE) as f :
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print('Not running', file=sys.stderr)
            raise SystemExit(1)

    else :
        print('Unknown command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)
    
