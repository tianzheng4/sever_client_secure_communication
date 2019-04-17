import signal
from threading import Timer
TIMEOUT = 5 # number of seconds your want for timeout

def interrupted(signum, frame):
    "called when read times out"
    print 'interrupted!'
signal.signal(signal.SIGALRM, interrupted)

def input():
    try:
            print 'You have 5 seconds to type in your stuff...'
            foo = raw_input()
            return foo
    except:
            # timeout
            return

# set alarmr
while True:
    timeout = 10
    t = Timer(timeout, print, ['Sorry, times up'])
    t.start()
    prompt = "You have %d seconds to choose the correct answer...\n" % timeout
    answer = input(prompt)
    t.cancel()
    
    print 'Next Round'
