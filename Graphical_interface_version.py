import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

####################################################################################################################
# Create the window for the clock
fig, ax = plt.subplots()
ax.axis('off')
text_Clock = ax.text(0.5, 0.5, '', transform=ax.transAxes, ha='center', fontsize=40, color = 'red')
####################################################################################################################

# Create my clock
#define the functions

def up_date_time(hours, minutes, seconds):  # Update the time
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

def format_time(hours, minutes, seconds, format_choice):  
    struct_time = time.struct_time((2025, 1, 6, hours, minutes, seconds, 0, 0, -1))
    if format_choice == '12h':
        return time.strftime("%I:%M:%S %p", struct_time)  
    elif format_choice == '24h':
        return time.strftime("%H:%M:%S", struct_time) 
    else:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")

def alarm_setting(current_h, current_m, current_s, alarm_h, alarm_m, alarm_s):  
    return (current_h == alarm_h and current_m == alarm_m and current_s >= alarm_s)

def init():    #this function is the equivalent of print_time()
    text_Clock.set_text('') #It initialize the animation of the text
    return text_Clock,

def update_text_clock(frame):  # Update the text during the animation
    global hours, minutes, seconds #global allow this function to modify these variables (they are not local) and this modification will be visible in the hole program
    formatted_time = format_time(hours, minutes, seconds, format_choice) #call the function to convert tuple into string

    
    MESSAGE = ''
    if alarm_setting(hours, minutes, seconds, alarm_hour, alarm_minute, alarm_second):
        ALARM = format_time(alarm_hour, alarm_minute, alarm_second, format_choice)
        MESSAGE = f"It's {ALARM}. It's wake-up time!" #verify the alarm and print this message
    
    text_Clock.set_text(formatted_time + "\n" + MESSAGE) #update the string shown in the figure
    hours, minutes, seconds = up_date_time(hours, minutes, seconds) #call the function to update the values of hours, minutes and seconds
    
    return text_Clock, #the returned value will be used by FuncAnimation 

#################################################################################################################
# Enter the values
try:
    hours = int(input("Enter current hour (0 - 23): "))
    minutes = int(input("Enter current minute (0 - 59): "))
    seconds = int(input("Enter current second (0 - 59): "))

    if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
        raise ValueError("Time values out of range")

except ValueError:
    print("Error")
    exit()

###################################################################################
# Choose the format
try:
    format_choice = input("Choose the adequate format (12h / 24h): ").strip().lower()
    if format_choice not in ['12h', '24h']:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")

except ValueError as e:
    print(f"Error: {e}")
    exit()

########################################################################################################
# Set the alarm
try:
    print(f"Please, set the alarm")

    alarm_hour = int(input("Choose the alarm hour (0 - 23): "))
    alarm_minute = int(input("Choose the alarm minute (0 - 59): "))
    alarm_second = int(input("Choose the alarm second (0 - 59): "))

    if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60 and 0 <= alarm_second < 60):
        raise ValueError("Time values out of range")

except ValueError:
    print("Error")
    exit()

#########################################################################################

# Create the animation for the clock in the figure
animate = FuncAnimation(fig, update_text_clock, frames=np.arange(0, 100), init_func=init, interval=1000, blit=True)

# Show my clock in the figure
plt.show()
