

def reg_auth(email_input,otp_input,password_input,name_input,mobile_input,otp_sent):
    print(otp_input,"..",otp_sent)
    if(otp_input==otp_sent):
        return True
    else:
        return False
         