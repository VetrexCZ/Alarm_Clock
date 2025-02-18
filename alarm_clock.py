# Python Alarm clock !
# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

from playsound import playsound
import time

# Escape codes for terminal
CLEAR = "\033[2J"  # Deletes the screen
CLEAR_AND_RETURN = "\033[H"  # Moves the cursor to the top left corner of the screen


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  # 125 // 60 = 2 Integer division (without residue)
        seconds_left = time_left % 60  # 125 % 60 = 5 Returns the remainder after integer division

        # Format :02d displays the number with at least 2 digits, adding a leading zero if necessary
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("Internet_projects\\Alarm_clock\\alarm.mp3")


while True:
    try:
        minutes = int(input("How many minutes to wait: "))
        if minutes < 0:
            raise ValueError("Minutes must be a non-negative integer.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        seconds = int(input("How many seconds to wait: "))
        if seconds < 0:
            raise ValueError("Seconds must be a non-negative integer.")
        break
    except ValueError as e:
        print(e)
        
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
