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

def get_valid_input(prompt, input_type="minutes"):
    while True:
        try:
            value = input(f"Enter {prompt}: ")
            # Check if input is empty
            if not value.strip():
                print(f"Error: {input_type} cannot be empty. Please enter a number.")
                continue
            
            # Convert input to integer
            number = int(value)

            # Check for negative numbers
            if number < 0:
                print(f"Error: {input_type} cannot be negative. Please enter a positive number.")
                continue
            
            return number

        except ValueError:
            print(f"Error: Invalid input. Please enter a valid number for {input_type}.")


# Get minutes
minutes = get_valid_input("number of minutes", "minutes")

# Get seconds
seconds = get_valid_input("number of seconds", "seconds")

total_seconds = minutes * 60 + seconds
alarm(total_seconds)
