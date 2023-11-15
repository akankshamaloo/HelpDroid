from pymongo import MongoClient
from firebase_admin import messaging, credentials, initialize_app
import datetime

# Firebase Admin Initialization
cred = credentials.Certificate("helpdroid-fa971-firebase-adminsdk-bmofw-25ebeda380.json")
initialize_app(cred)

# MongoDB Connection
client = MongoClient("mongodb_connection_string")
db = client.your_database_name
meds_collection = db.medications

def send_notification(device_token, message):
    # Constructing the Firebase message
    message = messaging.Message(
        notification=messaging.Notification(
            title='Medication Reminder',
            body=message
        ),
        token=device_token,
    )
    # Sending the message
    response = messaging.send(message)
    print('Successfully sent message:', response)

def check_and_notify():
    # Current time in HH:MM format
    current_time = datetime.datetime.now().strftime("%H:%M")
    query = {"time": current_time}
    for med in meds_collection.find(query):
        message = f"It's time to take your {med['name']}"
        send_notification(med['device_token'], message)

# Running the function
check_and_notify()
