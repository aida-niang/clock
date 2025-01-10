import time
import threading

current_time = (0, 0, 0)
alarm_time = None
is_12h_format = False
paused = False
stop_thread = False

def display_time():
    global current_time, is_12h_format, paused, stop_thread
    while not stop_thread:
        if not paused:
            if is_12h_format:
                hours = current_time[0] % 12
                hours = 12 if hours == 0 else hours
                am_pm = "AM" if current_time[0] < 12 else "PM"
                print("\r{:02d}:{:02d}:{:02d} {}".format(hours, current_time[1], current_time[2], am_pm), end="")
            else:
                print("\r{:02d}:{:02d}:{:02d}".format(current_time[0], current_time[1], current_time[2]), end="")
            time.sleep(1)
            update_time()

def update_time():
    global current_time
    hours, minutes, seconds = current_time
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
    current_time = (hours, minutes, seconds)
    check_alarm()

def set_time():
    global current_time
    print("Please enter the time in the format HH:MM:SS")
    time_str = input("Enter the time: ")
    hours, minutes, seconds = map(int, time_str.split(':'))
    current_time = (hours, minutes, seconds)

def set_alarm():
    global alarm_time
    print("Please enter the alarm time in the format HH:MM:SS")
    alarm_str = input("Enter the alarm time: ")
    hours, minutes, seconds = map(int, alarm_str.split(':'))
    alarm_time = (hours, minutes, seconds)

def choose_display_format():
    global is_12h_format
    mode = input("Choose the display format (12/24): ")
    is_12h_format = (mode == "12")

def toggle_pause():
    global paused
    paused = not paused
    if paused:
        print("\rClock paused.   ", end="")
    else:
        print("\rClock resumed.  ", end="")

def check_alarm():
    global current_time, alarm_time
    if alarm_time and current_time == alarm_time:
        print("\rAlarm! It's {:02d}:{:02d}:{:02d}   ".format(current_time[0], current_time[1], current_time[2]), end="")

def main():
    global stop_thread
    set_time()
    set_alarm()
    choose_display_format()

    thread = threading.Thread(target=display_time)
    thread.start()

    try:
        while True:
            # Ajout d'un message d'invite sur une nouvelle ligne
            print("\nPress Enter to pause or resume the clock:")
            input()
            toggle_pause()
    except KeyboardInterrupt:
        stop_thread = True
        thread.join()

if __name__ == "__main__":
    main()
