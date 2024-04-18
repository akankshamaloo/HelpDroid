from kivy.clock import Clock
from plyer import notification
import datetime

def schedule_medication_notification(med_name, time_to_take):
    # Calculate the time difference from now to the medication time
    now = datetime.datetime.now()
    med_time = datetime.datetime.strptime(time_to_take, '%H:%M')
    med_time = now.replace(hour=med_time.hour, minute=med_time.minute, second=0, microsecond=0)
    delay = (med_time - now).total_seconds()

    if delay > 0:
        # Schedule the notification
        Clock.schedule_once(lambda dt: send_notification(med_name), delay)
    print("scheduling")

def send_notification(med_name):
    notification.notify(title='Medication Reminder', message=f'Time to take your medication: {med_name}')
    print("sending")

# Example usage

