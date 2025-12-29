import time
from digitalio import DigitalInOut, Direction, Pull
import board

key1 = DigitalInOut(board.D2)
key1.direction = Direction.INPUT
key1.pull = Pull.UP

key2 = DigitalInOut(board.D3)
key2.direction = Direction.INPUT
key2.pull = Pull.UP

key3 = DigitalInOut(board.D4)
key3.direction = Direction.INPUT
key3.pull = Pull.UP

key4 = DigitalInOut(board.D5)
key4.direction = Direction.INPUT
key4.pull = Pull.UP

timer_running = False
timer_start = 0
timer_duration = 15 * 60

def start_timer(duration=None):
    global timer_running, timer_start, timer_duration
    timer_running = True
    timer_start = time.monotonic()
    if duration:
        timer_duration = duration

def pause_timer():
    global timer_running, timer_duration, timer_start
    timer_duration -= time.monotonic() - timer_start
    timer_running = False

def reset_timer():
    global timer_running, timer_duration
    timer_running = False
    timer_duration = 25 * 60

while True:
    if not key1.value:
        start_timer(25*60)
        time.sleep(0.2)
    if not key2.value:
        if timer_running:
            pause_timer()
        else:
            start_timer(timer_duration)
        time.sleep(0.2)
    if not key3.value:
        reset_timer()
        time.sleep(0.2)
    if not key4.value:
        start_timer(5*60)
        time.sleep(0.2)

    if timer_running:
        elapsed = time.monotonic() - timer_start
        remaining = timer_duration - elapsed
        if remaining <= 0:
            timer_running = False
            print("Timer done!")
        else:
            print(f"Time remaining: {int(remaining // 60)}:{int(remaining % 60):02}", end='\r')
    time.sleep(0.1)
