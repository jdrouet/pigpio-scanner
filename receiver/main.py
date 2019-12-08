import os
import pigpio
import time
import vw

PIGPIO_HOST = os.getenv("PIGPIO_HOST", "localhost")
PIGPIO_PORT = int(os.getenv("PIGPIO_PORT", "8888"))
PIGPIO_PIN = int(os.getenv("PIGPIO_PIN", "27"))
BAUD_RATE_MIN = int(os.getenv("BAUD_RATE_MIN", "100"))
BAUD_RATE_MAX = int(os.getenv("BAUD_RATE_MIN", "5000"))

def detect(pi, baud_rate):
  rx = vw.rx(pi, PIGPIO_PIN, baud_rate)
  found = False
  start = time.time()
  while time.time() - start < 30:
    while rx.ready():
      found = True
  rx.cancel()
  return found


pi = pigpio.pi(PIGPIO_HOST, PIGPIO_PORT)
for baud_rate in range(BAUD_RATE_MIN, BAUD_RATE_MAX+1, 10):
  if detect(pi, baud_rate):
    print("😀 message detected for baud rate", baud_rate)
  else:
    print("😡 nothing detected for baud rate", baud_rate)
pi.stop()
