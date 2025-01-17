import tkinter as tk
from tkinter import messagebox
import threading
import time

current_time = (0, 0, 0)
alarm_time = None
is_12h_format = False
paused = False
stop_thread = False

def update_time():
    global current_time
    hours, minutes, seconds = current_time
    if not paused:
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

def display_time():
    global current_time, is_12h_format
    while not stop_thread:
        if not paused:
            hours, minutes, seconds = current_time
            if is_12h_format:
                display_hours = hours % 12
                display_hours = 12 if display_hours == 0 else display_hours
                am_pm = "AM" if hours < 12 else "PM"
                time_str = f"{display_hours:02d}:{minutes:02d}:{seconds:02d} {am_pm}"
            else:
                time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            time_label.config(text=time_str)
        time.sleep(1)
        update_time()

def set_time():
    global current_time
    try:
        time_str = time_entry.get()
        hours, minutes, seconds = map(int, time_str.split(':'))
        current_time = (hours, minutes, seconds)
        messagebox.showinfo("Success", "Time updated successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Use HH:MM:SS.")

def set_alarm():
    global alarm_time
    try:
        alarm_str = alarm_entry.get()
        hours, minutes, seconds = map(int, alarm_str.split(':'))
        alarm_time = (hours, minutes, seconds)
        messagebox.showinfo("Success", "Alarm set successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid alarm format. Use HH:MM:SS.")

def toggle_pause():
    global paused
    paused = not paused
    status_label.config(text="Paused" if paused else "Running")

def toggle_format():
    global is_12h_format
    is_12h_format = not is_12h_format

def check_alarm():
    global current_time, alarm_time
    if alarm_time and current_time == alarm_time:
        messagebox.showinfo("Alarm", f"Alarm! It's {alarm_time[0]:02d}:{alarm_time[1]:02d}:{alarm_time[2]:02d}")
        alarm_time = None  # Reset alarm after triggering

def on_close():
    global stop_thread
    stop_thread = True
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Clock with Alarm")

# Time display
time_label = tk.Label(root, font=("Helvetica", 48), text="00:00:00")
time_label.pack(pady=20)

# Time entry
time_entry = tk.Entry(root, font=("Helvetica", 16))
time_entry.pack(pady=10)
set_time_button = tk.Button(root, text="Set Time", command=set_time)
set_time_button.pack()

# Alarm entry
alarm_entry = tk.Entry(root, font=("Helvetica", 16))  # Ensure alarm_entry is defined
alarm_entry.pack(pady=10)
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack()

# Control buttons
pause_button = tk.Button(root, text="Pause/Resume", command=toggle_pause)
pause_button.pack(pady=5)

format_button = tk.Button(root, text="Toggle 12/24 Hour Format", command=toggle_format)
format_button.pack(pady=5)

status_label = tk.Label(root, text="Running", font=("Helvetica", 12))
status_label.pack(pady=10)

# Run the clock in a separate thread
thread = threading.Thread(target=display_time, daemon=True)
thread.start()

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_close)

# Start the Tkinter event loop
root.mainloop()
