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
        Clock.schedule_once(lambda dt: send_notification_med(med_name), delay)
    print("scheduling")


def send_notification_med(med_name):
    notification.notify(title='Medication Reminder', message=f'Time to take your medication: {med_name}')
    print("sending")

def send_notification_apt(patient_name):
    notification.notify(title='Appointment Reminder', message=f'Time for your appointment with: {patient_name}')
    print(f"Notification sent to {patient_name}")

def schedule_appointment_notification(p_name, time_to_take, date):
    # Parse the date provided to a datetime object
    appointment_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    today_date = datetime.datetime.now().date()
    print("scheduling")
    # Check if the appointment date is today
    if appointment_date.date() == today_date:
        print("hiiiii")
        print(appointment_date.date(), today_date)
        now = datetime.datetime.now()
        med_time = datetime.datetime.strptime(time_to_take, '%H:%M')
        med_time = med_time.replace(year=now.year, month=now.month, day=now.day)
        
        delay = (med_time - now).total_seconds()
        print(now, med_time, delay )
        # Check if the time is within the next 5 minutes or has already passed
        if 0 <= delay <= 5 * 60:
            send_notification_apt(p_name)
        elif delay > 0:
            # Schedule the notification if more than 5 minutes away
            Clock.schedule_once(lambda dt: send_notification_apt(p_name), delay)
        else:
            print("The time for appointment has already passed.")
    else:
        print("The specified date is not today.")

