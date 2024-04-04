import pymongo
import sha256 as sha256
import os
import json
import tempfile
from triple_des import decrypted, encrypted
from kivymd.toast import toast
from notification import *
# Replace with your MongoDB connection string
mongo_uri = 'mongodb+srv://sonadas8april:riyadasdas@cluster0.x0jnn5h.mongodb.net/'

# Create a MongoClient
client = pymongo.MongoClient(mongo_uri)

# Replace with your database name
db = client['HelpDroid']

# Replace with your collection name
collection = db['User']

# Insert a document into the collection

def insert_data(email,password,mobile,name,role):
    # data = {'email': email, 'password': password,'mobile':mobile, 'name': name}
    # collection.insert_one(data)
    try:
        
        hash = sha256.sha256(password+""+email)
        
        data = {'email': email, 'password': hash,'mobile':mobile, 'name': name, 'role':role}
        collection.insert_one(data)
        print("Inserted")
    except Exception as e:
        print(f"Error:  (An error occurred)")

    # query = {'email': "Jlhn@john"}
def update(email_input,new_pass):
    filter_criteria = {"email": email_input}

    # Define the update operation (e.g., set a new value for a field)
    update_operation = {"$set": {"password": new_pass}}

    # Update the document in the collection
    collection.update_one(filter_criteria, update_operation)

    
def find(query):
   matching_documents = collection.find(query)
   return matching_documents
   
       
def loginotpcheck(email_input):
    query = {'email': email_input}
    matching_documents = collection.find(query)
    for document in matching_documents:
        print("Login Successful")
        role=(document['role'])
        if(role):
            return "Doctor"
        else:
            return "Patient"

    return None


def append_encrypted_image_to_prescription(path):
    # Encrypt the image data

    # Append the encrypted image to the prescription array of the document identified by the email
    if os.path.exists('session.json'):
        with open('session.json', 'r') as session_file:
            session_data = json.load(session_file)
            email = session_data.get('user_email')
            encrypted_image = encrypted(path)

            result = collection.update_one(
                {"email": email},
                {"$push": {"prescription_images": encrypted_image}}
            )

            # Check if the update was successful
            if result.modified_count > 0:
                print(f"Image appended to prescription for {email}")
            else:
                print(f"No document found with email {email} or no update was needed.")

                
def fetch_and_decrypt_prescription_images():
    # Fetch the document for the given email

    if os.path.exists('session.json'):
        with open('session.json', 'r') as session_file:
            session_data = json.load(session_file)
            email = session_data.get('user_email')
            document = collection.find_one({"email": email})

            # Check if the document was found
            if document:
                encrypted_images = document.get("prescription_images", [])

                decrypted_images = []
                for encrypted_image in encrypted_images:
                    image_bytes = decrypted(encrypted_image)  # Replace with your decryption method
                    # Save the decrypted image to a temporary file
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
                        temp_file.write(image_bytes)
                        temp_file_path = temp_file.name
                    decrypted_images.append({
                        "path": temp_file_path,
                        "subtitle": "Decrypted Image"
                    })
                return decrypted_images
            
            
            else:
                print(f"No document found with email {email}")
                return []

 

def read_email_from_session():
    with open('session.json', 'r') as file:
        session_data = json.load(file)
        return session_data.get('user_email', None)

def insert_contact(name='user', email1=None, mobile=None):
    email = read_email_from_session()
    if not email:
        print("No email found in session.")
        return

    if email1 is None:
        toast("Email is required.")
        return
    if mobile is None:
        toast("Mobile is required.")
        return
    contact_data = {"name": name, "email": email1, "mobile": mobile}

    try:
        print(contact_data)
        # Update the existing user document to add the contact
        update_result = collection.update_one(
            {"email": email},
            {"$push": {"contacts": contact_data}},
            upsert=False
        )
        if update_result.matched_count == 0:
            print("No user found with the provided email.")
            return False
        elif update_result.modified_count > 0:
            print("Contact inserted successfully.")
            return True
        else:
            print("No update was made, possibly because the contact already exists.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def fetch_contacts():
    email = read_email_from_session()
    if not email:
        print("No email found in session.")
        return

    try:
        # Fetch the user document
        user_document = collection.find_one({"email": email})

        # Check if the document was found
        if user_document:
            contacts = user_document.get("contacts", [])
            return contacts
        else:
            print(f"No document found with email {email}")
            return []

    except Exception as e:
        print(f"Error: {e}")
        return []
def user_details():
    email = read_email_from_session()
    if not email:
        print("No email found in session.")
        return

    try:
        # Fetch the user document
        user_document = collection.find_one({"email": email})

        # Check if the document was found
        if user_document:
            return user_document
        else:
            print(f"No document found with email {email}")
            return []

    except Exception as e:
        print(f"Error: {e}")
        return []

def insert_medication(med_name,med_time):
    email = read_email_from_session()
    if not email:
        print("No email found in session.")
        return

    if med_name is None or med_time is None:
        toast("Email is required.")
        return

    med_data = {"name": med_name, "time": med_time}

    try:
        # Update the existing user document to add the contact
        update_result = collection.update_one(
            {"email": email},
            {"$push": {"medication": med_data}},
            upsert=False
        )
        
        
        if update_result.modified_count > 0:
            print("medication inserted successfully.")
            schedule_medication_notification(med_name, med_time)
            return True
        else:
            print("No update was made, possibly because the contact already exists.")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False
def get_medications_details():
    email = read_email_from_session()
    # Replace with your collection name
    user_data = collection.find_one({"email": email})
    if user_data and "medication" in user_data:
        return user_data["medication"]
    return []
def delete_medication(med_name,med_time):
    email = read_email_from_session()
    if not email:
        print("No email found in session.")
        return

    if med_name is None or med_time is None:
        toast("Email is required.")
        return

    med_data = {"name": med_name, "time": med_time}

    try:
        # Update the existing user document to add the contact
        update_result = collection.update_one(
            {"email": email},
            {"$pull": {"medication": med_data}},
            upsert=False
        )
        
        
        if update_result.modified_count > 0:
            print("medication deleted successfully.")
            return True
        else:
            print("No update was made, possibly because the contact already exists.")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False
def send_notification():
    try:
        med_timings = get_medications_details()
        for med_timing in med_timings:
            schedule_medication_notification(med_timing["name"], med_timing["time"])
    except Exception as e:
        print("Error")
   