from stomp_ws import Stomp
import time

def do_thing_a(msg):
    print("MESSAGE: " + msg)

if __name__ == "__main__":
    stomp = Stomp("127.0.0.1:8080/game", sockjs=False, wss=False)
    stomp.connect()
    stomp.subscribe("/expire", do_thing_a)
