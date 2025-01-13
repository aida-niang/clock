# Step 1 : Import the necessary libraries
import time


# Initialization of the variables
hours = 0
minutes = 0
seconds = 0
paused = False

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
    set_time = time.struct_time((2025, 1, 6, hours, minutes, seconds, 0, 0, -1))
    if format_choice == '12h':
        return time.strftime("%I:%M:%S %p", set_time)  # 12-hour format
    elif format_choice == '24h':
        return time.strftime("%H:%M:%S", set_time)  # 24-hour format
    else:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")


def alarm_setting():  # Check if the alarm time matches the current time
    global hours, minutes, seconds, alarm_hour, alarm_minute, alarm_second
    return hours == alarm_hour and minutes == alarm_minute and seconds == alarm_second


####################################################################################################################
# Step 3 : Enter the values
try:
    current_time = input("Enter the current Time in HH:MM:SS format: ")
    hours, minutes, seconds = map(int, current_time.split(':'))

    if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
        raise ValueError("Time values out of range")

except ValueError:
    print("Error: Invalid time format or values out of range.")
    exit()

#####################################################################################################################
# Step 4 : Choose the adequate format
try:
    format_choice = input("Choose the adequate format (12h / 24h): ").strip().lower()
    if format_choice not in ['12h', '24h']:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")

except ValueError as e:
    print(f"Error: {e}")
    exit()

########################################################################################################################
# Step 5 : Set the alarm
try:
    print("Please, set the alarm.")
    alarm_time = input("Choose the alarm time in HH:MM:SS format: ")
    alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(':'))

    if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60 and 0 <= alarm_second < 60):
        raise ValueError("Alarm time values out of range")

except ValueError:
    print("Error: Invalid alarm time format or values out of range.")
    exit()

####################################################################################################################
# Step 6 : Call the different functions (the main loop)
print("To exit, press Ctrl + C")

try:
    while True:
        formatted_time = format_time()
        print(f"The current time is: {formatted_time}", end="\r")

        if alarm_setting():
            print("\n⏰ It's wake-up time!")
            break
 
        time.sleep(1)  # This function introduces a 1-second delay between updates.
        up_date_time()

except KeyboardInterrupt:
    print("\nClock interrupted!")
