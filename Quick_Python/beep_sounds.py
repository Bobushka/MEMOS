import beepy
import time

for i in range(1,8):
    print(i)
    beepy.beep(sound=i)
    time.sleep(1)
