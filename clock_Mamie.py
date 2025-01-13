# Step 1 : Import the necessary libraries
import os
import time
import keyboard
import winsound

##################################################################################
# Initialization of the variables
pause = False
hours = 0
minutes = 0
seconds = 0
alarm_hour = 0
alarm_minute = 0
alarm_second = 0
format_choice = ''  


###################################################################################
# Step 2 : Define the functions 
def up_date_time():  # Update the time
    global hours, minutes, seconds 
    seconds += 1 
    if seconds == 60: 
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
    return hours, minutes, seconds


def format_time():  # Choose the format 
    global hours, minutes, seconds, format_choice
    if format_choice == '':
        raise ValueError("You need to set the time format first (12h or 24h).")
    
    set_time = time.struct_time((2025, 1, 6, hours, minutes, seconds, 0, 0, -1))
    if format_choice == '12h':
        return time.strftime("%I:%M:%S %p", set_time)  # For the 12h format, we need the %p option to distinguish between morning and afternoon
    elif format_choice == '24h':
        return time.strftime("%H:%M:%S", set_time)
    else:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")


def alarm_setting():  # Check if the alarm time matches the current time
    global hours, minutes, seconds
    global alarm_hour, alarm_minute, alarm_second
    return (hours == alarm_hour and minutes == alarm_minute and seconds == alarm_second)

####################################################################################################################
# Step 3 : The menu
print(f"Hello, Here is the Granny's clock !")
print(f"1 - Press 'c' to set the clock")
print(f"2 - Press 'a' to set the alarm")
print(f"3 - Press 'p' to pause or resume the clock")
print(f"4 - Press 'q' to quit the clock (You can also press ctrl+C)")

####################################################################################################################
# Step 6 : The main loop

try:
    while True:
        if keyboard.is_pressed('c'):
            try:   
                hours = int(input("Please enter current hour (0 - 23): "))
                minutes = int(input("Please enter current minute (0 - 59): "))
                seconds = int(input("Please enter current second (0 - 59): "))
                
                if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                    raise ValueError("Time values out of range")
            
            except ValueError as e:
                print(f"Error: {e}")
                continue

            while True:
                try:
                    format_choice = input("Please, choose the adequate format (12h / 24h): ").strip().lower()
                    if format_choice not in ['12h', '24h']:
                        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

        elif keyboard.is_pressed('a'):
            try:
                print(f"Please, set the alarm")

                alarm_hour = int(input("Choose the alarm hour (0 - 23): "))
                alarm_minute = int(input("Choose the alarm minute (0 - 59): "))
                alarm_second = int(input("Choose the alarm second (0 - 59): "))

                if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60 and 0 <= alarm_second < 60):
                    raise ValueError("Time values out of range")
                
            except ValueError as e:
                print(f"Error: {e}")
                continue

        elif keyboard.is_pressed('p'):
            pause = not pause
            if pause:
                print("\nClock paused.")
            else:
                print("\nClock resumed.")
            time.sleep(1)  

        elif keyboard.is_pressed('q'):
            print("\nExiting the clock......")
            print("Goodbye !")
            break

        if not pause:
            # Only format time when the format_choice is valid
            if format_choice != '':
                formatted_time = format_time()
                print(f"The current time is: {formatted_time}", end="\r")

                if alarm_setting():
                    print(f"\nIt's {formatted_time}. It's wake-up time!")
                    for _ in range(3):
                        sound_file = 'C:\\chemin\\vers\\votre\\son.wav'
                        winsound.PlaySound(sound_file, winsound.SND_FILENAME)
                        time.sleep(0.2)
                        
    
            time.sleep(1)
            up_date_time()

except KeyboardInterrupt:
    print("\nClock interrupted!")
