from connection import *
from sha256 import *
def reg_auth(email_input,otp_input,password_input,name_input,mobile_input,otp_sent):
    print(otp_input,"..",otp_sent)
    if(otp_input==otp_sent):
       
        insert_data(email_input,password_input,mobile_input,name_input)
        return True
    else:
        return False
def login_auth(email_input,password_input):
    hash = sha256(password_input+""+email_input)
    
    matching_documents = find({"email":email_input,"password":hash})   
    for document in matching_documents:
        print(document)
        return True
    return False