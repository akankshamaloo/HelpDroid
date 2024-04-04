from connection import *
from sha256 import *
from kivymd.toast import toast
def reg_auth(email_input,otp_input,password_input,name_input,mobile_input,otp_sent,role):
    print(otp_input,"..",otp_sent)
    if(otp_input==otp_sent):
       
        insert_data(email_input,password_input,mobile_input,name_input,role)
        return True
    else:
        toast("OTP not matched")
        return False
def login_auth(email_input, password_input=None):
    # If a password is provided, hash it together with the email to check for a match.
    if password_input is not None:
        hash = sha256(password_input + "" + email_input)
        matching_documents = find({"email": email_input, "password": hash})
    else:
        # If no password is provided, check only based on the email.
        matching_documents = find({"email": email_input})

    for document in matching_documents:
        print(document)
        role=(document['role'])
        if(role):
            return "Doctor"
        else:
            return "Patient"

    return None

