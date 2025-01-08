import time
from datetime import datetime, timedelta
from threading import Event, Thread

# === Global Variables Section ===
set_time = None  
alarm_time = None  
pause_event = Event()  # Event to control the pause
pause_event.set()  # The clock starts active by default

# === Display Time Function Section ===
def display_time(mode=True):
    global set_time, alarm_time  
    try:
        while True:
            if set_time:
                current_time = set_time
                set_time += timedelta(seconds=1)  
            else:
                current_time = datetime.now()

            # Format the time based on the selected mode (24-hour or 12-hour)
            if mode:
                formatted_time = current_time.strftime("%H:%M:%S")  # 24-hour format
            else:
                formatted_time = current_time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM

            print(f"\r{formatted_time}", end="")

            # Check if the current time matches the alarm time
            if alarm_time and current_time.strftime("%H:%M:%S") == alarm_time.strftime("%H:%M:%S"):
                print(f"\n🔔 Alarm! It's time: {formatted_time}")
                alarm_time = None  # Reset the alarm after it goes off

            time.sleep(1)

            # Check if the clock is paused, in that case, stop the display
            pause_event.wait()
    except KeyboardInterrupt:
        print("\nProgram stopped.")  # Display this message when Ctrl+C is pressed

# === Mode Selection Function Section ===
def select_mode():
    while True:
        choice = input("Choose the time display mode (12h or 24h): ").strip().lower()
        if choice == "12h":
            return False  
        elif choice == "24h":
            return True  
        else:
            print("❌ Invalid choice. Please enter '12h' or '24h'.")

# === Time Setting Function Section ===
def set_time_function(hours, minutes, seconds):
    global set_time  
    current_time = datetime.now()
    # Set the time using the given hours, minutes, and seconds
    set_time = current_time.replace(hour=hours, minute=minutes, second=seconds)
    print(f"\nTime set to {set_time.strftime('%H:%M:%S')}.\n")  # Display the new time

# === Alarm Setting Function Section ===
def set_alarm(hours, minutes, seconds):
    global alarm_time  
    current_time = datetime.now()
    # Set the alarm time
    alarm_time = current_time.replace(hour=hours, minute=minutes, second=seconds)
    print(f"Alarm set for {alarm_time.strftime('%H:%M:%S')}.\n")  # Display the alarm time

# === Pause and Resume Functions Section ===
def pause_clock():
    pause_event.clear()  # Stops the clock by clearing the event
    print("\n⏸️ Clock paused.\n")

def resume_clock():
    pause_event.set()  # Resumes the clock by setting the event
    print("\n▶️ Clock resumed.\n")

# === Main Loop Section ===
def main():
    while True:
        # 1. Ask the user to choose the time display mode (12h or 24h)
        print("Welcome to the time display program.\n")
        mode = select_mode()  # Get the user's choice for time mode

        # Start displaying the time in a separate thread
        time_thread = Thread(target=display_time, args=(mode,))
        time_thread.daemon = True  # The thread will end when the main program ends
        time_thread.start()

        # 2. Ask if the user wants to set the time
        set_time_input = input("\nDo you want to set the time? (yes/no): ").strip().lower()
        if set_time_input == "yes":
            hours = int(input("Enter hours (0-23): "))
            minutes = int(input("Enter minutes (0-59): "))
            seconds = int(input("Enter seconds (0-59): "))
            set_time_function(hours, minutes, seconds)
        else:
            print(f"Current time: {datetime.now().strftime('%H:%M:%S')}\n")

        # 3. Ask if the user wants to set an alarm
        alarm_set_input = input("\nDo you want to set an alarm? (yes/no): ").strip().lower()
        if alarm_set_input == "yes":
            alarm_hours = int(input("Enter alarm hour (0-23): "))
            alarm_minutes = int(input("Enter alarm minutes (0-59): "))
            alarm_seconds = int(input("Enter alarm seconds (0-59): "))
            set_alarm(alarm_hours, alarm_minutes, alarm_seconds)

        # 4. Ask if the user wants to pause the clock and possibly resume it
        pause_input = input("\nDo you want to pause the clock? (yes/no): ").strip().lower()
        if pause_input == "yes":
            pause_clock()

            # Ask if the user wants to resume the clock
            resume_input = input("Do you want to resume the clock? (yes/no): ").strip().lower()
            if resume_input == "yes":
                resume_clock()

        # 5. Ask if the user wants to quit
        quit_input = input("\nDo you want to quit? (yes/no): ").strip().lower()
        if quit_input == "yes":
            print("👋 Goodbye!")
            break  # Exit the loop and stop the program

# === Execution Section ===
try:
    main()
except KeyboardInterrupt:
    print("\nProgram stopped.")  