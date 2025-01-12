#Step 1 : Import the necessary librairies
import time

##################################################################################
#Initialization of the variables
paused = False
hours = 0
minutes = 0
seconds = 0
alarm_hour = 0
alarm_minute = 0
alarm_second = 0

###################################################################################
#Step 2 : define the functions 
def up_date_time(): #up date the time
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


def format_time(): #choose the format 
    global hours, minutes, seconds, format_choice, local_time
    local_time = time.localtime()
    set_time = time.struct_time((2025, 1, 6, hours, minutes, seconds, 0, 0, -1))
    if format_choice == '12h':
        return time.strftime("%I:%M:%S %p", set_time) #for the 12h format, we have to add the %p options to destinguish between morning and afternoon
    elif format_choice == '24h':
        return time.strftime("%H:%M:%S", set_time)  
    else:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")


def alarm_setting(): #Check if the alarm time matches the current time
    global hours, minutes, seconds
    global alarm_hour, alarm_minute, alarm_second
    return (hours == alarm_hour and minutes == alarm_minute and seconds == alarm_second)

def break_clock():
    global paused
    paused = not paused
    if paused:
        print("Clock paused.")
    else:
        print("Clock resumed.")

####################################################################################################################
#Step 3 : Enter the values
print(f"Hello, Here is the Granny clock !")

try:
    hours = int(input("Please enter current hour (0 - 23): "))
    minutes = int(input("Please enter current minute (0 - 59): "))
    seconds = int(input("Please enter current second (0 - 59): "))
    
    if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
        raise ValueError("Time values out of range")

except ValueError :
    print(f"Error")
    exit()

print("To exit, press Ctrl + C")

#####################################################################################################################
#Step 4 : Choose the adequated format 
try:
    format_choice = input("Please, choose the adequate format (12h / 24h): ").strip().lower()
    if format_choice not in ['12h', '24h']:
        raise ValueError("Invalid format choice! Please choose '12h' or '24h'.")

except ValueError as e:
    print(f"Error: {e}")
    exit()

########################################################################################################################
#Step 5 : Set the alarm
alarm_ = input("\nDo you want to set the alarm ? ((Yes/No))").strip().lower()

try :
    if alarm_ == 'Yes' :
        print (f"Please, set the alarm")

        alarm_hour = int(input("Choose the alarm hour (0 - 23) : "))
        alarm_minute = int(input("Choose the alarm minute (0 - 23) : "))
        alarm_second = int(input("Choose the alarm second (0 - 23) : "))

        if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60 and 0 <= alarm_second < 60):
                raise ValueError("Time values out of range")

    elif alarm_ == 'No' :
        print('')

    else :
        print("I didn't understand your request. Please answer by 'yes' or 'no'!")

except ValueError :
        print(f"Error")
        exit()

####################################################################################################################
#Step 6 : Call the different functions (the main loop)
try:
    while True:
        formatted_time = format_time()
        print(f"The current time is: {formatted_time}", end="\r")

        if alarm_setting():
            print("\nIt's wake-up time!")
        
        if not paused :
            time.sleep(1) # This function introduces a 1 second delay (in this case) between each update.
            up_date_time() 

        if paused :
            input()
            break_clock()      

except KeyboardInterrupt:
    print("\nClock interrupted!")